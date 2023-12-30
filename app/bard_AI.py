from bardapi import BardCookies
import json

def bard_AI(prompt):
    try:
        f = open('app/bard_cookie/.cookie.json')
    except:
        f = open('app/bard_cookie/cookie.json')

    cookie_dict = json.load(f)

    bard = BardCookies(cookie_dict=cookie_dict)
    return (bard.get_answer(prompt)['content'])