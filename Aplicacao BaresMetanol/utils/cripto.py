from cryptography.fernet import Fernet

key = b'WpywE3nhdqSN7u7PBK3fl4Q-QxnHFc6S5kPGNC3wGEE='
cipher = Fernet(key)

def encrypt(data):
    cipher_data = cipher.encrypt(data.encode())   # converte data em uma sequ                                       ência de bytes

    return cipher_data


def decrypt(data):
    original_data = cipher.decrypt(data).decode()   #decripta a sequencia de bytes

    return original_data