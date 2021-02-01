from fractions import Fraction


class F(Fraction):

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


a, b = [int(x) for x in input().split()]

print(F(7 - max(a, b), 6))