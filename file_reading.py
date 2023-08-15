#wap to count no. of lines in a file
with open("file.txt","r") as f:
    data = f.readlines()
    print(len(data))

#wap to read file using readline funtion
with open("file.txt","r") as f:
    while True:
        line = f.readline()
        if(line==""):
            break
        else:
            print(line)

#wap to count no. of words in a file
count = 0
with open("file.txt","r") as f:
    while True:
        line = f.readline()
        if(line==""):
            break
        else:
            t = line.split()  #split() works on string
            count = count + len(t)
print(count)   

#wap to find no. of characters
with open("file.txt","r") as f:
    data = f.read()
    print(len(data))