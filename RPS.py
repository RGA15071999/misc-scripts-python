from random import randint
a = ['rock', 'paper', 'scissors']
b = randint(0, 2)
countcpu = 0
countpl1 = 0
inp = raw_input('Rock, paper or scissors. Write q to exit ')
while True:
    if inp == 'q':
        break
    if a[b] == inp:
        print 'Draw'
    elif inp == 'rock' and a[b] == 'scissors':
        print 'You win'
        countpl1 += 1
        if countpl1 == 3 or countcpu == 3:
            print 'Game Over'
            break
    elif inp == 'rock' and a[b] == 'paper':
        print 'You lose'
        countcpu += 1
        if countpl1 == 3 or countcpu == 3:
            print 'Game Over'
            break
    elif inp == 'paper' and a[b] == 'rock':
        print 'You win'
        countpl1 += 1
        if countpl1 == 3 or countcpu == 3:
            print 'Game Over'
            break
    elif inp == 'paper' and a[b] == 'scissors':
        print 'You lose'
        countcpu += 1
        if countpl1 == 3 or countcpu == 3:
            print 'Game Over'
            break
    elif inp == 'scissors' and a[b] == 'paper':
        print 'You win'
        countpl1 += 1
        if countpl1 == 3 or countcpu == 3:
            print 'Game Over'
            break
    elif inp == 'scissors' and a[b] == 'rock':
        print 'You lose'
        countcpu += 1
        if countpl1 == 3 or countcpu == 3:
            print 'Game Over'
            break
    else:
        print 'Careful write only rock paper or scissors'
    print "Cpu ", countcpu, " : ", countpl1, " Pl1"
    b = randint(0, 2)
    inp = raw_input('Input another or print q to exit ')
print 'Bye'
