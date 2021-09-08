import sys
n = int(input())
wordList = list()
for _ in range(n):
    word = input()
    if word not in wordList:
        wordList.append(word)
wordList.sort(key=lambda x: (len(x), x))
for i in range(len(wordList)):
    print(wordList[i])