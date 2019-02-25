try:
    file = open('simple.txt', 'r')
    file.write("Sagar says hello")
except FileNotFoundError:
    print("File not found. Check the filename")
except IOError:
    print("Couldn't read data from the file")
else:
    file.close()
