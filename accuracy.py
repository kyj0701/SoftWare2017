def isfloat(s): #실수여부 확인
	(m,_,n) = s.partition(".")
	return (m.isdigit() and (n.isdigit() or n=="")) or m=="" and n.isdigit()

c = 'y'
def accuracy():
	print("##########오차율 계산기##########")
	print("소숫점 4자리까지만 계산해 dream! 낄낄\n")
	
	a = str(input("이론값을 입력하렴 : "))

	while not isfloat(a) or a == '0':
		print("\n잘못된 입력값이잖니 ㅡ.ㅡ \n")
		if a == '0':
			print("이론값이 0인 경우에는 오차를 계산할 수 없어...\n")
		a = str(input("이론값을 입력하렴 : "))


	b = str(input("실험값을 입력하렴 : "))
	while not isfloat(b):
		print("\n잘못된 입력값이잖니 ㅡ.ㅡ \n")
		b = str(input("실험값을 입력하렴 : "))

	a,b = float(a), float(b)
	ans = float(round((abs(a-b)/a)*100,4))

	print("\n>>>오차율은 " + str(ans) +"% 란다.<<<")
	
	if ans >= 30:
		print("p.s) 맙소사...오차가 크잖아? 실험을 다시 해야겠는데?\n")


while 1:
	if c == 'y':
		accuracy()
		c = input("계속 하시겠습니까? (y/n)")
	elif c == 'n':
		print("안녕히 가세요.")
		break;
	else:
		c = input("계속 하시겠습니까.? (y/n)")

