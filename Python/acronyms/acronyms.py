"""To create acronyms using Python,  write a python
program that generates a short form of a word from a given sentence.
This can be done by splitting and indexing to get the first word and
then combine it.
"""



text = str(input("enter a phrase:"))
split_txt = text.split()
a = " "
for i in split_txt:
    a = a + str(i[0]).upper()
print(a)


""" first taking a string user input, then using the split() function in
Python for splitting the sentence.
Then declared a new variable ‘a’ to store the acronym of a phrase. At the end,
running a for loop over the variable ‘text’ which represents the
split of user input. While running the for loop we are storing the index value
of str[0] of every word after a split and turning it into an uppercase format by
using the upper() function.

"""
