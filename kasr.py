class Kasr:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m
    
    def sum(self, sums):
        result= Kasr(None, None)
        result.soorat= self.soorat * sums.makhraj + self.makhraj*sums.soorat
        result.makhraj= self.makhraj * sums.makhraj
        return result
    def mul(self, times):
        result= Kasr(None, None)
        result.soorat= self.soorat * times.soorat
        result.makhraj= self.makhraj * times.makhraj
        return result
    def sub(self, subs):
        result= Kasr(None, None)
        result.soorat= self.soorat * subs.makhraj - self.makhraj*subs.soorat
        result.makhraj= self.makhraj * subs.makhraj
        return result
    def div(self, divs):
        result= Kasr(None, None)
        result.soorat= self.soorat / divs.soorat
        result.makhraj= self.makhraj / divs.makhraj
        return result
    def show(self):
        print(self.soorat, '/' ,self.makhraj)
    def show_menu(x, y):
        options = ['sum', 'sub', 'mul','div']
        opn= 1
        for option in options:
            print(opn, option)
            opn+=1
        choice = input ('choose an option for exit enter "exit": ')
        if choice == '1':
            c = x.sum(y)
            c.show()
        if choice == '2':
            c = x.sub(y)
            c.show()
        if choice == '3':
            c = x.mul(y)
            c.show()
        if choice == '4':
            c = x.div(y)
            c.show()
        elif choice == 'exit':
            exit()
active = True
while active:
    a_n = int(input('input 1st numerator'))
    a_d = int(input("input 1st denumerator"))
    b_n = int(input('input 2nd numerator'))
    b_d = int(input('input 2nd denumerator'))
    a = Kasr(a_n, a_d)
    b = Kasr(b_n, b_d)
    Kasr.show_menu(a, b)

