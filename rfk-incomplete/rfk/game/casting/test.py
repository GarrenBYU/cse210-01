file = open('rfk-incomplete/rfk/data/messages.txt')
messages = [line.strip() for line in file]
print(messages)