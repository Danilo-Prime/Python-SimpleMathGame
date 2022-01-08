from random import randint
def lin(x=30):
    print('='*x)
lin()
print('# ALERT: YOU CANNOT HAVE -10 NEGATIVE POINT. That means 10 errors without right answer.')
print('# The Level is the 10^Level. The size of the level is the power of 10.')
lin()
print('\n')
test = right = wrong = point = 0
level = int(input('Enter Level (0 as default): '))
lim = 100
while True:
    p = (10**(level+1))-1
    px = (p+1)*2
    a = randint(2, p)
    b = (randint(2, px)*5)/(p+1)
    solution = (a*b)
    answer = float(input(f"Level {level}, test: ({test}/{lim}) | Point: {point}\n{a} x {b} = "))
    if answer == solution:
        right += 1
        point += 1
        print('[✅] Right!')
    else:
        wrong += 1
        point -= 1
        print('[❎] Wrong!')
    print(f'Answer: {solution}')
    test += 1
    if test > lim:
        if point > lim*0.66:
            level += 1
            test = 0
            print(f'[🏆] 🎈 Congratulations! 🎉 - You have been upgrade of level.\n |LEVEL {level} |')
        else:
            print('Level Over! - Restarting Level')
            test = 0
        
    if point == -10:
        print('Low point!\nRegressing Level')
        level -= 1
        test = 0
    if level == -1:
        print('You need learn MATH FIRST! You loose in the first level. This is END GAME!')
        print('Game Over.')
        break
    print('')
        
