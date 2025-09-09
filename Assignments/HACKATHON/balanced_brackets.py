def isbalanced(s):
    stack = []
    for i in s:
        if i in ["(", "{", "["]:
            stack.append(s)
        else:
            if not stack:
                return False

            curr_char = stack.pop()

            if curr_char == '(' and i != ")":
                return False
            if curr_char == '{' and i != "}":
                return False
            if curr_char == '[' and i != "]":
                return False

    return not stack
print(isbalanced("{}["))
print(isbalanced("{}"))
print(isbalanced("[]{}"))



