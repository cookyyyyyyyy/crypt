from Crypto.PublicKey import ECC
import getpass

def import_privkey(filename):
    pwd = getpass.getpass("Enter the password of the private key : ").encode()
    with open(filename, "rt") as file:
        privkey = file.read()
        return ECC.import_key(privkey, passphrase=pwd)

def import_pubkey(filename):
    with open(filename, "rt") as file:
        pubkey = file.read()
        return ECC.import_key(pubkey)
    
