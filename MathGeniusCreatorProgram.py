from random import randint
import os
def lin(x=60):
    print('='*x)
lines = '-'*50
lin()
print('# This programm is to Mental Math, not paper math. Do not write anything!\n# You can manipulate final result, is the only place you can modify is the result')
print('# ALERT: YOU CANNOT HAVE -10 NEGATIVE POINT. That means 10 errors without right answer.')
print('# The Level is the 10^Level. The size of the level is the power of 10.')
print('# Only two wrong. But the point will value less as penauty and the wrong point will mutiply as a game, or you lose or win less if you repeat mistakens...')
print("# Memory can't be anything different from int number or over 100. The game is flexible but everything have the down side or punity. More easy less repetition option. More hard more repetition option.")
lin()
print('\n')
test = right = wrong = point = 0
try:
    level = int(input('Enter Level (0 as default): '))
except:
    level = 0

try:
    memory = int(input('Do you can memorized how many test? (3 default | over 10 if you can!) '))
    if type(memory) != int or memory > 100:
        memory = 1
except:
    print('[Inválid] - Assuming 1 test!')
    memory = 1
lim = 100
while True:
    lista = []
    listc = []
    listSolutions = []
    listAnswers = []
    print(f"Level {level} | Point: {point} Wrong: {wrong}\n{lines}\n")
    for i in range(memory):
        p1 = (10**(level))+8
        p2 = (10**(level+1))-1
        px = (p2+1)*2
        a = randint(2, p1)
        b = (randint(2, px)*5)/(p2+1)
        c = randint(2, p2)
        d = (randint(2, px)*5)/(p2+1)
        # main
        solution = (a*c)
        lista.append(a)
        listc.append(c)
        listSolutions.append(solution)
        listAnswers.append(0)
        print(f"({test}/{lim})\t| Test [{i}] = ({a-b: ^6.4g} + {b: ^6.4g}){'x': ^6.4}({c+d: ^6.4g} - {d:^6.4g})")
        # final
        test += 1
    # Question:
    #================================
    ask = input('\nSOLVED and Memorized?\n[ANY BUTTON TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear') 
    # this will garante that there have solve the problem without notating. To that, he need memorized the solution.
    lin()
    print('[TEST START!]')
    round = 0
    roundLimit = memory
    while round < roundLimit:
        if round != 0:
            print(f'\n{lines}\nMore {roundLimit-1} times [{round}/{roundLimit-1}]:\n{lines}\n')
            point
        for i in range(memory):
            try:
                answer = float(input(f"Test [{i}] = "))
            except:
                print('[INVALID ANSWER] - ONLY NUMBERS!')
                answer = 0
            listAnswers[i] = answer
        # Scan ListSolutions vs AnswersList 
        if listAnswers == listSolutions: # change by scan: True or False
            right += (1/(round+1))*memory
            point += (1/(round+1))*memory
            print(f'[✅] Right! (+{1/(round+1)} point)\n')
            break
        else:
            wrong += ((round+1))*memory
            point -= ((round+1))*memory
            print(f'[❎] Wrong! (-{1*(round+1)} point)')
            round += 1
        if round < roundLimit:
            ask = input('Do you whant to repeat? (only if you remeber the answer!) [y/n] ')[0].lower()
            if ask == 'n':
                break
    if round == {roundLimit}:
        print('YOU LOSE YOU CHANCE!')
    print(f'Answer:\n')
    for i in range(memory):
        print(f"Test [{i}] =\t({lista[i]:^6.4g}{'x':^6.4}{listc[i]:^6.4g})\t= {listSolutions[i]:>6.4g} | You number: {listAnswers[i]:>6.4g}")
    print('='*50)
    ask = input('\n[ANY BUTTON TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear')
    #================================================
    if test > lim:
        res = str(input('Chose the level? [S/N] '))[0].lower()
        if res == 's':
            try:
                level = int(input('Enter Level (0 as default): '))
            except:
                level = 0
        else:
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
        
