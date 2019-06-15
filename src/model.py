enhancedModel = {
    "vers": [],
    "name": "Enhanced Cloze 2.1",
    "tags": [],
    "did": 1511491712850,
    "usn": -1,
    "flds": [
        {"name": "# Content", "media": [], "sticky": False, "rtl": False, "ord": 0, "font": "Arial", "size": 17},
        {"name": "Note", "media": [], "sticky": False, "rtl": False, "ord": 1, "font": "Arial", "size": 17},
        {"name": "Source", "media": [], "sticky": False, "rtl": False, "ord": 2, "font": "Arial", "size": 17},
        {"name": "Extra", "media": [], "sticky": False, "rtl": False, "ord": 3, "font": "Arial", "size": 17},
        {"name": "In-use Clozes", "media": [], "sticky": False, "rtl": False, "ord": 4, "font": "Arial", "size": 16},
        {"name": "Cloze99", "media": [], "sticky": False, "rtl": False, "ord": 5, "font": "Arial", "size": 16},
        {"name": "Cloze1", "media": [], "sticky": False, "rtl": False, "ord": 6, "font": "Arial", "size": 16},
        {"name": "Cloze2", "media": [], "sticky": False, "rtl": False, "ord": 7, "font": "Arial", "size": 16},
        {"name": "Cloze3", "media": [], "sticky": False, "rtl": False, "ord": 8, "font": "Arial", "size": 16},
        {"name": "Cloze4", "media": [], "sticky": False, "rtl": False, "ord": 9, "font": "\u65b9\u6b63\u5170\u4ead\u9ed1\u7b80\u4f53", "size": 16},
        {"name": "Cloze5", "media": [], "sticky": False, "rtl": False, "ord": 10, "font": "Arial", "size": 16},
        {"name": "Cloze6", "media": [], "sticky": False, "rtl": False, "ord": 11, "font": "Arial", "size": 16},
        {"name": "Cloze7", "media": [], "sticky": False, "rtl": False, "ord": 12, "font": "Arial", "size": 16},
        {"name": "Cloze8", "media": [], "sticky": False, "rtl": False, "ord": 13, "font": "Arial", "size": 16},
        {"name": "Cloze9", "media": [], "sticky": False, "rtl": False, "ord": 14, "font": "Arial", "size": 16},
        {"name": "Cloze10", "media": [], "sticky": False, "rtl": False, "ord": 15, "font": "Arial", "size": 16},
        {"name": "Cloze11", "media": [], "sticky": False, "rtl": False, "ord": 16, "font": "Arial", "size": 16},
        {"name": "Cloze12", "media": [], "sticky": False, "rtl": False, "ord": 17, "font": "Arial", "size": 16},
        {"name": "Cloze13", "media": [], "sticky": False, "rtl": False, "ord": 18, "font": "Arial", "size": 16},
        {"name": "Cloze14", "media": [], "sticky": False, "rtl": False, "ord": 19, "font": "Arial", "size": 16},
        {"name": "Cloze15", "media": [], "sticky": False, "rtl": False, "ord": 20, "font": "Arial", "size": 16},
        {"name": "Cloze16", "media": [], "sticky": False, "rtl": False, "ord": 21, "font": "Arial", "size": 16},
        {"name": "Cloze17", "media": [], "sticky": False, "rtl": False, "ord": 22, "font": "Arial", "size": 16},
        {"name": "Cloze18", "media": [], "sticky": False, "rtl": False, "ord": 23, "font": "Arial", "size": 16},
        {"name": "Cloze19", "media": [], "sticky": False, "rtl": False, "ord": 24, "font": "Arial", "size": 16},
        {"name": "Cloze20", "media": [], "sticky": False, "rtl": False, "ord": 25, "font": "Arial", "size": 16}],
    "sortf":0,
    "tmpls":[
    {
        "name": "Cloze",
        "qfmt": """<div id="card-body">
    <div id="main-section" class="content">
    <!-- Separation line -->
    {{cloze:Cloze1}}
    <!-- Separation line -->
    {{cloze:Cloze2}}
    <!-- Separation line -->
    {{cloze:Cloze3}}
    <!-- Separation line -->
    {{cloze:Cloze4}}
    <!-- Separation line -->
    {{cloze:Cloze5}}
    <!-- Separation line -->
    {{cloze:Cloze6}}
    <!-- Separation line -->
    {{cloze:Cloze7}}
    <!-- Separation line -->
    {{cloze:Cloze8}}
    <!-- Separation line -->
    {{cloze:Cloze9}}
    <!-- Separation line -->
    {{cloze:Cloze10}}
    <!-- Separation line -->
        {{cloze:Cloze11}}
        <!-- Separation line -->
        {{cloze:Cloze12}}
        <!-- Separation line -->
        {{cloze:Cloze13}}
        <!-- Separation line -->
        {{cloze:Cloze14}}
        <!-- Separation line -->
        {{cloze:Cloze15}}
        <!-- Separation line -->
        {{cloze:Cloze16}}
        <!-- Separation line -->
        {{cloze:Cloze17}}
        <!-- Separation line -->
        {{cloze:Cloze18}}
        <!-- Separation line -->
        {{cloze:Cloze19}}
        <!-- Separation line -->
        {{cloze:Cloze20}}
    </div>
    <br>

    <!-- Separation line -->
    {{#Note}}
    <div id="note-section">
        <div id="note-header" class="header header-red" onclick="showNextElement(this)">
            Note
        </div>
        <div id="note" class="content" style="display:none">
            {{Note}}
        </div>
    </div>
    <br> {{/Note}}

    <div id="info-section">
        <div id="info-header" class="header header-blue" onclick="showNextElement(this)">
            Information
        </div>

        <div id="info" class="content" style="display:none">
            <div>
                Deck: {{Deck}}
            </div>

            <!-- Separation line -->
            {{#Tags}}
            <div id="tags">
                Tags: {{Tags}}
            </div>
            {{/Tags}}
        </div>
    </div>
    <br>

    <!-- Separation line -->
    {{#Source}}
    <div id="source-section">
        <div id="source-header" class="header header-green" onclick="showNextElement(this)">
            Source
        </div>
        <div id="source" class="content" style="display:none">
            {{Source}}
        </div>
    </div>
    <br> {{/Source}}

    <!-- Separation line -->
    {{#Extra}}
    <div id="extra-section">
        <div id="extra-header" class="header header-yellow" onclick="showNextElement(this)">
            Extra
        </div>
        <div id="extra" class="content" style="display:none">
            {{Extra}}
        </div>
    </div>
    <br> {{/Extra}}

    <div id="functional-elements">
        <div id="show-one-cloze-left"></div>
        <div id="show-one-cloze-right"></div>
        <div id="no-more-cloze"></div>
        <div id="show-all-pseudo-clozes"></div>
        <div style="display:none">
            {{type:In-use Clozes}}
        </div>
    </div>
</div>

<script src="_jquery-3.2.1.min.js"></script>
<script src="_jquery.hotkeys.js"></script>
<script src="_jquery.visible.min.js"></script>

<script>
    var indexOfGenuineClozeToShow = 0;
    var genuineClozeTotalNumber = $('.genuine-cloze').length;
    $(function () {
        // INITIALIZE CLOZES
        //      genuine clozes refer to those belong to current card and need to be answered, e.g. {{c2::abc}} on card2
        //      pseudo clozes refer to the opposite, e.g. {{c1::abc}} and {{c3::abc}} on card2
        $('.genuine-cloze, .pseudo-cloze').each(function (index, elem) {
            toggleCloze(elem, 'hint')
        });

        // SHORTEN TAGS
        //      leaving only the last part if hierarchical tags are used, i.e. tag1::tag2::tag3 -> tag3
        // $('#tags').each(function (index, elem) {
        //     $(elem).text($(elem).text().replace(/[^:\\s]+::/g, ''));
        // });

        // SCROLL TO FIRST CLOZE
        if (genuineClozeTotalNumber) {
            scrollToCloze($('.genuine-cloze').first().get(0));
        }

        $(document).keyup(function (event) {
            if (event.which == 73 || event.which == 105){//i
                showOneCloze();
            }
            if (event.which == 188){ //,
                showAllPseudoClozes();
            }
        })

        // SETUP CLOZE CLICK EVENT
        $('.genuine-cloze, .pseudo-cloze').click(function () {
            toggleCloze(this, 'toggle');
        });

        $('#show-one-cloze-left, #show-one-cloze-right').click(function () {
            showOneCloze();
        });

        $('#show-all-pseudo-clozes').click(function () {
            showAllPseudoClozes();
        })

    });

    function scrollToCloze(elem) {
        $('html, body').animate({
            scrollTop: $(elem).offset().top - 60
        }, 500);
    }

    function showOneCloze() {
        //alert("indexOfGenuineClozeToShow is "+indexOfGenuineClozeToShow+" while genuineClozeTotalNumber is "+genuineClozeTotalNumber );
        if (indexOfGenuineClozeToShow >= genuineClozeTotalNumber) {
            $('#no-more-cloze').animate({
                display: "toggle",
            }, 500);
        } else {
            //alert("Thus there remains genuine cloze");
            $('.genuine-cloze[index=' + indexOfGenuineClozeToShow + ']').each(function (index, elem) {
                //alert("We loop over index"+index);
                len = $(elem).parents('#note:hidden').length
                //alert("$(elem).parents('#note:hidden').length is "+len);
                if (len) {
                    //alert("Thus show");
                    $("#note").show(0);
                } else {
                    //alert("Thus don't show");
                    if (!$(elem).is(":visible")) {
                        //alert("Elem is not visible");
                        scrollToCloze(elem);
                    } else {
                        //alert("Elem is visible");
                        toggleCloze(elem, 'answer');
                        if (!$(elem).is(":visible")) {
                            //alert("Elem is not visible (second time)");
                            scrollToCloze(elem);
                        } else {
                            //alert("Elem is visible (second time)");
                        }
                        $(elem).hide(0);
                        $(elem).fadeIn(500);
                        indexOfGenuineClozeToShow++;
                    }
                }
            })
        }
        //alert("");
    }

    function showAllPseudoClozes() {
        $('.pseudo-cloze').each(function (index, elem) {
            toggleCloze(elem, 'answer');
        })
    }

    function toggleCloze(elem, displayOption) {
        var answer = '',
            hint = '';
        var index = $(elem).attr('index');
        if ($(elem).hasClass('genuine-cloze')) {
            answer = $('#genuine-cloze-answer-' + index).html();
            hint = $('#genuine-cloze-hint-' + index).html();
        } else {
            answer = $('#pseudo-cloze-answer-' + index).html();
            hint = $('#pseudo-cloze-hint-' + index).html();
        }
        hint = '&nbsp;&nbsp;[&nbsp;&nbsp;' + hint + '&nbsp;&nbsp;]&nbsp;&nbsp;';

        if (displayOption == 'answer') {
            $(elem).attr('show-state', 'answer');
            $(elem).html(answer);
        } else if (displayOption == 'hint') {
            $(elem).attr('show-state', 'hint');
            $(elem).html(hint);
        } else if (displayOption == 'toggle') {
            if ($(elem).attr('show-state') == 'hint') {
                $(elem).attr('show-state', 'answer');
                $(elem).html(answer);
            } else {
                $(elem).attr('show-state', 'hint');
                $(elem).html(hint);
            };
        };
    }

    function showNextElement(elem) {
        $(elem).next().show(0);
    };
</script>
""",
        "did": None,
        "bafmt": "",
        "afmt": """
{{FrontSide}}

<script>
    $(function () {
        $('#note').show(0)
        $('#info').show(0)
        $('#source').show(0)
        $('#extra').show(0)
        $('.genuine-cloze').each(function (index, elem) {
            toggleCloze(elem, 'answer')
        })
    })
</script>""",
        "ord": 0,
        "bqfmt": ""}],
    "mod": 1560146886,
    "latexPost": "\\end{document}",
    "type": 1,
    "id": 1510132306224,
    "css": """#card-body {
    font: 17px/1.5em 'Arial', 'Helvetica', sans-serif;
    margin-top: 60px;
    margin-bottom: 60px;
}

.content {
    padding-left: 0.5em;
    border-left: 4px solid transparent;
}

.header {
    font: bold 17px/1.5em;
    padding-left: 0.5em;
}

.header-red {
    border-left: 4px solid #db4437;
    color: #db4437;
}

.header-green {
    border-left: 4px solid #0f9d58;
    color: #0f9d58;
}

.header-blue {
    border-left: 4px solid #4285f4;
    color: #4285f4;
}

.header-yellow {
    border-left: 4px solid #f4b400;
    color: #f4b400;
}

.genuine-cloze {
    border-bottom: 1px solid #db4437;
    padding-bottom: 1px;
}

.genuine-cloze[show-state="hint"] {
    border-bottom: 2px solid #db4437;
    background-color: #ffd6d4;
}

.pseudo-cloze {
    border-bottom: 1px solid #4285f4;
    padding-bottom: 1px;
}

.pseudo-cloze[show-state="hint"] {
    border-bottom: 2px solid #4285f4;
    background-color: #dce8ff;
}

#show-one-cloze-left,
#show-one-cloze-right,
#no-more-cloze {
    height: 100%;
    width: 30px;
    position: fixed;
    z-index: 9;
    top: 0;
    background-color: transparent;
}

#show-one-cloze-left {
    left: 0;
}

#show-one-cloze-right {
    right: 0;
}

#no-more-cloze {
    width: 10px;
    background-color: #db4437;
    left: 0;
    display: none;
}

#show-all-pseudo-clozes {
    height: 20px;
    width: 100%;
    position: fixed;
    z-index: 9;
    top: 0;
    left: 0;
    background-color: transparent;
}

i {
    padding-right: 0.5em;
}

u {
    background-color: #dbffed;
    border-bottom: 2px solid #0f9d58;
    text-decoration: none;
}

a {
    color: #444444;
    word-wrap: break-word;
}

.mobile ol,
.mobile ul,
.mobile li {
    margin-left: -0.5em;
}

.mobile li {
    margin: 0.1em, inherit;
}

table {
    border-collapse: collapse;
    margin: 0.5em;
}

thead tr,
tfoot tr {
    border-top: 2px solid #0f9d58;
    border-bottom: 2px solid #0f9d58;
}

td,
th {
    border: 1px solid #0f9d58;
    padding: 0.3em 0.5em;
}

hr {
    border-top: 2px solid #aaaaaa;
    width: 100%;
    margin: 0;
    padding: 0;
}

pre {
    border-left: 2px solid #0f9d58;
    padding-left: 10px;
}

code,
kbd,
var,
samp,
tt {
    background-color: #fdf3d6;
}""",
 "latexPre": """\\documentclass[12pt]{article}
\\special{papersize=3in,5in}
\\usepackage[utf8]{inputenc}
\\usepackage{amssymb,amsmath}
\\pagestyle{empty}
\\setlength{\\parindent}{0in}
\\begin{document}
"""}
