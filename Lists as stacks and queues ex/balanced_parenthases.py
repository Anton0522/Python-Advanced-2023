from collections import deque

paranthases = deque(input())

open_parenthases = deque()

while paranthases:
    current_paranthases = paranthases.popleft()
    if current_paranthases in "([{":
        open_parenthases.append(current_paranthases)
    elif not open_parenthases:
        print("NO")
        break
    else:
        if f'{open_parenthases.pop() + current_paranthases}' not in "(){}[]":
            print("NO")
            break
else:
    print("YES")