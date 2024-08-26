#input format - item1:number1-price1, item2:number2-price2

import sys

args = sys.argv[1:]

items = []
no_items = []
price_items =[]
total_items = []

def spaces(s, r):
    l = len(s)
    if l < r:
        d = r-l
        ls = list(s)
        for i in range(d):
            ls.append(" ")
        # print(ls)
        ns = "".join(ls)
        return ns

def numbers(n):
    lst = [str(i) for i in str(n)]
    l = len(lst)
    if l < 8:
        d = 8-l
        for i in range(d):
            lst.append(" ")
        # print(ls)
        ns = "".join(lst)
        return ns

for i in args:
    a, b = i.split(":")
    a = spaces(a, 15)
    items.append(a)
    c, d = b.split("-")
    c = numbers(c)
    d = numbers(d)
    no_items.append(c)
    price_items.append(d)
    e = int(c) * int(d)
    e = numbers(e)
    total_items.append(e)

item = spaces("Item", 15)
Number = spaces("Number", 8)
Price = spaces("Price", 8)
Cost = spaces("Total", 8)

print(item, Number, Price, Cost)
print("----------------------------------------")

for x in range(len(items)):
    # print(" ".join((items[x], str(no_items[x]), str(price_items[x]), str(total_items[x]))))
    print(items[x], no_items[x], price_items[x], total_items[x])

def Grand(l):
    add =0
    for i in l:
        add = add + int(i)
    return add

space = spaces("", 15)
space1 = spaces("", 8)
grand = spaces("Grand", 8)
grand_cost = numbers(Grand(total_items))

print("                       -----------------")
print(space, space1, grand, grand_cost)