import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data =  json.load(open('data.json'))

def get_definition(word):
    if not word:
        print('You have to tell me a word!')
        return False
    word = word.lower()
    word = word.strip()
    if word not in data:
        check_matches = get_close_matches(word, data.keys())[0]
        if len(check_matches) > 0:
            print(check_matches)
            new_word = data[check_matches]
            check_word = input('The word you chose is %s,  Press Y for yes and N for no: '   % check_matches)
            if check_word == 'Y':
                return new_word
            elif check_word == 'N':
                print('Fine then, try again')
                return False
            else:
                print('Figure out a real word!')
                return False
        else:
            print('Did you make that up?')
            return False
    keyword = data[word]
    return keyword
word = input('What word definition would you like? ')
word = word.lower()
word = word.strip()
output = get_definition(word)

for item in output:
    print(item)
