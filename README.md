# Enhanced cloze 2.1
This add-on allows to improve clozes usage. See the [original author](https://ankiweb.net/shared/info/873439973) description for more details. The only thing that changed is that you don't need JSbooster anymore.

## Warning
Make a backup before updating from 2.0 note type to 2.1 note type.

If you used those cards with anki 2.0, you need:
* either to change the note type to "Enhanced cloze 2.1" [Improving «change note type»](https://ankiweb.net/shared/info/513858554) may help you to do the change more safely, since those are clozed note.
* or to copy the front of the note type "Enhanced cloze 2.1" to "Enhanced cloze", remove "Enhanced cloze 2.1" and rename "Enhanced cloze" to "Enhanced cloze 2.1" (this one is more technical, but also safer)

## Internal
It edit the method `aqt.editor.Editor.saveNow`, the new method calls
the last one.

## Version 2.0
[Here](https://ankiweb.net/shared/info/873439973)

## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Version 2.0 by | [https://github.com/luzhe610/anki-enhanced-cloze](luzhe610)
Ported to 2.1 by | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-enhanced-cloze
Addon number| [2062736101](https://ankiweb.net/shared/info/2062736101)
Support luzhe610| https://www.paypal.me/LuZhe610
Support Arthur| [![Ko-fi](https://ko-fi.com/img/Kofi_Logo_Blue.svg)](Ko-fi.com/arthurmilchior) or [![Patreon](http://www.milchior.fr/patreon.png)](https://www.patreon.com/bePatron?u=146206)
