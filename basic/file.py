with open("testfile.txt", mode='w') as f:
    f.write("This files has some text\nanything can be added later")

with open("testfile.txt", mode='r') as f:
    print(f.read())

with open("testfile.txt", mode='a') as f:
    f.write("\nadding new line using append with file mode")

with open("testfile.txt", mode='r') as f:
    print(f.read())