import random


def choose():
    words=['apple', 'orange', 'mango', 'guava', 'lichi', 'strawberry']
    word=random.choice(words)
    return word

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thanks(p1name,p2name,pp1,pp2):
    print(f'{p1name} your final score is {pp1}')
    print(f'{p2name} your final score is {pp2}')
    print('Thanks for playing')

def play():
    p1name=input("Enter player1 name: ")
    p2name=input("Enter player2 name: ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if(turn%2==0):
            ans=input(f'{p1name} : Enter your answer: ')
            if(ans==picked_word):
                pp1=pp1+1
                print(f'{p1name} your score is {pp1}')
            else:
                print("Better luck next time, I selected: ",picked_word)
                c=int(input("Enter 1 for continue and 0 for quit"))
                if(c==0):
                    thanks(p1name,p2name,pp1,pp2)
                    break
        else:
            ans=input(f'{p2name} : Enter your answer: ')
            if(ans==picked_word):
                pp2=pp2+1
                print(f'{p2name} your score is {pp2}')
            else:
                print("Better luck next time, I selected: ",picked_word)
                c=int(input("Enter 1 for continue and 0 for quit: "))
                if(c==0):
                    thanks(p1name,p2name,pp1,pp2)
                    break
        turn=turn+1                
play()