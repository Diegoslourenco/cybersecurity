# Transposition Cipher Algorithm

In `Transposition Cipher`, instead of replacing the symbols, the plaintext is shifted in a regular system to form the ciphertext. This way the original message becomes unreadable.

The methods for the class `Transposition`:

* `encrypt()` takes a message and a key and returns a cipher message. The key corresponds to the number of `columns` for a table. The number o `rows` depends on the size of the message. The message fills the table from the left to the right, row by row. The spaces in the message are represent as (s). The empty spaces after the end of the message are totally ignored. In the example, the original message is `This is my secret message.`. The cipher message is readed column by column, so for the example it is `Tmtehy .i msse esicssra eg`.
<br>

| 1rs | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|  T  |  h  |  i  |  s  |   (s)  |  i  |  s  | (s)    |
|  m  |  y  |  (s)   |  s  |  e  |  c  |  r  |  e  |
|  t  |  (s)   |  m  |  e  |  s  |  s  |  a  |  g  |
|  e  |  .  |     |     |     |     |     |     |

<br>


* `decrypt()` takes a cipher message and the key and returns the original message.

<br>

* `brute_force()` receives only a cipher message and a language. Using a brute-forte attack it will test all the possible keys and return the result messages in a list that each item corresponds to a pair key and decrypted message. Because there are many possible solutions for this problem, a good way to solve this is that for each possible decrypted message here, check if some words make sense in a given language. For this purpuse, the `detected_language` module was created.

<br>

The functions present in the `detect_language.py`:

* `load_dictionary()` loads a dictionary with the words that could be checked and will be considered valid words.
* `remove_non_letters()` removes all the characters that are not part of a group of symbols.
* `count_language()` receives a text and returns the percentage about how many words from a given language are in a text.
* `check_valid_language()` receives a text and checks if some part of it is in a given language and returns a true or false.

<br>

Running the `main.py` the results for the messages are:
<br>

message = 'This is my secret message.' <br>
message_ptbr = 'Essa é minha mensagem secreta.' <br>

<br>

## Outputs

## **For the english message**

### Encrypted message with key 8 using `encrypt()`:

```sh
Tmtehy .i msse esicssra eg
```

### Decrypted message with the key using `decrypt()`:

```sh
This is my secret message.
```

### All the possibilities whitout the key using `brute_force()` returning the pair key-message value that matches at least 50% words as valid english words:

```sh
[(8, 'This is my secret message.')]
```
<br>

## **For the portuguese message**

### Encrypted message with key 8 using `encrypt()`:

```sh
Eiscsnarshgeaaet  maém . esmne
```

### Decrypted message with the key using `decrypt()`:

```sh
Essa é minha mensagem secreta.
```

### All the possibilities whitout the key using `brute_force()` returning the pair key-message value that matches at least 50% of words as valid portuguese words:

```sh
[   
    (8, 'Essa é minha mensagem secreta.'), (16, 'Essasgae mé  sneicnrheat am.em'), 
    (18, 'Essasgae mé  esmneicnrheat am.'), (19, 'Essasgae mé . esmneicnrheat am'), 
    (20, 'Essasgae mém . esmneicnrheat a')
]
```





