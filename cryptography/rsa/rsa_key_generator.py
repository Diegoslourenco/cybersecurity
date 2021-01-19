# RSA (Rivest-Shamir-Adleman) Key Generator

from euclidean import find_gcd, find_mod_inverse
from miller_rabin import generate_large_prime
import random

def generate_key(key_size):
    """
    Generates a key pair according to the keysize bits
    """
    # Create two prime numbers and multiple them
    p = generate_large_prime(key_size)
    q = generate_large_prime(key_size)
    n = p * q

    # Create a number that is relatively prime to (p-1)*(q-1)
    while True:
        # Trying until find a valid random number
        e = random.randrange(2**(key_size - 1), 2**(key_size))
        if find_gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Calculate the mod inverse of e
    d = find_mod_inverse(e, (p - 1) * (q - 1))

    public_key = (n, e)
    private_key = (n, d)

    return (public_key, private_key)

def export_key(name, key_size):
    """
    Creates two files with the keys name_public_key.txt and name_private_key.txt
    """
    public_key, private_key = generate_key(key_size)

    # Saving the public key
    with open(f'{name}_public_key.txt', 'w') as key_file:
        key_file.write(f'{key_size}\n{public_key[0]}\n{public_key[1]}')

    # Saving the private key
    with open(f'{name}_private_key.txt', 'w') as key_file:
        key_file.write(f'{key_size}\n{private_key[0]}\n{private_key[1]}')

    return