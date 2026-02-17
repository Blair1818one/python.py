from os import strerror

try:
    counter = 0
    stream = open('text.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    