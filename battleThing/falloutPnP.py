import random

print('너님은 폴아웃세계로 왔음. 종족을 선택하시오(인간만 가능)')
playerRace = input()
while playerRace != '인간':
    print('거 인간만 된다니까요!')
    playerRace = input()

print('good')
