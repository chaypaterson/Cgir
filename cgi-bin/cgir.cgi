#!/usr/bin/python
# -*- coding: utf-8 -*- 

import sys,cgi

def hello():
    print("Hello!\n")

# CSS from txti.es
txticss = ("html{-webkit-text-size-adjust:100%;padding-bottom:4em}"+
"body{font-family:sans-serif;line-height:1.5em;max-width:40em;padding:0"+
"2%;margin:auto}.text-input{width:96%;display:block;padding:.5em"+
"1%;margin-bottom:1.5em;font-size:1em}fieldset{margin-bottom:1.5em}"+
"textarea{height:10em}dt{font-weight:bold}.important{color:red}."+
"footer{text-align:right}.centered{text-align:center}.nope{display:none}"+
".ad-container{float:left;min-width:33%}")

def htmlify(txt):
    # escape special characters
    htmlcodes = {
        "\'" : "\\\'",
        "\"" : "\\\"",
        "‘" : "&lsquo;",
        "’" : "&rsquo;",
        "—" : "&mdash;",
        "–" : "&mdash;"
    }

    for key in htmlcodes:
        txt = txt.replace(key,htmlcodes[key])

    return txt

def readfile(txtfile, start):
    ps = []
    lines = 45 # read 45 lines
    # at 61 characters a line and 1 byte per char:
    bytes = 2745 # read this many bytes per page

    # read file from line "start" to line "start+n"
    if txtfile != "":
        doc = open(txtfile,"r")
        doc.seek(start*bytes,0)
        txt = doc.read(bytes)
        # deal with special characters in txt:
        txt = htmlify(txt)
        doc.close()

    # break into a list of paragraphs
    ps = txt.split("\n\n")
    # deal with special characters?

    # return the list of paragraphs
    return ps

def returnpage(ps, start, end):
    # print a formatted webpage to stdout
    title = "Page "+str(start+1)+"/"+str(end)

    # this should have ~61 characters per line
    # 390 wpp: 7 characters/wd: ~2730 charpp
    # 2730/61 = 45 lines.

    print("Content-type: text/html\n\n")
    print("<html><head>")
    # print title
    print("<title>"+title+"</title>")
    # add stylesheet:
    print("<style>\n"+txticss+"</style>")
    print("</head>")
    # begin body:
    print("<body>")

    for pp in ps:
        txtline="<p>"+str(pp)+"</p>"
        print(txtline.encode('utf-8'))

    # make a note of position in text:
    prevpg = start-1
    nextpg = start+1

    # print navigation bar
    if (start > 0):
        print("<a href=\"./cgir.cgi?arg1=%s\">Back</a>" % prevpg)

    if (start < end):
        print("<a href=\"./cgir.cgi?arg1=%s\">Next</a>" % nextpg)

    print("</body>")
    print("</html>")

def howlong(textfile):
    doc = open(textfile, "r")
    length = len(doc.read())/2745
    doc.close()

    return length

#-----------
# main routine:

def main():
    # which story to read:
    txtfile = "./cgi-bin/curious.txt"
    # get length of story (in pages):
    end = howlong(txtfile)

    # Get page to read from:
    # from argv:
    if (len(sys.argv)>1):
        start = int(sys.argv[1]) # opening page
    else:
        start = 0

    # argv is good for testing but not 100% compatible with cgi
    form = cgi.FieldStorage()
    if 'arg1' not in form:
        start = 0
    else:
        start = int(form['arg1'].value)

    if start > end:
        start = 0

    # read text page from file
    ps = readfile(txtfile, start)
    # format web page
    returnpage(ps, start, end)

main()
