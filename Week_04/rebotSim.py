# https://leetcode-cn.com/problems/walking-robot-simulation/

def rebotSim(commands, obstacles):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = di = 0
    dic = {}
    for c in obstacles:
        dic[tuple(c)] = True
    res = 0
    for cmd in commands:
        if cmd == -2:#left
            di = (di - 1) % 4
        elif cmd == -1:#right
            di = (di + 1) % 4
        else:
            for _ in range(cmd):
                if (x+dx[di], y+dy[di]) not in dic:
                    x += dx[di]
                    y += dy[di]
                    res = max(res, x * x + y * y)
    return res