def acronym():
    phrase = input("Insert the words for an acronym.")

    phrase_list = phrase.split()

    answer = ""
    for word in phrase_list:
        answer = answer + word[0]
    print(answer)


acronym()