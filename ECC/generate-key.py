from Crypto.PublicKey import ECC

def export_privkey(privkey, filename):
    with open(filename, "wt") as file:
        pwd = b'secret' #I know i know
        key_data = privkey.export_key(format='PEM',
                                passphrase=pwd,
                                protection='PBKDF2WithHMAC-SHA512AndAES256-CBC',
                                prot_params={'iteration_count':131072})
        file.write(key_data)

def export_pubkey(pubkey, filename):
    with open(filename, "wt") as file:
        key_data = pubkey.export_key(format='PEM')
        file.write(key_data)

Keypair = ECC.generate(curve='p256')
pub_Keypair = Keypair.public_key()

export_privkey(Keypair, 'priv_key.pem')
export_pubkey(pub_Keypair, 'pub_key.pem')