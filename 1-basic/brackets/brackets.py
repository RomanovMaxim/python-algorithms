# Проверить правильность расстановки скобок

def equal_type_brackets(char1, char2):
    if char1 == '(' and char2 == ')' or char1 == '[' and char2 == ']' or char1 == '{' and char2 == '}':
        return True
    return False

def check_brackets(string):
    stack = []
    index = []
    for i in range(len(string)):
        ch = string[i]
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
            index.append(i)
        elif ch == ')' or ch == ']' or ch == '}':
            index.pop()
            if not equal_type_brackets(stack.pop(), ch):
                return str(i + 1)
    if stack:
        return str(index[0] + 1)
    return "Success"

if __name__ == '__main__':
    string = input()
    print(check_brackets(string))
