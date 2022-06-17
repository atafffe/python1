introstring = input("Enter introduction: ")
characterCount = 0
wordCount = 1

for character in introstring:
    characterCount = characterCount + 1
    if(character==' '):
        wordCount = wordCount + 1
print("Number of words in the string: ")
print(wordCount)
print("Number of characters: ")
print(characterCount)