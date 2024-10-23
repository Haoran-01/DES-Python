"This file is the part that is encrypted during DES iterations, including the wheel function"

from substitution_boxes import s_box_compression
from permutation import permutation
from utils import xor_with_key


def extended(source):
    # E Expansion to expand 32bit data to 48bit
    output = permutation(source, "e_matrix")
    return output


def substitution(source):
    output = ""
    # Divided into 8 parts, s-box compressed
    data_blocks = [source[i:i + 6] for i in range(0, 48, 6)]
    for i, block in enumerate(data_blocks):
        output += s_box_compression(block, f"S{i + 1}")
    return output


def round_function(source, iterations_key):
    extend_source = extended(source)
    # Compute with key value
    result = xor_with_key(extend_source, iterations_key)
    # Perform S-box compression
    result = substitution(result)
    # carry out P-substitution
    output = permutation(result, "P")
    return output
