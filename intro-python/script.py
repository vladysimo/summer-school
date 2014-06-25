#first piece of code

import sys

name = sys.argv[1]

def repeat(s, exclaim=True):
    result = s * 3
    if exclaim:
         result += "!!!"
    return result

if name == "Vlad":
    print "Salut", name, "ai acces"
else:
    print repeat("Nu", 1)
