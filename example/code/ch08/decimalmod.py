# modules
import decimal

# floating point expression
print(7.6 + 8.7)

# decimal expression
print(decimal.Decimal(7.6) + decimal.Decimal(8.7))

# assign precision
decimal.getcontext().prec = 3
print(decimal.Decimal(7.6) + decimal.Decimal(8.7)) 
decimal.getcontext().prec = 4
print(decimal.Decimal(7.6) + decimal.Decimal(8.7)) 
