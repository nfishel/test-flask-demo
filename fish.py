from datetime import datetime
import pytz

indytz = pytz.timezone("America/Indianapolis")
now = datetime.now(indytz)
print(now.month, "/",now.day,"/", now.year, sep="")
print(now.hour, ":",now.minute, ":", now.second, sep="")
print("-"*60)

print(now.strftime("%a, %b %-d, %Y - %-I:%M:%S"))
print(now.strftime("%c"), now.strftime("%x"), now.strftime("%X"), sep="\n")

input()

import string
from os import system
system("clear")



sentence = input("Enter a sentence:\n")

sen = ""

for x in string.punctuation:
  sentence = sentence.replace(x, "")

sentence = sentence.replace(" ", "")
letters = set()
for c in sentence:
  letters.add(c.lower())

  
l = len(sentence)

print(sentence, "has", l, "letters in it.")
print(sentence, "has", len(letters), "UNIQUE letters in it.")
print(letters)