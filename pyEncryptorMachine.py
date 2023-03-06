# This is Encryption Machine

# Import necessary modules
import random as r
import string

# Define key for encryption
# key string is a combination of letters, numbers and symbols
key = string.ascii_letters + string.digits + " !@#$%^&*()"

# Define a random index in the key length
randomizer = r.randint(0, len(key) - 1)

# Define a random value function with the random index and the key
def random_value(key, randomizer):
    value = key[randomizer] + key[randomizer + 1 :] + key[:randomizer]
    return value

# define a dictionary for encryption
encrypt_dict = dict(zip(key, random_value(key, randomizer)))

# Define a decryption dictionary
decrypt_dict = dict(zip(random_value(key, randomizer), key))

# Encoding a password
# This function will be used to encrypt a password.
def encode_password(password):
    encoded_password = ""
    for char in password:
        encoded_password += encrypt_dict[char]
    with open("encryptor_machine.key", "a") as f:
        f.write(encoded_password + "|" + str(randomizer) + "\n")
    return encoded_password

# Decoding a password
# This function will be used to decrypt a password.
def decode_password(password):
    with open("encryptor_machine.key", "r") as f:
        list_of_lines = f.readlines()
        for lines in list_of_lines:
            if password in lines:
                decodex, randx = lines.rstrip().split("|")
                break
    decoded_password = ""
    decrypt_dict = dict(zip(random_value(key, int(randx)), key))
    for char in decodex:
        decoded_password += decrypt_dict[char]
    return decoded_password
# This is the end of the Encryption Machine