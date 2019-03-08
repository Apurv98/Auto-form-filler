import mechanize
import random

allowed_chars='abcdefghijklmnopqrstuvwxyz'

def randomstring(allowed_chars,len):
    return ''.join(random.choice(allowed_chars) for i in range(len))

br = mechanize.Browser()
br.set_handle_robots(False)
br.open("http://127.0.0.1:8000/")
n = 0
while n<=50:
    br.select_form(nr=0)
    br['name'] = randomstring(allowed_chars,6)
    br['department'] = randomstring(allowed_chars,10)
    br.submit()
    n+=1
