num1 = int(input("정수를 입력하여주세요: "))

if num1 >= 1 and num1 <= 9:
	for i in range(1, 10 ):
		print(f"{num1} X {i} = {num1*i}")
else:
  print("1~9 사이의 정수를 입력해주세용^^")