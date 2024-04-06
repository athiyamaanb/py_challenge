


def get_common_chars(words):
    commons = list(words[0])

    for word in words[1:]:
        new = []
        for s in commons:
            if s in word:
                new.append(s)
                word = word.replace(s, '', 1)
        commons = new
    return commons

print(get_common_chars(["bella","label","roller"]))


print(get_common_chars(["cool","lock","cook"]))