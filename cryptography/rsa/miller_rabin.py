# Rabin-Miller Algorithm

import random

def test_miller_rabin(number):
    """
    Return true if the given number is prime
    """
    # the maximum that will go from 0 to num - 1
    s = number - 1
    # Start t to track how many times we will halve s
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even
        s = s // 2
        t += 1
      
    # Picking a random integer in [2..number-2] 
    # Corner cases make sure that number > 4 
    a = 2 + random.randint(1, number - 4)
  
    # Compute a**s % n 
    x = pow(a, s, number) 
  
    if (x == 1 or x == number - 1): 
        return True 
  
    # Keep squaring x while one of the following doesn't happen 
    # (i) s does not reach n-1 
    # (ii) (x**2) % number is not 1 
    # (iii) (x**2) % number is not n-1 
    while (s != number - 1): 
        x = (x * x) % number
        s *= 2; 
  
        if (x == 1): 
            return False
        if (x == number - 1): 
            return True 
  
    # Return composite 
    return False


def check_prime(number):
    """
    Return True if the number is prime
    """
    if (number < 2):    # 0, 1, and negative numbers are not prime
        return False

    # using a list of prime numbers to check and speed the process
    low_primes = [  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                    83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                    179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
                    271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373,
                    379, 383, 389, 97, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 
                    479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593,
                    599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821,
                    823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
                    941, 947, 953, 967, 971, 977, 983, 991, 997
                ]

    if number in low_primes:
        return True

    # Check if any of the low prime numbers can divide number
    for prime in low_primes:
        if (number % prime == 0):
            return False

    # Call test_miller_rabin() to determine if number is a prime.
    return test_miller_rabin(number)


def generate_large_prime(key_size=1024):
    """
    Return a random prime number given a keysize of bits
    """
    while True:
        number = random.randrange(2**(key_size - 1), 2**(key_size))
        if check_prime(number):
            return number