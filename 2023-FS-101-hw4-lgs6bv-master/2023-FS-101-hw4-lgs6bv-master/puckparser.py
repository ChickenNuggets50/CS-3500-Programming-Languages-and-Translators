#Lincoln Steber

token = ""
line = []
index = 0
error = False

def get_input():
    global line
    global index
    index = 0
    line = input().split()


def get_token():
    global token
    global index
    global line
    if index < len(line):
        token = line[index]
        index += 1


def is_Integer(s: str) -> bool:
    i: int = 0
    state: int = 0

    while i < len(s):
        if state == 0:
            if s[i] == '+' or s[i] == '-':
                state = 0
            elif s[i].isdigit():
                state = 1
            else:
                return False
        elif state == 1:
            if s[i].isdigit():
                state = 1
            else:
                return False
        i += 1

    if state != 1:
        return False

    return True


def is_Decimal(s: str) -> bool:
    parts = s.split(".")
    # may need to check for len(parts) > 1
    if len(parts) > 2:
        return False

    if is_Integer(parts[0]):
        ic(parts)
        if len(parts) > 1:
            if is_Integer(parts[1]):
                return True

    return False


def is_String(s: str) -> bool:
    state: int = 0
    i: int = 1

    if s[0] == '"':
        for char in s:
            if (char.isspace()):
                return False

    if s[-1] == '"':
        return True

    return False


def is_Keyword(s: str) -> bool:
    return s in ["WRITE", ".", "[", "]", "(", ")", ";"]


def is_Operator(s: str) -> bool:
    return s in [":=", "~", "<", ">", "=", "#", "+", "-", "&", "OR", "*", "/", "AND"]


def is_Identifier(s: str) -> bool:
    return s[0].isalpha() and not is_Keyword(s)


def is_Relation():
    global token
    global error
    if token in ["<", ">", "=", "#"]:
        get_token()
    else:
        error = True
        print("Invalid!")
        print("Error: Expected Relation ☜(ಠ_ಠ☜)")


def is_AddOpperator():
    global token
    global error
    if token in ["+", "-", "&", "OR"]:
        get_token()
    else:
        error = True
        print("Invalid!")
        print("Error: Expected AddOperator ☜(ಠ_ಠ☜)")


def is_MulOperator():
    global token
    global error
    if token in ["*", "/", "AND"]:
        get_token()
    else:
        error = True
        print("Invalid!")
        print("Error: Expected MulOperator ☜(ಠ_ಠ☜)")


def is_SimpleExpression():
    is_Term()
    while token in ["+", "-", "OR", "&"]:
        get_token()
        is_Term()


def is_Term():
    is_Factor()
    while token in ["*", "/", "AND"]:
        is_MulOperator()
        is_Factor()


def is_Expression():
    is_SimpleExpression()
    if token in ["<", ">", "=", "#"]:
        get_token()
        is_SimpleExpression()


def is_Factor():
    global token
    global error
    if is_Integer(token):
        get_token()
    elif is_Decimal(token):
        get_token()
    elif is_String(token):
        get_token()
    elif is_Identifier(token):
        get_token()
    elif error == True:
        return
    elif token == "(":
        get_token()
        is_Expression()
        if token == ")":
            get_token()
        else:
            error = True
            print("Invalid!")
            print("Error: Expected ) (눈_눈) ")
            return
    elif token == "~":
        get_token()
        is_Factor()
    else:
        error = True
        print("Invalid!")
        print("Error: Expected Factor (>_<)")
        return


def is_Selector():
    global token
    global error
    if token == ".":
        get_token()
        if is_Identifier(token):
            get_token()
        else:
            error = True
            print("Invalid!")
            print("Error: Expected Identifier after . (¬_¬)")
    elif token == "[":
        get_token()
        is_Expression()
        if token == "]":
            get_token()
        else:
            error = True
            print("Invalid!")
            print("Error: Expected ] (¬_¬)")
    else:
        error = True
        print("Invalid!")
        print("Error: Expected . or [ (¬_¬)")

def is_Designator():
    global error
    global token
    if is_Identifier(token):
        get_token()
        while token == "." or token == "[":
            is_Selector()
    else:
        error = True
        print("Invalid!")
        print("Error: Expected Identifier (¬_¬)")

def is_Assignment():
    global error
    is_Designator()
    if token == ":=":
        get_token()
        is_Expression()
    else:
        error = True
        print("Invalid!")
        print('Error: ":=" expected, got ' + '"' + token + '"')

def is_WriteStatement():
    global token
    global error
    if token == "WRITE":
        get_token()
        if token == "(":
            get_token()
            is_Expression()
            if token == ")":
                get_token()
            else:
                error = True
                print("Invalid!")
                print("Error: Expected )")
        else:
            error = True
            print("Invalid!")
            print("Error: Expected (")
    else:
        error = True
        print("Invalid!")
        print("Error: Expected WRITE  (ಠ ∩ ಠ) ")

def is_Statement():
    global error
    if is_Identifier(token):
        is_Assignment()
    elif token == "WRITE":
        is_WriteStatement()
    else:
        error = True
        print("Invalid!")
        print("Error: Expected Statement (╯°□°)╯︵ ┻━┻")

def is_StatementSequence():
    is_Statement()
    while token == ";":
        get_token()
        is_Statement()

if __name__ == "__main__":

    while error != True:
        get_input()
        if ";" not in line:
            get_token()
            is_Statement()
            break
        get_token()
        is_Statement()
    if error == False:
        print("CORRECT")

