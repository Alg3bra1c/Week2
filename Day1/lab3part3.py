phrase = "Do Re Me Fa So La Ti Do"
phraseList = phrase.split()
# note that  phraseList is equal to ['Do', 'Re', 'Me', 'Fa', 'So', 'La', 'Ti', 'Do']
answer = ""
for word in phraseList:
    if word[1] != 'a':
        answer = answer + word
print(answer)