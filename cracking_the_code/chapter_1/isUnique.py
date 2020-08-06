def has_all_unique(string):
    letters_seen = set()
    for char in string:
        if char in letters_seen:
            return False
        letters_seen.add(char)
    return True

print(has_all_unique("hola"))
