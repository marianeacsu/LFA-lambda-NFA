cin = open("file.txt")

class LNFA_proiect1:
    def __init__(self):
        self.alf = set()
        self.nr_stari,nr_tranzitii = tuple(map(int,cin.readline().split()))
        self.a = [[[] for h in range(self.nr_stari)] for i in range(self.nr_stari)] 
        while nr_tranzitii:
            nr_tranzitii -= 1
            i,j, lit = cin.readline().split()
            self.alf.add(lit)
            self.a[int(i)][int(j)].append(lit)
        self.alf = self.alf - set('#') 
        self.stare_initiala = int(cin.readline()) 
        self.stari_finale = list(map(int,cin.readline().split())) [1:]
        self.drumuri = []

    def back(self, stare, s, poz,d):
        drum = d.copy()
        n = len(s)
        drum.append(stare)
        if poz == n:
            if stare in self.stari_finale:
                self.ok = True
                a = drum.copy()
                self.drumuri.append(a)
            else:
                for i in range(self.nr_stari):
                    if self.a[stare][i] != []:
                        for j in self.a[stare][i]:
                            if j == '#':
                                self.back(i, s, poz,drum)
        elif s[poz] == '#':
            for i in range(self.nr_stari):
                if self.a[stare][i] != []:
                    for j in self.a[stare][i]:
                        if j == '#':
                            self.back(i, s, poz,drum)
                            self.back(stare, s, poz + 1,drum)
                            self.back(i, s, poz + 1,drum)
                        else:
                            self.back(stare, s, poz + 1,drum)
                else:
                    self.back(stare, s, poz + 1,drum)
        else:
            for i in range(self.nr_stari):
                if self.a[stare][i] != []:
                    for j in self.a[stare][i]:
                        if j == '#':
                            self.back(i, s, poz,drum)
                        else:
                            d = len(j)
                            if d + poz <= n:
                                if s[poz:poz+d] == j:
                                    self.back(i,s,d + poz,drum)

    def accept(self, lit):
        self.drumuri = []
        self.ok = False
        self.back(self.stare_initiala, lit, 0, [])
        if self.ok:
            print("DA")
            print("Traseu: ", end = " ")
            print(*self.drumuri[0])
        else:
            print('NU')

LNFA = LNFA_proiect1()
d = int(cin.readline())
while d:
    d-=1
    c = cin.readline()
    c = c.replace("\n", "")
    LNFA.accept(c)

cin.close()