import re


# match : match = re.match(pat, str)
# search : match = re.search(pat, str)
# findall : Finds all the matches and returns them as a list of strings

# match = re.findall(pat, str)
str = 'How ?s How ry the weather today?'

match = re.match(r'How \W', str)

print(match)
if match:
    print('String found : {}'.format(match.group()))
else:
    print('No Match')

# repetition example

match = re.search(r're+', 'rees') # 'r' followed by 1 or more 'e's
if match is not None:
    print(match.group()) # prints ree

match = re.search(r're+s*', 'rees') # 'r' followed by 1 or more 'e's and 0 or more occurrences of 's'
if match is not None:
    print(match.group()) # prints rees

match = re.search(r're+s*', 'reeses') # 'r' followed by 1 or more 'e's and 0 or more occurrences of 's'
if match is not None:
    print(match.group()) # prints rees

match = re.search(r'^be*', 'bees') # Stats with character 'b' and followed by 0 or more occurrences of 'e'
if match is not None:
    print(match.group())


email = 'john.reid@company.com' # very basic email id validation

match = re.search(r'[\w.-]+@[\w-]+\.\w+', email)
if match is None:
    print('{} is {}'.format(email,'bad email id'))
else:
    print('{} is {}'.format(email, 'good email id'))

# explaining group
match = re.search(r'([\w.-]+)@([\w-]+\.\w+)', email) # grouping blocks are enclosed inside the parenthesis().
if match is not None:
    print("Full match string: ", match.group())
    print("First block match: ", match.group(1))
    print("Second block match: ",match.group(2))



# find all example

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

emails = re.findall(r'[\w\.-]+@[\w-]+\.\w+', str) ## ['alice@google.com', 'bob@abc.com']
if emails is not None:
    for email in emails:
        print(email)


emails = re.findall(r'([\w.-]+)@([\w-]+\.\w+)', str) ## ['alice@google.com', 'bob@abc.com']
if emails is not None:
    print(emails)


# some more examples

regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    match = re.search(regex, "June 24")
    # to know the start and end position of the found string
    print("Match at index %s, %s" % (match.start(), match.end()))


# sub example
regex = r"([a-zA-Z]+) (\d+)"
# interchanging the first and second match with 'of' inbetween
print(re.sub(regex, r"\2 of \1", "June 24, August 9, Dec 12"))

# using compile method
regex = re.compile(r"(\w+) World")
result = regex.search("Hello World basic example")

if result:
    print(result.group())

# findall method
for result in regex.findall("Hello World, Bonjour World"):
    print(result)

# sub example
print(regex.sub(r"\1 Earth", "Hello World"))