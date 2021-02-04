import json
from difflib import get_close_matches

data = json.load(open("Dictionary/data.json"))

word = input("Enter word: ")
word = word.lower()

def translate(word):
    if word in data:
        return data[word]
    
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn =  input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys(), cutoff=0.8)[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys(), cutoff=0.8)[0]]
        elif (yn == "N"):
            return "The word doesn't Exist!!"
        else:
            return "We didn't understand the entry"
    else:
        return "The word doesn't Exist!!"

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

