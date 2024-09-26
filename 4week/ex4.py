num = int(input("1 이상의 정수를 입력하시오: "))  

def sumfunc(n):
    total = 0  
    i = 0
  
    while i <= n:
        total = total + i  
        i = i + 1  
    return total

if num >= 1 and num <= 20:
    result = sumfunc(num)
    print(f"1~{num} 까지 정수의 합은 {result}입니다.")  
else:
    print("1~20 사이의 숫자를 입력하세요")
