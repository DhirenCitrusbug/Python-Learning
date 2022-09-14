import datetime
def schedul(teams,ind,ln):
    teams = set(teams)
    matches = set()
    scheduled ={}


    print(teams)
    for team in teams:
        for i in teams:
            if i != team:
                match = (team,i)
                match = tuple(sorted(match))
                matches.add(match)
            
    matches = list(matches)
    
    for i in matches:
        indx = matches.index(i)
        if indx == 0:
            d = datetime.datetime.today() + datetime.timedelta(days=ln*ind)
            scheduled[i] = d
        else:
            d = scheduled[matches[indx-1]] + datetime.timedelta(days=1)
            scheduled[i] = d
        print('for team',i[0],'and',i[1],'time is',scheduled[i])


while True:
    series_name= input("Enter Your Series Name : ")
    total_team=int(input("Enter Total Number Of Teams "))
    g = int(input("Number of Group : "))
    groups = []
    grp = []
    teams = list(range(total_team,0,-1))
    if total_team < 1:
        print('Atleast Four Teams Required')
        continue
    for i in range(g):
        grp = []
            
        for j in range(int(total_team//g)):
            grp.append(teams.pop())
        groups.append(grp)
        
        
        
        if len(teams)<=total_team//g:
            groups.append(teams)
            if len(groups[-1])==1:
                groups[-2].extend(groups[-1])
                groups.pop(-1)
            break
    pb = True
    for i in groups:
        if len(i)==1:
            pb = False
            break
        else:
            schedul(tuple(i),groups.index(i),total_team//g)

    if not pb:
        print('Given Number of Group is Not Possible For Playing Match')