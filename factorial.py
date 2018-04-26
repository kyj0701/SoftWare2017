def main():
	res = 1
	t = str(input("어떤 수의 팩토리얼을 구해드릴까요? : "))
	if t.isdigit():
		t = int(t)
		for i in range(t):
			res *= (i+1)
		print("이 수의 팩토리얼은 " + str(res) + " 입니다.")
		a = str(input("더 계산해드릴까요? (y/n) : "))

		if a == "y":
			main()
		elif a == "n":
			print("안녕히가세요")
	else:
		main()

main()
