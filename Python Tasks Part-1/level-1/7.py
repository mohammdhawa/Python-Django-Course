def remove_word(sentence, word):
    return sentence.count(word)


sentence = "A room without books is like a body without a soul"

print(remove_word(sentence, "body"))
