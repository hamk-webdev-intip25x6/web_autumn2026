d = {"dog": "koira", "cat": "kissa"}

while True:
    word = input("Enter a word to translate (or enter to quit): ")
    if not word:
        break
    if word in d:
        print(f"The translation of '{word}' is '{d[word]}'.")
    else:
        print(f"Sorry, the word '{word}' is not in the dictionary.")
        definition = input(f"Please provide a translation for '{word}': ")
        if definition:
            d[word] = definition
            print(f"Added '{word}': '{definition}' to the dictionary.")
