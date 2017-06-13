numeros = [21681, 231073, 26413]


class consultar(object):
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def nConsecutivos(self):
        if self.a == (self.a + 1):
            return False
        if self.b == (self.b + 1):
            return False
        if self.c == (self.c + 1):
            return False
        if self.d == (self.d + 1):
            return False
        if self.e == (self.e + 1):
            return False

    def nPares(self):
        if (self.a + self.b + self.c + self.d + self.e) % 2 == 0:
            return True
        else:
            return False

    def n1npodeserigualao2(self):
        if self.a == self.e:
            return False


for i in numeros:
    n = str(i)
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    d = int(n[3])
    e = int(n[4])
    c = consultar(a, b, c, d, e)
    if False in (c.n1npodeserigualao2(), c.nConsecutivos(), c.nPares()):
        print("O numero", i, "não atende as necessidades")
    else:
        print("#O numero", i, "atende as necessidades!")
