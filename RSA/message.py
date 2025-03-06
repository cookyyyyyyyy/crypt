from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class DCrypt():
    def __init__(self, message=None, privkey_path=None, pubkey_path=None, passphrase=None):
        self.message = message
        self.privkey_path = privkey_path
        self.pubkey_path = pubkey_path
        self.passphrase = passphrase
    
    def import_privkey(self):
        with open(self.privkey_path, "rb") as file:
            privkey = RSA.importKey(file.read(), passphrase=self.passphrase)
        return privkey
    
    def import_pubkey(self):
        with open(self.pubkey_path, "rb") as file:
            pubkey = RSA.importKey(file.read())
        return pubkey
    
    def encrypt(self):
        if isinstance(self.message, str):
            self.message = self.message.encode()

        keypub_encrypt = PKCS1_OAEP.new(self.import_pubkey())
        encrypted_message = keypub_encrypt.encrypt(self.message)
        return encrypted_message.hex()

    def decrypt(self, encrypted_message):
        if isinstance(encrypted_message, bytes):
            encrypted_message = encrypted_message.decode('utf-8')

        encrypted_message_byte = bytes.fromhex(encrypted_message)

        keypub_decrypt = PKCS1_OAEP.new(self.import_privkey())
        decrypted_message = keypub_decrypt.decrypt(encrypted_message_byte)

        return decrypted_message.decode('utf-8')
