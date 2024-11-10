def add_excitement(strings):
    for i in range(len(strings)):
        strings[i] +='!'
    return strings


word = ["hellow", "sourav", "python"]
add_excitement(word)
new_word = add_excitement(word)
print(word)
print(new_word)
