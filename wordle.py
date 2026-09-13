file = open("words.txt", "r")
content = file.read()
file.close()

def get_words(n):
    words = content.splitlines()
    return [word for word in words if len(word) == n and word.isalpha()]

