def unqEle(lis):
    s = []
    for i in range(len(lis)):
        if lis[i] not in s:
            s.append(lis[i])
    print("unique numbers:",s)
    for i in range(len(s)):
        for j in range(0, len(s) - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s

inp = list(map(int,input("Enter input numbers:").split()))
print("Sorted and unique numbers: ",unqEle(inp))
