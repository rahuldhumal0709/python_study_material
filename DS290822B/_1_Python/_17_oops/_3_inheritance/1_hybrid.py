class A:
    def house(self):
        print("house")
class B(A):
    def car(self):
        print("car")
class C(A):
    def laptop(self):
        print("laptop")
class D(B):
    def bike(self):
        print("bike")
class E(C):
    def mobile(self):
        print("mobile")
class F(C):
    def bat(self):
        print("bat")
class G(E,F):
    def ball(self):
        print("ball")
g=G()
d=D()
g.house()
g.laptop()
g.mobile()
g.bat()
g.ball()
d.house()
d.car()
d.bike()