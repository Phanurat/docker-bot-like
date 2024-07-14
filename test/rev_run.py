#bot input 

#bot_id = 'number_bot'

class cookies_info:
    def __init__(self, c_user, xs, datr, fr):
        self.c_user = c_user
        self.xs = xs
        self.datr = datr
        self.fr = fr

api_c_user = "61551780956965"
api_xs = "19%3AzAyL2YXiSh_4pw%3A2%3A1720775422%3A-1%3A-1%3A%3AAcX8dWSh9hhQXE9r7LXydcOkUSgC-IZu0AKSgQMl2w"
api_datr = "__GMZCgwVF5BbyvAtfJojQwg"
api_fr = "01ahWiYH59lE402S7.AWUJZwbYhWORRKMgcOPaiRJPPOw.BmkPL9..AAA.0.0.BmkPMA.AWXw2wuhccw"

cookies = cookies_info(api_c_user, api_xs, api_datr, api_fr)

print("c_user:", cookies.c_user)
print("xs:", cookies.xs)
print("datr:", cookies.datr)
print("fr:", cookies.fr)

def myfunc():
    global gl_user
    gl_user = "61551780956965"

myfunc()

print(gl_user)

def myfunc_test():
    print(gl_user)

myfunc_test()
