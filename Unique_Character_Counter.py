# Write a program that asks the user to enter a long sentence. Convert the sentence into a Set
#  to find out exactly how
# many unique characters (letters, numbers, or symbols) were used in the sentence (ignore spaces
#  if possible). Print
# the set of unique characters and the total count.

sentence = input("enter a long sentence: ")
sentence_set = set(sentence)
print(sentence_set)
print(len(sentence_set))

