"这个文件内主要是一些辅助函数，来帮助程序进行计算"


# Decimal to binary conversion
def binary_conversion(decimal_number):
    binary_number = bin(int(decimal_number))[2:]
    return binary_number


# Binary to decimal conversion
def decimal_conversion(binary_number):
    decimal_number = str(int(binary_number, 2))
    return decimal_number


# different-or operation
def xor_with_key(source, the_key):
    # performs the different-or operation
    result = ""
    for i in range(len(source)):
        # Different-or each bit of data and key
        if source[i] != the_key[i]:
            result += "1"
        else:
            result += "0"
    return result


# Preprocessing of input strings
def processing_string(string):
    process_string = ''.join(format(ord(char), '08b') for char in string)

    strings = []

    # When the string is less than 64 bits
    if len(process_string) < 64:
        # complement
        padding_length = 64 - len(process_string) % 64

        # Supplemented with 64-bit
        if padding_length != 0:
            process_string = padding_length * "0" + process_string
        strings.append(process_string)
    else:
        # When the string is greater than or equal to 64-bit
        # Need to add the section
        padding_length = len(process_string) % 64

        # Supplemented with 64 integer multiples
        if padding_length != 0:
            process_string = (64 - padding_length) * "0" + process_string

        strings = [process_string[i:i + 64] for i in range(0, len(process_string), 64)]

    return strings


# Convert binary numbers to text
def string_transform(binary_data):
    string_data = ''.join(chr(int(binary_data[i:i + 8], 2)) for i in range(0, len(binary_data), 8))
    # string_data = string_data.replace('\0', '')
    string_data = string_data.lstrip('\0')
    return string_data

