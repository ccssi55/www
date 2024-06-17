import random
while (p := input("rock, siser, paper 중에 선택하세요: ").lower()) and print(f'컴퓨터 = {(c := random.choice(["rock", "siser", "paper"]))}\n당신 = {p}, {"비겼습니다" if p == c else "이겼습니다" if (p == "rock" and c == "siser") or (p == "paper" and c == "rock") or (p == "siser" and c == "paper") else "졌습니다"}') or input("다시 하시겠습니까? (y/n): ").lower() == 'y': pass
print("게임을 종료합니다.")

