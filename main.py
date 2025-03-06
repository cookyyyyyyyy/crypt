from RSA.imp_rsa import DCrypt

def menu():
    print("======Menu======")
    print ("1. Decrypt")
    print ("2. Encrypt")


def main():
    while True:
        menu()
        action = input("1 choice: ")

        if action == "1":
            message = input("Message to decrypt : ")
            message = message.encode()
            loc_privkey = input("Locate private key : ")
            pass_privkey = input("passphrase of private key")

            decrypt = DCrypt(privkey_path=loc_privkey, passphrase=pass_privkey)

            decrypted_message = decrypt.decrypt(message)

            print(f"Decrypted message : {decrypted_message}")
        
        elif action == "2":
            message_crypt = input("Message to crypt :")
            loc_pubkey = input("Locate of pub key : ")
            
            crypt = DCrypt(message=message_crypt,pubkey_path=loc_pubkey)

            crypted_message = crypt.encrypt()

            print(f"Encrypted message : {crypted_message}")

if __name__ == '__main__':
    main()
