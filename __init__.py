# -*- coding: utf-8 -*-

import re
import os
from shutil import copy

from anki.hooks import addHook
from aqt import mw
from aqt.utils import showInfo
from aqt.addcards import AddCards
from aqt.browser import Browser
from aqt.editcurrent import EditCurrent
from aqt.utils import tooltip
from anki.hooks import addHook, wrap
from aqt.editor import Editor
from aqt.qt import *
from .model import enhancedModel

# global variables
genuine_cloze_answer_array = []
genuine_cloze_hint_array = []
pseudo_cloze_answer_array = []
pseudo_cloze_hint_array = []
current_cloze_field_number = 0

# constants
MODEL_NAME = "Enhanced Cloze"
CONTENT_FIELD_NAME = "# Content"
IN_USE_CLOZES_FIELD_NAME = "In-use Clozes"
UPDATE_ENHANCED_CLOZE_SHORTCUT = "Ctrl+Alt+C"


def generate_enhanced_cloze(note):
    # cloze_id means, eg. c1, cloze_number means, eg. 1

    src_content = note[CONTENT_FIELD_NAME]

    # Get ids of in-use clozes
    cloze_start_regex = r"\{\{c\d+::"
    cloze_start_matches = re.findall(cloze_start_regex, src_content)

    # if no clozes are found, empty Cloze1 ~ Cloze20 and fill in Cloze99
    if not cloze_start_matches:
        for i_cloze_field_number in range(1, 20 + 1):
            dest_field_name = "Cloze%s" % i_cloze_field_number
            note[dest_field_name] = ""

        note[IN_USE_CLOZES_FIELD_NAME] = "[0]"

        # Anki will warn if cloze notes include no cloze or more strictly, no single-line cloze
        # so I use a invisible single-line cloze {{cX::@@@@}} to cheat Anki :)
        note["Cloze1"] = src_content + \
            '<div style="display:none">{{c1::@@@@}}</div>' + \
            '<div id="card-cloze-id" style="display:none">c0</div>'
        return
    else:
        in_use_clozes_numbers = sorted(
            [int(re.sub(r"\D", "", x)) for x in set(cloze_start_matches)])
        note[IN_USE_CLOZES_FIELD_NAME] = str(in_use_clozes_numbers)

        # Fill in content in in-use cloze fields and empty content in not-in-use fields
        global current_cloze_field_number
        for current_cloze_field_number in range(1, 20 + 1):

            dest_field_name = "Cloze%s" % current_cloze_field_number
            dest_field_content = ""

            if not current_cloze_field_number in in_use_clozes_numbers:
                dest_field_content = ""
            else:
                # Initialize the lists to store different content on each card later
                global genuine_cloze_answer_array
                global genuine_cloze_hint_array
                global pseudo_cloze_answer_array
                global pseudo_cloze_hint_array

                del genuine_cloze_answer_array[:]
                del genuine_cloze_hint_array[:]
                del pseudo_cloze_answer_array[:]
                del pseudo_cloze_hint_array[:]

                dest_field_content = src_content

                cloze_regex = r"\{\{c\d+::[\s\S]*?\}\}"
                dest_field_content = re.sub(
                    cloze_regex, process_cloze, dest_field_content)

                # Store corresponding answers and hints (gunuine or pseudo)
                # in html of every in-use cloze fields for javascript to fetch later
                for index, item in enumerate(genuine_cloze_answer_array):
                    dest_field_content += '<pre style="display:none"><div id="genuine-cloze-answer-%s">%s</div></pre>' % (
                        index, item)
                for index, item in enumerate(genuine_cloze_hint_array):
                    dest_field_content += '<pre style="display:none"><div id="genuine-cloze-hint-%s">%s</div></pre>' % (
                        index, item)
                for index, item in enumerate(pseudo_cloze_answer_array):
                    dest_field_content += '<pre style="display:none"><div id="pseudo-cloze-answer-%s">%s</div></pre>' % (
                        index, item)
                for index, item in enumerate(pseudo_cloze_hint_array):
                    dest_field_content += '<pre style="display:none"><div id="pseudo-cloze-hint-%s">%s</div></pre>' % (
                        index, item)

                dest_field_content += '<div style="display:none">{{c%s::@@@@}}</div>' % current_cloze_field_number
                dest_field_content += '<div id="card-cloze-id" style="display:none">c%s</div>' % str(
                    current_cloze_field_number)

            note[dest_field_name] = dest_field_content
        return


def check_model(model):
    """Whether this model is Enhanced cloze version 2.1"""
    return re.search("Enhanced Cloze 2.1", model["name"])

def exists_model():
    "Whether the collection contains model Enhanced Cloze 2.1"
    for model in mw.col.models.all():
        if check_model(model):
            return True
    return False

def process_cloze(matchObj):

    cloze_string = matchObj.group()  # eg. {{c1::aa[::bbb]}}
    index_of_answer = cloze_string.find("::") + 2
    index_of_hint = cloze_string.rfind("::") + 2
    cloze_id = cloze_string[2: index_of_answer - 2]  # like: c1 or c11
    cloze_length = len(cloze_string)

    answer = ""
    hint = ""
    if index_of_answer == index_of_hint:  # actually no hint at all
        answer = cloze_string[index_of_answer: cloze_length - 2]
        hint = ""
    else:
        answer = cloze_string[index_of_answer: index_of_hint - 2]
        hint = cloze_string[index_of_hint: cloze_length - 2]

    global current_cloze_field_number
    if cloze_id != 'c' + str(current_cloze_field_number):
        # Process pseudo-cloze
        global pseudo_cloze_answer_array
        global pseudo_cloze_hint_array
        pseudo_cloze_answer_array.append(answer)
        pseudo_cloze_hint_array.append(hint)
        index_in_array = len(pseudo_cloze_answer_array) - 1
        new_html = '<span class="pseudo-cloze" index="_index_" show-state="hint" cloze-id="_cloze-id_">_content_</span>'
        new_html = new_html.replace('_index_', str(index_in_array)).replace(
            '_cloze-id_', cloze_id).replace('_content_', cloze_string.replace("{", '[').replace("}", "]"))
        return new_html
    else:
        # Process genuine-cloze
        global genuine_cloze_answer_array
        global genuine_cloze_hint_array
        genuine_cloze_answer_array.append(answer)
        genuine_cloze_hint_array.append(hint)
        index_in_array = len(genuine_cloze_answer_array) - 1
        new_html = '<span class="genuine-cloze" index="_index_" show-state="hint" cloze-id="_cloze-id_">_content_</span>'
        new_html = new_html.replace('_index_', str(index_in_array)).replace(
            '_cloze-id_', cloze_id).replace('_content_', cloze_string)
        return new_html

def update_all_enhanced_clozes_in_browser(self, evt=None):
    browser = self
    mw = browser.mw

    mw.checkpoint("Update Enhanced Clozes")
    mw.progress.start()
    browser.model.beginReset()

    update_all_enhanced_cloze(self)

    browser.model.endReset()
    mw.requireReset()
    mw.progress.finish()
    mw.reset()


def update_all_enhanced_cloze(self):
    mw = self.mw
    nids = mw.col.findNotes("*")
    for nid in nids:
        note = mw.col.getNote(nid)
        if not check_model(note.model()):
            continue
        generate_enhanced_cloze(note)
        note.flush()


def setup_menu(self):
    browser = self
    menu = browser.form.menuEdit
    menu.addSeparator()
    a = menu.addAction('Update Enhanced Clozes')
    a.setShortcut(QKeySequence(UPDATE_ENHANCED_CLOZE_SHORTCUT))
    a.triggered.connect(
        lambda _, b=browser: update_all_enhanced_clozes_in_browser(b))



_oldSaveNow = Editor.saveNow
def on_save_now(self, *args, **kwargs):
    if self.web is None: # This occur if the window is already closing, but closing has not yet ended.
        return
    self.web.eval("saveField('key');")
    note = self.note
    if not note or not check_model(note.model()):
        return _oldSaveNow(self, *args, **kwargs)
    self.saveTags()

    generate_enhanced_cloze(note)

    self.loadNote()
    self.web.setFocus()
    self.web.eval(f"focusField({self.currentField});")
    ret = _oldSaveNow(self, *args, **kwargs)
    return ret

Editor.saveNow = on_save_now

def onCloze(self):
    _oldSaveNow(self, self._onCloze, keepFocus = True)
Editor.onCloze = onCloze
Editor._links["cloze"] = onCloze

# AddCards.addCards = wrap(AddCards.addCards, on_add_cards, "around")

# EditCurrent.onSave = wrap(EditCurrent.onSave, on_edit_current_save, "around")





addHook("browser.setupMenus", setup_menu)

def addModel():
    if exists_model():
        #print("Model exists")
        return
    mw.col.models.add(enhancedModel)
    jsToCopy = ["_Autolinker.min.js", "_jquery-3.2.1.min.js", "_jquery.hotkeys.js", "_jquery.visible.min.js"]
    for file in jsToCopy:
        file = os.path.join(mw.addonManager.addonsFolder(__name__), file)
        print(f"File is {file}")
        copy(file,mw.col.media.dir())

addHook("profileLoaded", addModel)
