import json
from difflib import SequenceMatcher
from difflib import get_close_matches

# load json data
data =  json.load(open('data.json'))

def get_definition(word):
    # check if word is empty
    if not word:
        print('You have to tell me a word!')
        return False
    # sanitize the word
    word = word.lower()
    word = word.strip()
    # word is not found in the dictionary
    if word not in data:
        # use difflib built-in get_close_matches function to see what's close at the first answer
        check_matches = get_close_matches(word, data.keys())[0]
        # if check matches returns a value greater than 0
        if len(check_matches) > 0:
            # set the new word
            new_word = data[check_matches]
            # check with user if the new word matches
            check_word = input('The word you chose is %s,  Press Y for yes and N for no: '   % check_matches)
            # TO DO: MAKE STRICT
            if check_word == 'Y':
                return new_word
            elif check_word == 'N':
                print('Fine then, try again')
                return None
            else:
                print('Figure out a real word!')
                return False
        else:
            print('Did you make that up?')
            return False
    # if everything is smooth just set it and return it
    keyword = data[word]
    return keyword

# Get the word to search for, send it to lower, strip it and pass it to get_definition
word = input('What word definition would you like? ')
word = word.lower()
word = word.strip()
# waits on the definition to be returned
output = get_definition(word)
# loops through the output and prints each definition on their own line out of the list
if output:
    for item in output:
        print(item)
else:
    False
