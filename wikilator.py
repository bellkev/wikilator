#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
from xml.dom import minidom

# give some dummy test variables or take input from cgi
if __name__ == '__main__':
    source='en'
    target='ja'
    text='apple'
else:
    import cgitb
    cgitb.enable()
    form=cgi.FieldStorage()
    source=form["source"].value
    target=form["target"].value
    text=form["text"].value

# perform inital search based on form input
def search(source, text, searchResultLimit=10):
    searchUrl ="http://{0}.wikipedia.org/w/api.php?action=query\
&list=search&srsearch={1}&srlimit={2}&format=xml".format(source,text,searchResultLimit)
    u=urllib.urlopen(searchUrl)
    x=minidom.parse(u)
    u.close()
    pList=x.getElementsByTagName("p")
    results=[p.attributes["title"].value, p.attributes["snippet"].value for p in pList]
    return results

#HTML output
code = 'utf-8' # make it easy to switch the codec later
html = 'Content-type:text/html\r\n\r\n'
html+='<html>'

# use a <meta> tag to specify the document encoding used
html += '<meta http-equiv="content-type" content="text/html; charset=%s">' % code
html += '<head></head><body>'

# actual Unicode content ...
html += search(source, text)
html += u'</body></html>'
#open('t.html','w').write( html.encode( code ) )
print html
#if __name__ == '__main__'


