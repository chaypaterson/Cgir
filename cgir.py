#!/bin/python

import sys

def hello():
    print("Hello!\n")

# CSS from txti.es
txticss = ("html{-webkit-text-size-adjust:100%;padding-bottom:4em}"+
"body{font-family:sans-serif;line-height:1.5em;max-width:40em;padding:0"+
"2%;margin:auto}.text-input{width:96%;display:block;padding:.5em"+
"1%;margin-bottom:1.5em;font-size:1em}fieldset{margin-bottom:1.5em}textarea{height:10em}dt{font-weight:bold}.important{color:red}.footer{text-align:right}.centered{text-align:center}.nope{display:none}.ad-container{float:left;min-width:33%}")

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
        doc.close()

    # break into a list of paragraphs
    ps = txt.split("\n\n")

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
        print("<p>"+str(pp)+"</p>")

    # make a note of position in text:
    prevpg = start-1
    nextpg = start+1

    # print navigation bar
    if (start > 0):
        print("<a href=\"./cgir.py?arg1=%s\">Back</a>" % prevpg)

    print("<p>%s/%s</p>" % (start, end) )

    if (start < end):
        print("<a href=\"./cgir.py?arg1=%s\">Next</a>" % nextpg)

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
    foo = "curious.txt"
    # get length of story (in pages):
    end = howlong(foo)

    # Get position to read from:
    if (len(sys.argv)>1):
        start = int(sys.argv[1]) # opening page
    else:
        start = 0

    start = start % end # just in case of malformed/malicious output

    # read text page from file
    ps = readfile(foo, start)
    # format web page
    returnpage(ps, start, end)

main()
