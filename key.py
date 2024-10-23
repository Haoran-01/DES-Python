"This file is about the iterative generation of k-value"
import json

from permutation import permutation


# Subkey generation function
def key_generation(key):
    # Call the hash function
    hashed_key = custom_hash_key_to_64_bits(key)

    # Display the hash result as a binary string
    hashed_key_binary = ''.join(format(byte, '08b') for byte in hashed_key)

    key = hashed_key_binary
    # Read the iteration left shift count data
    with open("des_config.json", "r") as config_file:
        config = json.load(config_file)

    left_shift = config["Iterative shift left"]

    keys = []
    # Replacement option PC1
    calculate_key = permutation(key, "PC1")
    for iteration in range(16):
        # Iterative left shift
        c = calculate_key[:28]
        d = calculate_key[28:]

        left_shift_number = left_shift[iteration]
        left_part = c[left_shift_number:] + c[:left_shift_number]
        right_part = d[left_shift_number:] + d[:left_shift_number]

        # Combining left and right parts
        shifted_key = left_part + right_part

        # Replacement option PC2
        output_key = permutation(shifted_key, "PC2")

        # iterative assignment
        calculate_key = shifted_key

        # Storing the subkey
        keys.append(output_key)
    return keys


import hashlib


def custom_hash_key_to_64_bits(key):
    # SHA-256 hash it, then extend the hash to 64-bit binary numbers.
    sha256 = hashlib.sha256()
    sha256.update(key.encode('utf-8'))
    hashed_key = sha256.digest()

    # If the length of the hash result is less than 64 bits,
    # fill its left side with zeros until it reaches 64 bits
    if len(hashed_key) < 8:
        padded_hash = b'\x00' * (8 - len(hashed_key)) + hashed_key
    else:
        padded_hash = hashed_key[:8]

    return padded_hash

