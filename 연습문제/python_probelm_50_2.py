# 53 괄호 올바른지 판단
def check_bracket(l):
    if l.count('(') != l.count(')'):
        return False

    ll = []
    for i in l:
        if('('):
            ll.append('(')
        else:
            if len(ll) == 0:
                return False
            ll.pop()
    return True
l = '(()())'
print(check_bracket(l))

# 54 연속되는 수 인가?
l = [1, 4, 2, 6, 3]
l.sort()
check = True
for i in range(len(l) - 1):
    if l[i] + 1 != l[i + 1]:
        check = False
        break
print(check)

# 55 하노이의 탑 # 다시 풀어보자
route = []
def hanoi(disk_count, start_top, goal_top, help_top):
    if disk_count == 1:
        route.append([start_top, goal_top])
        return None
    hanoi(disk_count - 1, start_top, help_top, goal_top)
    route.append([start_top, goal_top])
    hanoi(disk_count - 1, help_top, goal_top, start_top) 
    return route

print(hanoi(3, 'A', 'C', 'B'))

# 56
nationWidth = {
    'korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England' : 242900 }

w = nationWidth.pop('korea')
print(min(nationWidth, key = lambda x: abs(w - nationWidth.get(x))))

# 57
s = ''
for i in range(1001):
    s += str(i)
print(s.count('1'))
print(str([i for i in range(1001)]).count('1'))
print(str(list(range(1001))).count('1'))
