'''
this program is used to split a sentence
join it together, capitalizing the 1st letter of each word
and putting the words together and adding a hashtag at the beginning
'''
s = str(input("Enter a sentence: "))

result = '#'+''.join(elem.capitalize() for elem in s.split())


# .split() splits a sentence into elements in a list.
print(s.split(" "))

# .title() capitalize every word in the sentence.
print(s.title())

# .capitalize() Converts the first character to upper case.
# .join() puts together all split words.


print(result)