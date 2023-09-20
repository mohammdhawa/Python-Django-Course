def remove_duplicated_word(sentence):
    sentence = sentence.split(' ')
    words = []
    for word in sentence:
        if word in words:
            continue
        else:
            words.append(word)

    print(f"The sentence after removing duplicated words: {' '.join(words)}")


sentence = "hello world, hello I'm Muhammad, hello guys, world."

remove_duplicated_word(sentence)