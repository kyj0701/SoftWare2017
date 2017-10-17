def Theory():
	t = str(input("이론값을 입력해주십시오 : "))
	if not isfloat(t) or float(t) <= 0:
		return Theory()
	else:
		return float(t)


def Experiment():
	e = str(input("실험값을 입력해주십시오 : "))
	if not isfloat(e) or float(e) < 0:
		return Experiment()
	else:
		return float(e)


def isfloat(s):
	(m,_,n) = s.partition(".")
	return (m.isdigit() and (n.isdigit() or n=="")) or m=="" and n.isdigit()


def main():
	print("오차율 계산 프로그램입니다.")
	r1 = Theory()
	r2 = Experiment()
	result = abs(r1-r2)/r1 * 100
	print("오차율은 " + str(round(result,4)) + "%입니다.")
	a = str(input("더 계산해드릴까요?(Y를 치시면 다시, 다른 문자를 치시면 프로그램이 종료됩니다.) : "))
	if a == "Y":
		main()
	else:
		print("안녕히가세요")

main()