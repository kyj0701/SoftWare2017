import math

def main():
	print("이차방정식의 근을 구해드립니다.")
	a = float(input("2차항의 계수를 입력해 주십시오 : "))
	b = float(input("1차항의 계수를 입력해 주십시오 : "))
	c = float(input("상수항을 입력해 주십시오 : "))
	if a != 0:
		i = math.sqrt(b**2-4*a*c)
		result1 = (-b + i)/(2*a)
		result2 = (-b - i)/(2*a)
		print("근은 " + str(result1) + ", " + str(result2) + " 입니다.")
		j = str(input("더 계산해드릴까요?(Y를 치시면 다시, 다른 문자를 치시면 프로그램이 종료됩니다.) : "))
		if j == "Y":
			main()
		else:
			print("안녕히가세요")
	else:
		main()

main()
