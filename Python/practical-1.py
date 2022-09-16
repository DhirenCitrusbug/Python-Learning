import random
import time
words = ['absorb', 'abuse', 'academic', 'accept', 'according', 'account', 'across', 'act', 'action', 'activity', 'actually', 'add', 'address', 'administration', 'admit', 'adult', 'affect', 'after', 'again', 'against', 'begin', 'behavior', 'behind', 'believe', 'benefit', 'best', 'better', 'between', 'beyond', 'big', 'bill', 'billion', 'bit', 'black', 'blood', 'community', 'company', 'compare', 'computer', 'concern', 'condition','conference', 'consider', 'construction', 'consultant', 'consume', 'deal', 'death', 'debate', 'decade', 'decide', 'decision', 'deep', 'defend', 'defendant', 'defense', 'defensive', 'deficit', 'define', 'definitely', 'definition', 'degree', 'delay', 'deliver', 'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front', 'floor', 'fly', 'focus', 'follow', 'food', 'foot', 'for', 'force', 'foreign', 'forget', 'form', 'former', 'forward', 'four', 'free', 'friend', 'from', 'front']
random.shuffle(words)
random_words = words[0:10]
real_words = random_words[:]
print(random_words)

def printPattern(count):
    patrn = {
    1:'|',
    2:'    |',
    3:'    |',
    4:'    |',
    5:'    O',
    6:'   -',
    7:'|',
    8:'-',
    9:'   /',
    10:'\\',
}
    i=1
    while i<=8:
        j=1
        while j<=10:
            if i==1 and j>=2 and j<6:
                print('-',end='')
            if j==1:
                print('|',end='')
            for k in range(1,count+1):
                if j==6 and k == 10 and i==7:
                    print(patrn[k],end='')
                    continue
                if j==6 and k == 9 and i==7:
                    print(patrn[k],end='')
                    continue
                if j==6 and k == 8 and i==6:
                    print(patrn[k],end='')
                    continue
                if j==6 and k == 7 and i==6:
                    print(patrn[k],end='')
                    continue
                    
                if j==6 and i == k and i<=6:
                    print(patrn[k],end='')


            if i==8 and j>1:
                print('_',end='')

            j += 1
        i += 1
        print()

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
printPattern(0)
for i in random_words:
    print(i)
    n=input("Guess The Word : ")
    if n in real_words:
        print(type(n))
        answers.append(True)
        
    else:
        print(type(n))
        answers.append(False)
    if answers.count(False) == 10:
        time.sleep(3)
    printPattern(answers.count(False))

print(answers)

'''
|----|
|	 |
|	 |
|    |
|	 O
|   -|-
|	 /\\
|_________
'''




