import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

lcm_value = lcm(36, 24)
print(lcm_value)  # Output: 72
