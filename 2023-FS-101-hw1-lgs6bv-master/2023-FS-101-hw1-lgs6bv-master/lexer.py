# Lincoln Steber
# My First Lexical Analyser


def is_valid_int(string):
    state = 0
    valid_digits = set("0123456789")
    for c in string:
        if state == 0:
            if c == "+" or c == "-":
                state = 1
            elif c in valid_digits:
                state = 2
            else:
                state = 3
        elif state == 1:
            if c in valid_digits:
                state = 2
            else:
                state = 3
        elif state == 2:
            if c in valid_digits:
                state = 2
            else:
                state = 3

    if state == 2:
        return True
    else:
        return False


def is_valid_decimal(string):
    state = 0
    valid_digits = set("0123456789")

    for c in string:
        if state == 0:
            if c == "+" or c == "-":
                state = 1
            elif c in valid_digits:
                state = 2
            else:
                state = 5
        elif state == 1:
            if c in valid_digits:
                state = 2
            else:
                state = 5
        elif state == 2:
            if c in valid_digits:
                state = 2
            elif c == ".":
                state = 3
            else:
                state = 5
        elif state == 3:
            if c in valid_digits:
                state = 4
            else:
                state = 5
        elif state == 4:
            if c in valid_digits:
                state = 4
            else:
                state = 5

    if state == 4:
        return True
    else:
        return False


def is_valid_scientific(string):
    state = 0
    valid_digits = set("123456789")
    parts = string.split("E")

    if is_valid_decimal(parts[0]):
        scientific_string = "E" + parts[1]
        for c in scientific_string:
            if state == 0:
                if c == "E":
                    state = 1
                else:
                    state = 4
            elif state == 1:
                if c in valid_digits:
                    state = 3
                elif c == "+" or c == "-":
                    state = 2
                else:
                    state = 4
            elif state == 2:
                if c in valid_digits:
                    state = 3
                elif c == "0":
                    state = 2
                else:
                    state = 4
            elif state == 3:
                if c in valid_digits:
                    state = 3
                elif c == "0":
                    state = 3
                else:
                    state = 4

    if state == 3:
        return True
    else:
        return False


def is_valid_hexadecimal(string):
    state = 0
    valid_hex_chars = set("0123456789ABCDEF")

    for c in string:
        if state == 0:
            if c in valid_hex_chars:
                state = 1
            else:
                state = 3
        elif state == 1:
            if c in valid_hex_chars:
                state = 1
            elif c == "H":
                state = 2
            else:
                state = 3
        elif state == 2:
            state = 3

    if state == 2:
        return True
    else:
        return False


def is_keyword(string):
    state = 0
    for c in string:
        if state == 0:
            if c == "P":
                state = 1
            elif c == "I":
                state = 16
            elif c == "F":
                state = 18
            elif c == "L":
                state = 20
            else:
                state = 24

        elif state == 1:
            if c == "R":
                state = 2
            elif c == "O":
                state = 13
            else:
                state = 24

        elif state == 2:
            if c == "O":
                state = 3
            elif c == "I":
                state = 10
            else:
                state = 24

        elif state == 3:
            if c == "C":
                state = 4
            else:
                state = 24

        elif state == 4:
            if c == "E":
                state = 5
            else:
                state = 24

        elif state == 5:
            if c == "D":
                state = 6
            else:
                state = 24

        elif state == 6:
            if c == "U":
                state = 7
            else:
                state = 24

        elif state == 7:
            if c == "R":
                state = 8
            else:
                state = 24

        elif state == 8:
            if c == "E":
                state = 9
            else:
                state = 24

        elif state == 10:
            if c == "N":
                state = 11
            else:
                state = 24

        elif state == 11:
            if c == "T":
                state = 12
            else:
                state = 24

        elif state == 13:
            if c == "O":
                state = 14
            else:
                state = 24

        elif state == 14:
            if c == "L":
                state = 15
            else:
                state = 24

        elif state == 16:
            if c == "F":
                state = 17
            else:
                state = 24

        elif state == 18:
            if c == "I":
                state = 19
            else:
                state = 24

        elif state == 20:
            if c == "O":
                state = 21
            else:
                state = 24

        elif state == 21:
            if c == "O":
                state = 22
            else:
                state = 24

        elif state == 22:
            if c == "P":
                state = 23
            else:
                state = 24

        else:
            state = 24

    if (
        state == 9
        or state == 12
        or state == 15
        or state == 17
        or state == 19
        or state == 23
    ):
        return True
    else:
        return False


def is_valid_string_literal(string):
    state = 0
    invalid_digits = set(' "')
    for c in string:
        if state == 0:
            if c == '"':
                state = 1
            else:
                state = 3
        elif state == 1:
            if c not in invalid_digits:
                state = 1
            elif c == '"':
                state = 2
            else:
                state = 3
        else:
            state = 3

    if state == 2:
        return True
    else:
        return False


def is_valid_character_literal(string):
    state = 0
    valid_hex_chars = set("0123456789ABCDEF")
    for c in string:
        if state == 0:
            if c in valid_hex_chars:
                state = 1
            else:
                state = 4
        elif state == 1:
            if c in valid_hex_chars:
                state = 2
            else:
                state = 4
        elif state == 2:
            if c == "X":
                state = 3
            else:
                state = 4
        else:
            state = 4

    if state == 3:
        return True
    else:
        return False


def is_valid_identifier(string):
    state = 0
    valid_letters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    valid_chars = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_")
    for c in string:
        if state == 0:
            if c in valid_letters:
                state = 1
            else:
                state = 2
        elif state == 1:
            if c in valid_chars:
                state = 1
            else:
                state = 2
        else:
            state = 2

    if state == 1:
        return True
    else:
        return False


def get_input(num: int) -> list:
    inputs = []
    for _ in range(num):
        inputs.append(input())
    return inputs


def print_output(num: int, outputs: list):
    print(num)
    for i in range(len(outputs)):
        print(str(i + 1) + ":", outputs[i])


def lexical_Analyser(outputs: list) -> list:
    for i in range(len(outputs)):
        if is_valid_int(outputs[i]):
            outputs[i] = "Integer"

        elif is_valid_decimal(outputs[i]):
            outputs[i] = "Decimal"

        elif is_valid_scientific(outputs[i]):
            outputs[i] = "Scientific"

        elif is_valid_hexadecimal(outputs[i]):
            outputs[i] = "Hexadecimal"

        elif is_keyword(outputs[i]):
            outputs[i] = "Keyword"

        elif is_valid_string_literal(outputs[i]):
            outputs[i] = "String"

        elif is_valid_character_literal(outputs[i]):
            outputs[i] = "Character"

        elif is_valid_identifier(outputs[i]):
            outputs[i] = "Identifier"

        else:
            outputs[i] = "INVALID!"

    return outputs


if __name__ == "__main__":
    num_input = int(input())
    lexems = get_input(num_input)
    lexems = lexical_Analyser(lexems)
    print_output(num_input, lexems)
