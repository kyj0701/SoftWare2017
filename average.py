def main():
	r = 0
	t = str(input("평균을 구하고 싶은 값의 개수를 입력해 주십시오 : "))
	if t.isdigit():
		t = int(t)
		for i in range(t):
			a = float(input(str(i+1) + " 번 값을 입력해 주십시오 : "))
			r += a
		result = r/t
		print("평균은 " + str(round(result,4)) + " 입니다.")
		a = str(input("더 계산해드릴까요?(Y를 치시면 다시, 다른 문자를 치시면 프로그램이 종료됩니다.) : "))
		if a == "Y":
			main()
		else:
			print("안녕히가세요")
	else:
		main()

main()