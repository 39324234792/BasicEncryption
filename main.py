decrypted = b"abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]{}\|;:'\"<>?/.,~` "
encrypted = b"m6bha\",.;/|{&*y3knjuitfg14785^credpo+_-=]09l(2v)xswqz#%$@!><[}:'\~`? "

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

choice = input("1 to decrypt, 2 to encrypt or 0 to quit program\n ")
if choice == '0':
    quit()

elif choice == '1':
    message = input('Enter message for encryption: ')
    result = message.translate(encrypt_table)
    print(result)

elif choice == '2':
    print('Enter message to decrypt: ')
    message = input()
    result = message.translate(decrypt_table)
    print(result)

elif choice != '0':
    print('There was a mess up')
