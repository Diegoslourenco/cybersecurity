# RSA Cipher Algorithm

## Symmetric and Asymmetric Cipher

While a **symmetric cipher** algorithm uses only one key to encrypt and decrypt a message, for an **asymmetric cipher** algorithm are necessary two different types of keys: one to encrypt the message and another one to decrypt the ciphertext. It is safer than the **symmetric cipher** algorithms because even if someone could take the encryption key, it is still not possible to read the encrypted message. It happens because the encrypt key can only encrypt the message and the decrypt key can only decrypt a message encrypted using its key pair.

For this reason, the two keys are called the **`public key`** that is shared to the world which is used to `encrypt`, and the **`private key`** that must be kept as a secret and is used to `decrypt`.

## RSA Cipher

`RSA Cipher` (abbreviation for the author's names Rivest-Shamir-Adleman) is an asymmetric algorithm considered one of the most used nowadays. it is based on the [relatively prime integers](https://en.wikipedia.org/wiki/Coprime_integers) concept.

### RSA - Public and Private keys

First, it is necessary to generate the keys. This is made using the `rsa_key_generator.py` and there are some steps to follow:

1. Create two distinct and large prime numbers `p` and `q`. These two numbers are multiply and the result is saved in `n`.
2.   A random number `e` that is relatively prime with `(p - 1) * (q - 1)` is created.
3. The modular inverse of `e` is saved in `d`.

The `public key` is composed of the two numbers `n` and `e`. The numbers `n` and `d` consist of the `private key`.

The functions in `rsa_key_generator.py` are:

- `generate_key()`: receives a size for the keys in bits and returns the two public and private key pairs.
- `export_key()` exports a txt file that contains the size for the keys and the respective public and private pair keys in two different files. 

##### Large Prime Numbers

In order to create the two random **large prime numbers** in step 1, the **Miller-Rabin** [¹](https://crypto.stanford.edu/pbc/notes/numbertheory/millerrabin.html)  [²](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)  algorithm was used. For organization purposes, the `miller_rabin.py` was created and contains:

* `test_miller_rabin()`: returns true if a given number is prime according to the algorithm. Otherwise returns false. 
* `check_prime()`: the Miller-Rabin algorithm could be slow sometimes. In order to cover some basic prime number cases, this function checks some low prime numbers that cover a vast number of cases. If it is not the case, this function calls the `test_miller_rabin()`.
* `generate_large_prime()`: could receive the size for the keys in bits and returns a large prime number based on that. If a key size was not provided, the default value is 1024 bits.

##### Euclidean Algorithms

For steps 2 and 3 it is necessary to do some math to find the keys. A `euclidean.py` was created and the functions in it are:

* `find_gcd`: takes two numbers and uses the **Euclidean algorithm**  [¹](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)  [²](https://crypto.stanford.edu/pbc/notes/numbertheory/euclid.html)  to compute and return the Greatest Common Divisor for the given numbers.
* `fin_mod_inverse()`: returns the modular inverse of two given numbers using the [extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm).

### RSA Schema

After the keys are created, the RSA schema can be shown. With this intention, the class `Rsa` was created and can receive optionally two parameters.  The `text` is the text to be encrypted or decrypted and could be left empty. The `block size`  parameter corresponds to the size of the blocks in **bytes** that the message is going to be encrypted or decrypted and the default value is 128. The methods inside `rsa.py` are:
* `read_key_file()`: is used to open the file that contains the keys.
* `get_blocks_from_text()`: receives a text and convert it to a list of block integers encoding according to [ASCII](https://en.wikipedia.org/wiki/ASCII). Each integer has the size of the **block size** previously defined.
* `get_text_from_blocks()`: receives the block integers and the length of the message. It converts a list o block integers to the original message.
* `encrypt()`: takes the file name to save the encrypted message and the file that contains the **public key** to encrypt a message. It uses the key and the `get_blocks_from_text()` method for the encryption. The method converts the message to a list of block integers, encrypt each block with the key, and export a file with the content.
* `decrypt()`: gets the file name to save the decrypted message and the file with the **private key**. This key must be the pair for the one that encrypted the message, otherwise, it cannot be decrypted. The method converts a message to block integers, decrypt it using the key and using the `get_text_from_blocks()` get the original message and export it to a file.

## The main file

Running the `main.py`, the parameters are the message `This is my secret message`, the block size equals the default value `128` and a key size of `1024`. 
Two files with the keys are created: `diego_public_key.txt` and `diego_private_key.txt`. The file contains the size of the key and the two key pairs in each line.

Using the public key file, the message is encrypted and saved in `encrypted_message.txt`. In the first line, there is the message length. The second one corresponds to the block size of the message. The last one contains the cipher message itself.

In conclusion, the file with the encrypted message is read, and using the private key file it is converted to plaintext and save in `decrypted_encrypted_message.txt`. The file contains only the original message.

