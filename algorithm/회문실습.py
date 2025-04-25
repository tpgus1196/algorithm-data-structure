def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: #닫는 괄호가 많은 경우(닫는 괄호 만났을 때)
                return False
            stack.pop() #짝 맞는 여는 괄호 제거
    return len(stack) == 0 #스택에 남아 있으면 닫지 못한 괄호 있음

print(is_valid_parentheses("()")) #true
print(is_valid_parentheses("(()())")) #true
print(is_valid_parentheses("())(")) #False
print(is_valid_parentheses("(()")) #False
print(is_valid_parentheses(")(")) #False
        
