import random
while True:

	def lotto_game():
		while True:
			def Lotto():
				lotto = []

				while True:
					a = int(random.random()*45) + 1
					check = True
					for i in lotto:
						if a == i:
							check = False
					if check:
						lotto.append(a)
					if (len(lotto) == 6):
						break
				return  lotto

			win = [1,4,13,29,38,39]
			bonus = [7]
			def last_win():
				count = 0
				while True:
					lotto = Lotto()
					count += 1
					lotto.sort()
					if win == lotto:
						break
				print(count)



			def count():
				n = int(input("돈 입력 : "))
				result = {'1등':0,'2등':0,'3등':0,'4등':0,'5등':0,'꽝':0}
				while (n > 1000):
					lotto = Lotto()
					count2 = 0
					count_bonus = 0
					n = n - 1000
					for j in win:
						if j in lotto:
							count2 += 1
					if count2 == 6:
						result['1등'] +=1
					elif count2 ==5 and bonus in lotto :
						result['2등'] +=1
					elif count2 == 5:
						result['3등'] +=1
					elif count2 == 4:
						result['4등'] +=1
					elif count2 == 3:
						result['5등'] +=1
					else:
						result['꽝'] += 1
				print(result)

			def year():
				def check(x,y):
					if x== y:
						return True
					return False

				week = 0
				end = True
				while end:
					com = Lotto()
					week+=1
				for i in range(100):
					me = Lotto()
					if check(com,me):
						end = False
						year = week/52
				print(year)
			number1 = int(input("1: 저번주 로또 번호와 비교하기, 2: 1~5등을 각각 몇번할 수 있을까?, 3: 로또에 당첨되기까지 걸리는 년횟수, 4: 종료하기 : "))
			if number1 == 1:
				last_win()
			elif number1 == 2:
				count()
			elif number1 == 3:
				year()
			elif number1 == 4:
				exit = input("이 게임을 종료하고 싶으면 종료를 입력하세요. \n 돌아가려면 아무키나 입력하세요 : ")
				if exit != "종료":
					False
				else:
					break
			else:
				print("다시 입력하세요.")
				False
			
			
		
	def gogae():
		while True:
			def twen():
				com_num = random.randint(1,1000)
				for i in range(1,11):
					num = int(input("숫자 입력({}번/10번)".format(i)))
					if (num > com_num):
						print("down")
					elif (num < com_num):
						print("up")
					else:
						break
				if ( i <= 10):
					print("정답입니다 ! {}만에 맞췄습니다. 컴퓨터가 생각한 숫자는 {}입니다.".format(i,com_num))
				else:
					print("10번안에 맞추지 못했습니다.")
			number1 = int(input("1: 게임계속하기, 2: 종료하기 : "))
			if number1 == 1:
				twen()
			elif number1 == 2:
				exit = input("이 게임을 종료하고 싶으면 종료를 입력하세요. \n 돌아가려면 아무키나 입력하세요 : ")
				if exit != "종료":
					False
				else:
					break
			else:
				print("다시 입력하세요")
				False

	def rsp():
		com = random.randint(1,3)
		me = input("1: 가위, 2: 바위, 3: 보")
		if com == me:
			print("비김")
		elif( com == 1 and me == 2 ) or (com == 2 and me == 3) or (com == 3 and me == 1):
			print("이김")
		else:
			print("짐")
	def game_369():
		for i in range(1,101):
			j = str(i)
		count = 0
		for k in j:
			if (k == '3' or k == '6' or k == '9'):
				count += 1
		if (count == 0):
				print(i,end =' ')
		else:
				print(count*'짝',end=' ')

	print("1: 가위바위보, 2: 369, 3: 스무고게, 4: 로또 게임")
	number = int(input("어떤 게임을 하겠습니까? : "))
	
	
	if number == 1:
		rsp()
	elif number == 2:
		game_369()
	elif number == 3:
		gogae()
	elif number == 4:
		lotto_game()
	else:
		print("다시 선택하세요")
		False
	exit = input("종료하고 싶으면 종료를 입력하세요. \n 게임을 다시 선택하고 싶다면 아무키나 입력하세요 : ")
	if exit != "종료":
		False
	else:
		break