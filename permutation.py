"Functions for substitution"
import json


def permutation(source, matrix_name):
    with open("des_config.json", "r") as config_file:
        config = json.load(config_file)
    # Read initial permutation matrix from json file
    matrix = config[matrix_name]

    # Substitution of inputs by initial substitution matrices
    output = []
    for row in matrix:
        for colum in row:
            output.append(source[colum - 1])
    return ''.join(output)

