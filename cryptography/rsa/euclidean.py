# Euclidean

def find_gcd(a, b):
    """
    Return the Greatest Common Divisor
    """
    # According to Euclidean Algorithm
    while a != 0:
        a, b = b % a, a
    return b

def find_mod_inverse(a, m):
    """
    Return the modular inverse of a and m that is
    (a * x) % m = 1
    """
    if find_gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    # Calculating with the Extended Euclidean Algorithm
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m