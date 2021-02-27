import decimal
from itertools import count

# First few digits of Pi 200 decimal digits of Pi
# We are taking as 'good enough for this exercise'
pi_str = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'
pi = decimal.Decimal(pi_str)

final_powers = []
for decimal_places in range(2, 50):
    # Set precision for power calculations, 5n + 1 is probably enough
    decimal.getcontext().prec = decimal_places * 5 + 1
    power = 2
    pi_trunc = decimal.Decimal(pi_str[:decimal_places + 2])
    while True:
        pi_power = pi ** power
        pi_power_trunc = pi_trunc ** power

        # First check if integers are of
        if int(pi_power) != int(pi_power_trunc):
            break

        # Get decimal digits
        pi_power_digits = str(pi_power).split('.')[1]
        pi_power_trunc_digits = str(pi_power_trunc).split('.')[1]
        

        # Find first figit where they differ
        for i in count():
            if pi_power_digits[i] != pi_power_trunc_digits[i]:
                break
        
        if i == 0:
            break

        # Uncomment below to see it matches graph at 11:00 for digits 2 to 9
        # print(f'{decimal_places} digits ({pi_trunc}) @ power {power} results in {i} digit(s) of precision')
        power += 1
    final_powers.append(power)
print(final_powers)
