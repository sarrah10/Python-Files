#read mode
f = open("story.txt","r")
data = f.read(7)
print(data) 

data1 = f.readline()  #will read line till \n
print(data1)

data2 = f.readlines()  #will show whole lines with \n
print(data2)
f.close()

#if opening file with "with" automatically file will be closed after executing
with open("story.txt","r") as f:  
    print(f.read(5))
    print(f.read(7))

f = open("jokes.txt","r") #will read file line by line
for line in f:
    print(line)

# Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the"
def readword():
    with open("friends.txt","r") as f: 
        count = 0
        data = f.readlines() 
        for i in data:
            for words in i.split():
                if(words =='the' or words =='The'):
                    count += 1
        print("the in file notes.txt is :",count, "times") 
readword()

# Write a function in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters
def readwors():
    with open("story.txt","r")as f: 
        data=f.readlines()
        for i in data:
            for words in i.split(): 
                if(len(words)<=4):
                    print(words)
readwors()

