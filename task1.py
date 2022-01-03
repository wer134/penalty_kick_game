import random

round = {'1':'a','2':'b'}
result1 = {'1':'a','2':'b','3': 'c','4':'d','5':'f'}
result2 = {'1':'a','2':'b','3': 'c','4':'d','5':'f'}
score_team1=0
count_team1 = 0
score_team2=0
count_team2 = 0
while True:
    try:
        proba = random.randint(1,100) #골대 맞을 확률
        keep1 = random.randint(1,2) # 오른쪽 왼쪽
        keep2 = random.randint(1,3) # 상 중 하
        shoot1 = int(input("슛할 방향은???(1: 왼쪽, 2: 오른쪽)\n>> "))
        if shoot1 > 2:
            print("1팀 : 벗어났습니다~")
            round['1'] = '○'
        else:
            if keep1 == shoot1:
                print("1팀 : 방향이 읽혔습니다~")
                shoot2 = int(input("1팀 : 슛할 방향은???(1: 상, 2: 중, 3: 하)\n>> "))
                if shoot2 != keep2 and proba <= 85:
                    print("1팀 : 들어갔습니다~")
                    round['1'] = '●'
                    score_team1 += 1
                elif proba > 85 :
                    print("1팀 : 골대 맞았습니다~")
                    round['1'] = '○'
                elif keep2 == shoot2:
                    print("1팀 : 막혔습니다~")
                    round['1'] = '○'
            else:
                if proba <= 85:
                    print("1팀 : 들어갔습니다~")
                    round['1'] = '●'
                    score_team1 += 1
                else:
                    print("1팀 : 골대 맞았습니다~")
                    round['1'] = '○'
        count_team1 += 1

        proba = random.randint(1,10) #골대 맞을 확률
        keep1 = random.randint(1,2) # 오른쪽 왼쪽
        keep2 = random.randint(1,3) # 상 중 하
        comshoot1 = random.randint(1,3)
        comshoot2 = random.randint(1,3)
        if comshoot1 > 2:
            print("2팀 : 벗어났습니다~ ")
            round['2'] = '○'
        else:
            if keep1 == comshoot1:
                print("2팀 : 방향이 읽혔습니다~")
                if comshoot2 != keep2 and proba <= 85:
                    print("2팀 : 들어갔습니다~")
                    round['2'] = '●'
                    score_team2+=1
                elif proba > 85:
                    print("2팀 : 골대 맞았습니다~")
                    round['2'] = '○'
                elif keep2 == comshoot2:
                    print("2팀 : 막혔습니다~")
                    round['2'] = '○'
            else:
                if proba <= 85:
                    print("2팀 : 들어갔습니다~")
                    round['2'] = '●'
                    score_team2+=1
                else:
                    print("2팀 : 골대 맞았습니다~")
                    round['2'] = '○'
        count_team2 += 1
        round = list(round.values())
        
        
        print(round)  
        if  count_team2 == 5 and count_team2 == 5 and score_team2 != score_team1:
            if score_team1 < score_team2:
                print("1팀 : " ,count_team1,"번" ," 중 ", score_team1,"번 성공\n" , "2팀 : ",count_team2 ,"번", " 중 " ,score_team2,"번 성공")
                print("2팀(컴퓨터)이 이겼습니다~")
                break
            else :
                print("1팀 : " ,count_team1,"번" ," 중 ", score_team1,"번 성공\n" , "2팀 : ",count_team2 ,"번", " 중 " ,score_team2,"번 성공")
                print("1팀이 이겼습니다~")
                break
        
        if count_team2 > 5 and count_team2 > 5 and score_team2 != score_team1:
            print("1팀 : " ,count_team1,"번" ," 중 ", score_team1,"번 성공\n" , "2팀 : ",count_team2 ,"번", " 중 " ,score_team2,"번 성공")
            break
    except ValueError :
        print('\033[93m' + "[오류] 숫자만 입력해 주세요" + '\033[97m')
        