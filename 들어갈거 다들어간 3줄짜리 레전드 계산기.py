num1, num2 = float(input("첫번째 숫자: ")), float(input("두번째 숫자: "))
while (oprate := input(" +,-,/,* ")) not in ['+','-', '/', '*']: print("유효하지 않습니다. 다시 입력해주세요 ")
print(f" {num1} {oprate} {num2} = {eval(f'{num1}{oprate}{num2}')}" if oprate != '/' or num2 != 0 else (f"{num1}는 0으로 나눌 수 없습니다"))

