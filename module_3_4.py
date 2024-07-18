def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in str(word).lower() or str(word).lower() in root_word.lower():
            same_words.append(word)
    return same_words


result01 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result02 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(f"{result01} \n{result02}")
