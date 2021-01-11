# Transposition Cipher Algorithm

Running the `main.py` the results for the messages are:
<br>

message = 'This is my secret message' <br>
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





