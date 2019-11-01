# CGI READER
-----------

This is a CGI script/simple web framework that prints pages in a directory (or
a text file, page by page), with some formatting options.

The Python script at cgi-bin/cgir.cgi should:

    * read a text file
    * select a few lines of the file
    * print a html page containing those lines, and some forward and
    back buttons.

That's it.

---

How to run:

    * Place a text file in the cgi-bin/ directory.
    * Change the "txtfile" variable in cgi-bin/cgir.cgi to point to the target
      file.
    * Start the script with "python -m CGIHTTPServer"
