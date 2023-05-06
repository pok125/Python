# 1
nums = [100, 200, 300, 400, 500]
nums.remove(400)
nums.remove(500)

# 2
l = [200, 100, 300]
l.insert(2, 10000)

# 8 
d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
# print(d['weight']) # 84

# 9 
year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

# print(year, month, day, sep = '/', end=' ')
# print(hour, minute, second, sep = ':')

# 10
# input_count = int(input())
# star = '*'
# for i in range(1, input_count * 2, 2):
    # print((star * i).center(input_count * 2))

# n = int(input())
# for i in range(1, n + 1):
	# print(" " * (n - i) + ("*" * (2 * i - 1)))

# 28
l = 'Python'
for i in range(len(l) - 1):
    print(l[i : i + 2])
    # print(l[i], l[i + 1], sep='')

# 30
l = 'pineapple is yummy'
print(l.find('apple'))

# 33
l = ['1', '2', '3', '4', '5']
print(l[::-1])

#35
def one(n):
    def two(x):
        return x ** n
    return two

a = one(2)
b = one(3)
c = one(4)
print(a(10))
print(b(10))
print(c(10))

# 37
l = ['원범', '원범', '혜원', '혜원', '혜원', '혜원', '유진', '유진']
seleted_name = ''
count = 0
temp = 0
for i in set(l):
    temp = l.count(i)
    if count < temp:
        seleted_name = i
        count = temp

print(f'{seleted_name}(이)가 총 {count}표로 반장이 되었습니다.')

# 38
scores = [97, 86, 75, 66, 55, 97, 85, 97, 97, 95]
top3_socores = [i for i in sorted(set(scores), reverse=True)]

candy_count = 0
for i in range(0, 3):
    candy_count += scores.count(top3_socores[i])

print(candy_count)

# 39
l1 = 'hqllo my bamq is hyqwob'
l1 = l1.translate(str.maketrans('qb', 'en'))
# l1 = l1.translate(str.maketrans({'q':'e', 'b':'n'}))
print(l1)

# 41 (소수 판별)

# 42
import datetime
print(datetime.date(year = 2020, month = 5, day = 24).weekday())

# 43
# 44
# 45
# 46
# 50