"""
-polynomial.py
-this module will process polynomials with one essential class :
        polynomial

"""
import settings
import numpy as np 
import number_theory as nt 
import graph_func as gr 

class polynomial(object):
    def __init__(self, coeffs):
        self.coeffs = coeffs#;self.normalize()
        self.deg = len(self.coeffs) - 1

    def __call__(self, x):
        s = 0
        for i in range(len(self.coeffs)):
            s += self.coeffs[i] * (x ** (self.deg - i)) 

        return s

    def __str__(self):
        string = []
        for i in range(len(self.coeffs)):
            sentence = "%d%s" % (self.coeffs[i], "x^%d" % (self.deg - i) if self.deg - i != 0 else "")
            string.append(sentence)

        s = '+'.join(string)
        return s

    def functionize(self):
        return lambda x : self(x)

    def normalize(self):
        new_coeffs = [];
        for i in range(len(self.coeffs)):
            if i != 0:
                break;
        
        new_coeffs = self.coeffs[i + 1: ]

        self.coeffs = new_coeffs[:]

        return True

    def __add__(self, other):
        p1 = self.coeffs[:] if self.deg <= other.deg else other.coeffs[:]
        p2 = other.coeffs[:] if self.deg <= other.deg else self.coeffs[:]
        p3 = len(p2) * [0]
        CONSTANT_OF_LENGTH = len(p2)

        for _ in range(CONSTANT_OF_LENGTH - len(p1)):
            p1.insert(0, 0)
        
        for i in range(CONSTANT_OF_LENGTH):
            p3[i] += p1[i] + p2[i]
        
        return polynomial(p3)
    
    def __sub__(self, other):
        other_copy = other * (-1)
        return self + other_copy 
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            p = [c * other for c in self.coeffs]
            return polynomial(p)

        elif isinstance(other, polynomial):
            p1 = list(zip(self.coeffs, range(self.deg, -1, -1)))
            p2 = list(zip(other.coeffs, range(other.deg, -1, -1)))
            p3 = [(c1 * c2, e1 + e2) for c1, e1 in p1 for c2, e2 in p2]

            pow_dict = {}
            for c, p in p3:
                if p in pow_dict.keys():
                    pow_dict[p] += c

                else:
                    pow_dict.update({p : c})
            
            p3_elems = list(pow_dict.items()); p3_elems = sorted(p3_elems, key = lambda x : x[0], reverse = True)
            p3_res = [c for p, c in p3_elems]

            return polynomial(p3_res)

    
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            p = [c / other for c in self.coeffs]
            return polynomial(p)

        elif isinstance(other, polynomial):
            a1 = np.array(self.coeffs)
            a2 = np.array(other.coeffs)
            q, r = np.polydiv(a1, a2); q = list(q); r = list(r)
            return polynomial(q), polynomial(r)

    def R(self):
        if self.deg == 1:
            return [-self.coeffs[1] / self.coeffs[0]]

        elif self.deg == 2:
            d = self.coeffs[1] ** 2 - 4 * self.coeffs[0] * self.coeffs[1]
            if d < 0:
                return []
            elif d == 0:
                return -self.coeffs[1] / (2 * self.coeffs[0])

            else:
                return [(-self.coeffs[1] + d ** .5) / (2 * self.coeffs[0]), (-self.coeffs[1] - d ** .5) / (2 * self.coeffs[0])]

        else:
            return list(np.roots(self.coeffs))

    def graph(self, f=[]):
        f.append(self)
        gr.plot(-100, 100, f)

    def undefined(self):
        return []
