import math

class Complex(object):
    def __init__(self, real, img1):
        self.real = real
        self.img1 = img1

    def __add__(self, no):
        rl = self.real + no.real
        ig = self.img1 + no.img1
        return Complex(rl, ig)

    def __sub__(self, no):
        rl = self.real - no.real
        ig = self.img1 - no.img1
        return Complex(rl, ig)

    def __mul__(self, no):
        res = complex(self.real, self.img1) * complex(no.real, no.img1)
        return Complex(res.real, res.imag)

    def __truediv__(self, no):
        res = complex(self.real, self.img1) / complex(no.real, no.img1)
        return Complex(res.real, res.imag)

    def mod(self):
        res = math.sqrt(self.real**2 + self.img1**2)
        return Complex(res, 0)

    def __str__(self):
        if self.img1 == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.img1 >= 0:
                result = "0.00+%.2fi" % self.img1
            else:
                result = "0.00-%.2fi" % (abs(self.img1))
        elif self.img1 > 0:
            result = "%.2f+%.2fi" % (self.real, self.img1)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.img1))
        return result
    
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')