

def lol():
    data = 0
    def lol2():
        nonlocal data
        data += 1
        return data
    return lol2
    

p = lol()

print(p())
print(p())
print(p())
print(p())