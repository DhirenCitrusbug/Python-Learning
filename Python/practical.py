from enum import Flag
import random
from typing import List
words = ['absorb', 'abuse', 'academic', 'accept', 'according', 'account', 'across', 'act', 'action', 'activity', 'actually', 'add', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again', 'against', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond', 'big', 'bill', 'billion', 'bit', 'black', 'blood', 'community', 'company', 'compare', 'computer', 'concern', 'condition','conference', 'consider', 'construction', 'consultant', 'consume', 'deal', 'death', 'debate', 'decade', 'decide', 'decision', 'deep', 'defend', 'defendant', 'defense', 'defensive', 'deficit', 'define', 'definitely', 'definition', 'degree', 'delay', 'deliver', 'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front', 'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front']

random.shuffle(words)
random_words = words[0:10]
real_words = random_words[:]
print(random_words)
for word in random_words:
    b = [x for x in word]
    random_words[random_words.index(word)]=b

for word in random_words:
    count = 0
    for ch in word:
        r = random.randrange(0,3)
        if r == 0:
            if count >= len(word)//2 or count >= 3:
                break    
            word[word.index(ch)]='_'
            count += 1
    j = ''.join(word)
    if "_" not in j:
        word[-1]="_"
        j = ''.join(word)
    random_words[random_words.index(word)]=j

print(random_words)
answers = []
print(real_words)
for i in random_words:
    print(i)
    
    n=input("Guess The Word : ")
    if n in real_words:
        print(type(n))
        answers.append(True)
    else:
        print(type(n))
        answers.append(False)

print(answers)

'''
|----|
|	 |
|	 |
|    |
|	 O
|   -|-
|	 /\
|_________
'''
if answers.count(False) == 1:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 2:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 3:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 4:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 5:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 6:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 7:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 8:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 9:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
elif answers.count(False) == 10:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()
else:
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')

            if j==6 and i == 1:
                print('|',end='')
            if j==6 and i == 2:
                print('    |',end='')
            if j==6 and i == 3:
                print('    |',end='')
            if j==6 and i == 4:
                print('    |',end='')
            if j==6 and i == 5:
                print('    O',end='')
            if j==6 and i == 6:
                print('   -|-',end='')
            if j==6 and i == 7:
                print('    /\\',end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()

# i=1
# while i<=8:
#     j=1
#     while j<=10:
#         if i==1 and j>=2 and j<6:
#             print('-',end='')
#         if j==1:
#             print('|',end='')

#         if j==6 and i == 1:
#             print('|',end='')
#         if j==6 and i == 2:
#             print('    |',end='')
#         if j==6 and i == 3:
#             print('    |',end='')
#         if j==6 and i == 4:
#             print('    |',end='')
#         if j==6 and i == 5:
#             print('    O',end='')
#         if j==6 and i == 6:
#             print('   -|-',end='')
#         if j==6 and i == 7:
#             print('    /\\',end='')


#         if i==8 and j>1:
#             print('_',end='')

#         j += 1
#     i += 1
#     print()


# i = 0
# while i<=7:
#     j=0
#     while j<=9:
#         if j == 0:
#             print('|',end='')
#         if j>0 and i==0:
#             print('-',end='')
#         else:
#             print(' ',end='')
#         j += 1
#         if i==7 and j>=0:
#             print('_',end='')
#         # if j == 8 and i == 0:
#         #     print('|',end='')
#     print()
#     i += 1
