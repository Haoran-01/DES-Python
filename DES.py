"Here is the file for the DES algorithm implementation"
from permutation import permutation
from encryption import round_function
from utils import xor_with_key
from key import key_generation


def encryption(plain_text, master_key):
    # initial permutation
    data = permutation(plain_text, "IP")

    # Generate subkeys
    keys = key_generation(master_key)

    # Perform 16 rounds of iterations
    for round_num in range(16):
        left_half = data[:32]
        right_half = data[32:]

        new_left_half = right_half
        # Calling Wheel Functions
        new_right_half = xor_with_key(left_half, round_function(right_half, keys[round_num]))

        data = new_left_half + new_right_half

        # Swap the left and right parts for the last time
        if round_num == 15:
            data = new_right_half + new_left_half

    # Perform inverse initial conversion
    cipher_text = permutation(data, "IP-1")

    return cipher_text


def decryption(cipher_text, master_key):
    # Using the IP-1 substitution matrix
    data = permutation(cipher_text, "IP")

    # Get subkey
    keys = key_generation(master_key)

    # Inverse 16 iterations
    for round_num in range(16):
        left_half = data[:32]
        right_half = data[32:]

        new_left_half = right_half
        # Calling Wheel Functions
        new_right_half = xor_with_key(left_half, round_function(right_half, keys[15 - round_num]))

        data = new_left_half + new_right_half

        # Swap the left and right parts for the last time
        if round_num == 15:
            data = new_right_half + new_left_half

    # Perform inverse initial conversion
    plain_text = permutation(data, "IP-1")

    return plain_text

