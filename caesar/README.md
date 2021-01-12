# Caesar Cipher Algorithm

In `Caesar Cipher` each symbol in a given message, usually called plaintext, is replaced by a symbol some fixed number of position down of some group of symbols. This fixed number is called `key`. For example, according to the group of `symbols` below and a key equal to 3, the D would be replaced by G, E would become H, and so on. The method is a reference to Julius Caesar, who used it in his private correspondence.

The methods for the class `Caesar`:
* `encrypt()` takes a text and a key and returns a cipher message.
* `decrypt()` takes a cipher message and a key and returns the original message.
* `brute_force()` receives only a cipher message. Using a brute-forte attack it tests all the possible keys and return the result messages in a list that each item corresponds to a pair key and decrypted message.

Running the `main.py`, the results for this message and symbols are:
<br>

message = 'This is my secret message' <br>
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz "

<br>

## Outputs

### Encrypted message with key 13 using `encrypt()`:

```sh
guvFMvFM KMFrpErGM rFFntr
```

### Decrypted message with the key using `decrypt()`:

```sh
This is my secret message
```

### All the possibilities whitout the key using `brute_force()` returning the pair key-message value and the correct one:

```sh
[   (0, 'guvFMvFM KMFrpErGM rFFntr'),  (1, 'ftuELuELzJLEqoDqFLzqEEmsq'),  (2, 'estDKtDKyIKDpnCpEKypDDlrp'), 
    (3, 'drsCJsCJxHJComBoDJxoCCkqo'),  (4, 'cqrBIrBIvGIBnlAnCIvnBBjpn'),  (5, 'bpqAHqAHuFHAmk mBHumAAiom'),
    (6, 'aop Gp GtEG ljzlAGtl  hnl'),  (7, 'ZnozFozFsDFzkiyk Fskzzgmk'),  (8, 'YmnyEnyErCEyjhxjzErjyyflj'), 
    (9, 'XlmxDmxDqBDxigviyDqixxeki'),  (10, 'WklvClvCpACvhfuhxCphvvdjh'), (11, 'VjkuBkuBo BugetgvBoguucig'), 
    (12, 'UijtAjtAnzAtfdsfuAnfttbhf'), (13, 'This is my secret message'), (14, 'SghrzhrzlxzrdbqdszldrrZfd'), 
    (15, 'RfgqygqykvyqcapcrykcqqYec'), (16, 'QefpxfpxjuxpbZobqxjbppXdb'), (17, 'PdeoveovitvoaYnapviaooWca'), 
    (18, 'OcdnudnuhsunZXmZouhZnnVbZ'), (19, 'NbcmtcmtgrtmYWlYntgYmmUaY'), (20, 'MablsblsfqslXVkXmsfXllTZX'), 
    (21, 'LZakrakreprkWUjWlreWkkSYW'), (22, 'KYZjqZjqdoqjVTiVkqdVjjRXV'), (23, 'JXYipYipcnpiUShUjpcUiiQWU'), 
    (24, 'IWXhoXhobmohTRgTiobThhPVT'), (25, 'HVWgnWgnalngSQfShnaSggOUS'), (26, 'GUVfmVfmZkmfRPeRgmZRffNTR'), 
    (27, 'FTUelUelYjleQOdQflYQeeMSQ'), (28, 'ESTdkTdkXikdPNcPekXPddLRP'), (29, 'DRScjScjWhjcOMbOdjWOccKQO'), 
    (30, 'CQRbiRbiVgibNLaNciVNbbJPN'), (31, 'BPQahQahUfhaMKZMbhUMaaIOM'), (32, 'AOPZgPZgTegZLJYLagTLZZHNL'), 
    (33, ' NOYfOYfSdfYKIXKZfSKYYGMK'), (34, 'zMNXeNXeRceXJHWJYeRJXXFLJ'), (35, 'yLMWdMWdQbdWIGVIXdQIWWEKI'), 
    (36, 'xKLVcLVcPacVHFUHWcPHVVDJH'), (37, 'vJKUbKUbOZbUGETGVbOGUUCIG'), (38, 'uIJTaJTaNYaTFDSFUaNFTTBHF'), 
    (39, 'tHISZISZMXZSECRETZMESSAGE'), (40, 'sGHRYHRYLWYRDBQDSYLDRR FD'), (41, 'rFGQXGQXKVXQCAPCRXKCQQzEC'), 
    (42, 'qEFPWFPWJUWPB OBQWJBPPyDB'), (43, 'pDEOVEOVITVOAzNAPVIAOOxCA'), (44, 'oCDNUDNUHSUN yM OUH NNvB '), 
    (45, 'nBCMTCMTGRTMzxLzNTGzMMuAz'), (46, 'mABLSBLSFQSLyvKyMSFyLLt y'), (47, 'l AKRAKREPRKxuJxLRExKKszx'), 
    (48, 'kz JQ JQDOQJvtIvKQDvJJryv'), (49, 'jyzIPzIPCNPIusHuJPCuIIqxu'), (50, 'ixyHOyHOBMOHtrGtIOBtHHpvt'), 
    (51, 'hvxGNxGNALNGsqFsHNAsGGous')
]
```

```sh
(13, 'This is my secret message')

```





