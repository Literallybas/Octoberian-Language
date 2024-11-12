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
        if w[0].isupper():
            n = n.capitalize()
        r.append(n)
    return " ".join(r)

while True:
    text = input("Enter a sentence (or type 'exit' to quit): ")
    if text.lower() == "exit":
        break
    print(fun2(text))
