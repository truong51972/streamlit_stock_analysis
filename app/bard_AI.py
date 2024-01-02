from bardapi import BardCookies
from bardapi import Bard, max_token, max_sentence
import json

class bard_AI:
    def __init__(self) -> None:
        try:
            f = open('app/bard_cookie/.cookie.json')
        except:
            f = open('app/bard_cookie/cookie.json')
        cookie_dict = json.load(f)
        try:
            self.bard = BardCookies(cookie_dict=cookie_dict)
        except:
            print('Invalid cookies!')
            
    def getAnwser(self,prompt):
        response = self.bard.get_answer(prompt)['content']
        return (response)
    
    