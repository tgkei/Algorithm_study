# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

score = dict()
win = dict()

N = int(input())

for _ in range(N*(N-1)):
    tmp_input = list(input().split())
    team1 = tmp_input[0]
    team2 = tmp_input[2]
    score1 = int(tmp_input[1])
    score2 = int(tmp_input[3])

    if team1 not in score:
        win[team1] = 0
        score[team1] = 0
    
    if team2 not in score:
        win[team2] = 0
        score[team2] = 0
    
    if score1 < score2:
        win[team2] += 1
        if score1:
            score[team2] += 1
            score[team1] -= 1
        else: 
            score[team2] += 2
            score[team1] -= 2
    else:
        win[team1] += 1
        if score2: 
            score[team1] +=1
            score[team2] -= 1
        else: 
            score[team1] += 2
            score[team2] -= 2
    
win_team_dict = dict()
for k,v in sorted(win.items(), key = lambda item: -item[1]):
    if v not in win_team_dict:
        win_team_dict[v] = [k]
    else:
        win_team_dict[v].append(k)

for win, teams in win_team_dict.items():
    if len(teams) > 1:
        tmp = dict()
        for team in teams:
            if score[team] not in tmp:
                tmp[score[team]] = [team]
            else: tmp[score[team]].append(team)
        for k, v in tmp.items():
            v.sort()
        tmp = {k: v for k, v in sorted(tmp.items(), key=lambda item: item[1])}

        for k, v in tmp.items():
            if len(v) == 1:
                print(f'{v} {win} {k}')
            else:
                for tmp_v in v:
                    print(f'{tmp_v} {win} {k}')
    else:
        print(f'{teams[0]} {win} {score[teams[0]]}')
    