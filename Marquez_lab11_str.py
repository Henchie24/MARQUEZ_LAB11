word_col = []

while len(word_col) < 10:
    word_input = (input("Enter a Word: "))
    
    if word_input == " ":
        print("Invalid!\nMust Enter a Word")
        continue

    elif word_input.isdigit():
        print("Invalid!\nNumbers are not allowed")
        continue

    elif " " in word_input:
        print("Invalid!\nEnter 1 word only")
        continue

    elif not word_input.isdigit():
        word_col.append(word_input)
        print("Word Accepted!")

mis_words = []
word_len = int(input("Enter word length: "))

for words in word_col:
    if len(words) == word_len:
        mis_words.append(words)
print(f"Entered Words with {word_len} letters:\n{mis_words}")
