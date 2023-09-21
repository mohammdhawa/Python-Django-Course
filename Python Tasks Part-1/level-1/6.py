def remove_word(sentence, word):
    sentence = sentence.split(' ')
    while word in sentence:
        sentence.remove(word)
    return ' '.join(sentence)

sentence = "A room without books is like a body without a soul"
print(remove_word(sentence, "room"))
