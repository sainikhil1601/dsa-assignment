def dup_ele(lis, l, freq, i):
    if i == l:
        return
    freq[lis[i]] += 1
    dup_ele(lis, l, freq, i+1)

def count_frequency(lis, l):
    freq = [0] * 100
    dup_ele(lis, l, freq, 0)
    for i in range(100):
        if freq[i] > 1:
            print("frequency of", i, "is ", freq[i])

lis = list(map(int,input("Enter Numbers: ").split()))
l = len(lis)
count_frequency(lis, l)
