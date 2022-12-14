def charFreq(str):
    wordcount=dict()
    for letter in set(str):
        wordcount[letter]=str.count(letter)
    return wordcount
word = input("Enter a string to check for character frequency:")
print(charFreq(word))