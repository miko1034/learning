# repr(x) surrounds x with '' e.g if x is "test" then repr(x) would output "'test'"

def hashing(key):
    return sum(ord(letters) for letters in repr(key))

print(hashing("john123"))
print(hashing("tests"))
