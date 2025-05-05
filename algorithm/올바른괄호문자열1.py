#스택 다운받아 사용
from collections import deque

s = input()
stack = deque()

for p in s:
    if p == "(":
        stack.append(p)
    elif p == ")":
        if not stack:
            print("NO")
            break
        stack.pop()

#for 루프가 끝날 떄까지 break 없이 실행되면 else블록 실행
#break가 한번이라도 실행되면 else블록 건너뜀
else:  # for문이 break 없이 정상 종료된 경우만 실행
    if not stack:
        print("YES")
    else:
        print("NO")