import mysql.connector
import json
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter word: ")
word = word.lower()


def translate(word):
    query = cursor.execute(
        "SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if results:
        for result in results:
            print(result[1])
        
    # elif len(get_close_matches(word,results,cutoff=0.8)) > 0:
    #     yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, results[0], cutoff=0.8)[0])
    else:
        print(get_close_matches(word, [item[0] for item in results], cutoff=0.8))
        return "The word doesn't exists!!"
    

translate(word)
