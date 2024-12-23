import sys

# Read english to list
english = open("src/swadesh/english_words.txt").read().split(sep='\n')

# Read words from input to list
target = sys.stdin.read().split(sep='\n')

for (english_word, target_word) in zip(english, target):
    print(f"{english_word}: {target_word}")