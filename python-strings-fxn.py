# len fxn
message = 'Hello World'
print(len(message))

# access characters in string
print(message[1], message[2])

# Slicing --> print Range of message -> print character at startIndex till endIndex-1
print(message[0:5])
print(message[:5])
print(message[6:])

# Lowercase / uppercase --> immutable
print(message.lower())
print(message.upper())

print(message)

# Count character / word
print(message.count("Hello"))
print(message.count('Hello'))
print(message.count('l'))
print(message.count("l"))

# Find character/word --> returns index
print(message.find('hello'))
print(message.find('World'))
print(message.find("World"))

# Replace --> immutable
print(message.replace('World', 'Universe'))
print(message)

# Concat using +
greeting = 'Hello'
name = 'Neelansh'

newMessage = greeting + ', ' + name
print(newMessage)

# Concat using format fxn & placeholders --> better than +
placeholder = '{}, {}. Welcome!'
formattedMessage = placeholder.format(greeting, name)
print(formattedMessage)


# fstrings --> new in python 3 --> make formatting of strings simpler
fmessage = f'{greeting}, {name}. Welcome!'
print(fmessage)

fmessage = f'{greeting}, {name.upper()}. Welcome!'
print(fmessage)

fmessage = f'{greeting.lower()}, {name.upper()}. Welcome!'
print(fmessage)


# dir fxn --> shows attributes and methods/fxns
print(dir(fmessage))

# help fxn --> show documentation --> works with types only
# print(help(str))
print(help(str.lower))
