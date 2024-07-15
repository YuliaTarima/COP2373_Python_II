from decimal import Decimal

d1, d2 = Decimal(1.40), Decimal(0.60)

print(d1 + d2)

from decimal import Decimal
fr1 = Decimal('1.200')
fr2 = Decimal('1.2')

if fr1 == fr2:
    print('They are equal.')
else:
    print('They are not equal.')


from fractions import Fraction

fraction = Fraction(1, 5)
print(fraction)  # Outputs: 1/5

print(Fraction(1,5))