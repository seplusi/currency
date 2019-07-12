"""
    File with loose functions that will be used several times
"""

def convert_string_float_into_integer(number_str):
    """
        Receives a string with a float and shifts the decimal number to the left so it becomes an integer
        Ex: 123.456 -> 123456

    :param number_str: String with a float
    :return: Integer with all digits moved to the left
    """
    if ',' in number_str:
        thousands = int(number_str.split(',')[0])
    else:
        thousands = 0

    remain = number_str.split(',')[-1]
    units = int(remain.split('.')[0])
    decimals = remain.split('.')[1]
    multiplier = pow(10, len(decimals))

    return thousands * multiplier * 1000 + units * multiplier + int(decimals), multiplier
