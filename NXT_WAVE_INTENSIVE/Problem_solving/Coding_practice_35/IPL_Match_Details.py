n=int(input())
teams= {}
for i in range(n):
    m=input().split(';')
    if m[0] not in teams:
        teams[m[0]]={'Played':0,'Won':0,'Lost':0,'Draw':0,'Points':0}
    if m[1] not in teams:
        teams[m[1]]={'Played':0,'Won':0,'Lost':0,'Draw':0,'Points':0}
    teams[m[0]]['Played']+=1
    teams[m[1]]['Played']+=1
    if m[-1]=='win':
        teams[m[0]]['Won']+=1
        teams[m[0]]['Points']+=3
        teams[m[1]]['Lost']+=1
    elif m[-1]=='loss':
        teams[m[0]]['Lost']+=1
        teams[m[1]]['Won']+=1
        teams[m[1]]['Points']+=3
    elif m[-1]=='draw':
        teams[m[0]]['Draw']+=1
        teams[m[1]]['Draw']+=1
        teams[m[0]]['Points']+=1
        teams[m[1]]['Points']+=1


teams=dict(sorted(teams.items(),key=lambda x:x[1]['Points'],reverse=True))
for i,j in teams.items():
    print(f'Team: {i}, Matches',end=' ')
    for k,l in j.items():
        if k=='Points':
            print(f'{k}: {l}',end='')
        else:
            print(f'{k}: {l}, ',end='')
    print()
if n==0:
    print('No Output')
