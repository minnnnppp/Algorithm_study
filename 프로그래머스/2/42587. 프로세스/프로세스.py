from collections import deque
def solution(priorities, location):
    idx = deque(range(0, len(priorities)))
    priorities = deque(priorities)
    cnt = 0
    break_bool = False

    while True:
        x = priorities.popleft()
        y = idx.popleft()
        if priorities:
            if max(priorities) < x or max(priorities) == x:
                cnt += 1
                if y == location:
                    return cnt
            else:
                priorities.append(x)
                idx.append(y)
        else:
            return cnt+1    