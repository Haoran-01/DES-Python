"This file is used to handle data processing for each set of S-boxes"
import json
import utils


def s_box_compression(bits, s_box_name):
    if len(bits) != 6:
        raise ValueError("Input bits must be 6 bits long")
    with open("des_config.json", "r") as config_file:
        config = json.load(config_file)

    # Read the corresponding s box
    s_box = config[s_box_name]

    # Calculate the number of rows and columns obtained
    row = utils.decimal_conversion(bits[0] + bits[5])
    col = utils.decimal_conversion(bits[1:5])

    # Corresponding figures obtained against the S box table
    s_box_value = s_box[int(row)][int(col)]
    output = utils.binary_conversion(s_box_value)

    # Fill operation when converted to a binary number with less than four bits
    if len(output) != 4:
        padding_length = 4 - len(output)
        output = "0" * padding_length + output
    return output
