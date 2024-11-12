import re

def fun1(w):
    x = re.search(r"[aeiouyAEIOUY][^aeiouy]*$", w)
    if x:
        return x.group()
    return w

def fun2(s):
    r = []
    for w in s.split():
        y = fun1(w)
        n = y + w[:-len(y)] + "awy"
        r.append(n)
    return " ".join(r)

text = input("Enter a sentence: ")
print(fun2(text))