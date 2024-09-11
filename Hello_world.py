d0 = [
[1,1,1],
[1,0,1,],
[1,0,1,],
[1,0,1,],
[1,1,1]
]
d1 =[
[0,1,0],
[0,1,0],
[0,1,0],
[0,1,0],
[0,1,0],
[0,1,0]
]
d2 = [
[1,1,1],
[0,0,1],
[1,1,1],
[1,0,0],
[1,1,1]
]
d3 = [
[1,1,1],
[0,0,1],
[1,1,1],
[0,0,1],
[1,1,1]
]
d4 = [
[1,0,1],
[1,0,1],
[1,1,1],
[0,0,1],
[0,0,1]
]
d5 = [
[1,1,1],
[1,0,0],
[1,1,1],
[0,0,1],
[1,1,1]
]
d6 = [
[1,0,0],
[1,0,0],
[1,1,1],
[1,0,1],
[1,1,1]
]
d7 = [
[1,1,1],
[1,0,1],
[0,0,1],
[0,0,1],
[0,0,1]
]
d8 = [
[1,1,1],
[1,0,1],
[1,1,1],
[1,0,1],
[1,1,1]
]
d9 = [
[1,1,1],
[1,0,1],
[1,1,1],
[0,0,1],
[1,1,1]
]

digit_pattern = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9]
digit_pattern[2]

def show(d):
    for j in range(5):
        for i in range(3):
            if d[j][i]== 1:
                c='■'
            else:
                c='□'
            print(c, end='')
        print()
    print()

for i in range(10):
    show(digit_pattern[i])

def display(digits):
    for j in range(5):
        n = len(digits)
        for k in range(n):
            d = int(digits[k])
            for i in range(3):
                if digit_pattern[d][j][i]==1:
                    c = '■'
                else:
                    c='□'
                print(c, end='')
            print(' ', end='')
        print()

display('20241116')