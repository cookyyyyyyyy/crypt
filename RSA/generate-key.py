from Crypto.PublicKey import RSA

def export_privkey(privkey, filename):
    with open(filename, "wb") as file:
        file.write(privkey.export_key(format='PEM',
                                      passphrase='MyPassPhrase', #yeah, i know...
                                      protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                                      prot_params={'iteration_count':131072}))
        file.close()

def export_pubkey(pubkey, filename):
    with open(filename, "wb") as file:
        file.write(pubkey.export_key())
        file.close()

Keypair = RSA.generate(3072)
pub_Keypair = Keypair.publickey()

export_privkey(Keypair, 'priv_key.pem')
export_pubkey(pub_Keypair, 'pub_key.pem')
