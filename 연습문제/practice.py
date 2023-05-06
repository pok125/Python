# 언패킹
a, b, *c = (0, 1, 2, 3, 4, 5)
print(a, b, c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, _, _ = scores
print(valid_score)

_, *valid_score, _ = scores
print(valid_score)

temp = {}
temp2 = {2}
print(type(temp), type(temp2))

# =====
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice['메로나'] = 1300
print(ice)
ice.pop('메로나') # del ice['메로나']
print(ice)

# =====
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory['메로나'][0])
inventory['월드콘'] = [500, 7]
print(inventory)

total_price = sum([i[0] for i in inventory.values()])
print(total_price)

new_product = {'가나다': [100, 10]}
inventory.update(new_product)
print(inventory)
# =====
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
d = dict(zip(keys, vals))
print(d)

# =====
l = ['dog', 'cat', 'parrot']

for i in range(len(l)):
    l[i] = l[i].capitalize()
    
print(l)
