from random import randint
def lin(x=30):
    print('='*x)
lin()
print("""# ALERT: YOU CANNOT HAVE -10 NEGATIVE POINT. That means 10 errors without right answer.
# The Level is the 10^Level. The size of the level is the power of 10.
# Limit of 4 digit of decimals.
""")
lin()
print('\n')
test = right = wrong = point = 0
level = int(input('Enter Level (0 as default): '))
lim = 1000
while True:
    p = (10**(level+1))-1
    px = (10**(level+2))-1
    a = randint(2, p)/100
    b = (randint(2, px))/(p+1)
    if b == 1:
        b += (randint(2, px))/(p+1)
    solution = (((a*1000)*(b*1000))/10**6) # treat the solution | Memory erro that make a bug of ...9999999... The solution have been put all in interger.
    answer = float(input(f"Level {level}, test: ({test}/{lim}) | Point: {point}\n{a} x {b} = "))
    if answer == solution:
        right += 1
        point += 1
        print('[✅] Right!')
    else:
        wrong += 1
        point -= 1
        print('[❎] Wrong!')
    print(f'Answer {a} x {b}: {solution}')
    test += 1
    if test > lim:
        if point > lim*0.66:
            level += 1
            test = 0
            point = 0
            print(f'[🏆] 🎈 Congratulations! 🎉 - You have been upgrade of level.\n |LEVEL {level} |')
        else:
            print('Level Over! - Restarting Level')
            test = 0
            point = 0
        
    if point == -10:
        print('Low point!\nRegressing Level')
        level -= 1
        test = 0
    if level == -1:
        print('You need learn MATH FIRST! You loose in the first level. This is END GAME!')
        print('Game Over.')
        break
    print('')
        
