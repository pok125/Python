# 다시 보자 : 53, 55 64, 66, 67, 69
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

# 58
money = 123456789
result = format(money, ',')
print(result)

# 59
s = 'hi'
print(s.center(50, '='))
print(f'{s:=^50}')

# 60
student = ['강은지','김유정','박현서','최성훈','홍유진','박지호','권윤일','김채리','한지호','김진이','김민호','강채연']
student.sort()
for num, name in enumerate(student, 1):
    print(f'번호: {num}, 이름: {name}')

# 61 정규표현식  사용해보기
s = 'aaabbbbcdddd'
ss = set(s)
for i in ss:
    print(f'{i}{s.count(i)}')

# 62 20190923출력하기 문제 이해를 잘 못했음
string='aacddddddddd'
a=string.count('a') #2
b=string.count('b') #0
c=string.count('c') #1
d=string.count('d') #9
print(int(str(a)+str(b)+str(c)+str(d)+str(b)+str(d)+str(a)+str(a+1)))

# 63
string = '복잡한 세상 편하게 살자'
print(list(map(lambda x:x[0], string.split(' '))))

# 64 최적의 kg찾기
N = 24
result = 0

while True:
    if N % 7 == 0:
        result += N // 7
        print(result)
        break
    N -= 3
    result += 1
    if N < 0:
        print(-1)
        break
# 65
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
l = []
for i in range(len(a)):
    if i % 2 == 0:
        l.append([a[i], b[i]])
    else:
        l.append([b[i], a[i]])
print(l)

# 66 블록검사
def solution(block_list, rule):
    answer = []
    for blocks in block_list:
        answer.append(check_block_order(blocks, rule))
    return answer

def check_block_order(blocks, rule):
    cur_rule = 0
    for i in blocks:
        if i in rule:
            if cur_rule > rule.index(i):
                return 'impossible'
            cur_rule = rule.index(i)
    return 'possible'

top = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
rule = "ABD"
print(solution(top, rule))

# 67 악수
handshake_count = 59
total_count = 0
people_count = 2

while total_count <= handshake_count:
    total_count = sum(range(1, people_count)) # n*(n-1)/2
    people_count += 1

people_count -= 1

print(people_count - (total_count - handshake_count) - 1)

# 68
def sub_time(time1, time2):
    l1 = list(map(int, time1.split(':')))
    l2 = list(map(int, time2.split(':')))

    total_time1_minute = l1[0] * 60 + l1[1]
    total_time2_minute = l2[0] * 60 + l2[1]
    if total_time2_minute < total_time1_minute:
        return '지나갔습니다'

    hour = (total_time2_minute - total_time1_minute) // 60
    minute = (total_time2_minute - total_time1_minute) % 60
    print(hour, minute)
    return f'{hour:0>2}시간 {minute:0>2}분'
bus_schedule = ['12:30', '13:20', '14:13']
cur_time = '12:40'
print(sub_time(cur_time, bus_schedule[1]))

# 69 골드바흐의 추측
n = 100
def prime_nums(x):
    j = 2
    l = []
    
    for i in range(2, x + 1):
        j = 2
        while j ** 2 <= i:
            if i % j == 0:   
                break
            j += 1
        else:
            l.append(i)
    return l
prime_list = prime_nums(100)
for i in range(len(prime_list)):
    for j in range(len(prime_list) - 1, i, -1):
        if prime_list[i] + prime_list[j] == n:
            print(f'{prime_list[i]} + {prime_list[j]} == {n}')
# 더 나은 코드
# for i in range(2, n//2+1):    
#     if i in a and n-i in a:
#         l.append(i)
#         l.append(n-i)

