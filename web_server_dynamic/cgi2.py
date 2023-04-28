#!\Users\Lenovo\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\Python 3.10 (64-bit).lnk"

import cgi
content = '''<html><body>
    <h3>Name: {strname} </h3>
    <h3>Password: {strpwd} </h3>
    </body></html>'''

def main():
    form = cgi.FieldStorage()
    strname = form.getfirst("sname", "")
    strpwd = form.getfirst("pwd", "     ")
    print(content.format(**locals()))

try:
    main()
except:
    cgi.print_exception()



