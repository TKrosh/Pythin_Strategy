s = [[0] * 10 for _ in range(10)]
s[0][0] = 5


def show():
    for _ in s:
        print(_)


#def limit(num):
#    if num < 0 :

amount = 5
for _ in range(2):
    for x in range(0 - amount, 0 + amount + 1):
        for y in range(0 - amount, 0 + amount + 1):
            if s[x][y] != 0:
                amount = s[x][y]
                try:
                    if s[x - 1][y] == 0:
                        s[x - 1][y] = amount - 1
                    if s[x + 1][y] == 0:
                        s[x + 1][y] = amount - 1
                    if s[x][y - 1] == 0:
                        s[x][y - 1] = amount - 1
                    if s[x][y + 1] == 0:
                        s[x][y + 1] = amount - 1
                except Exception:
                    pass
show()
