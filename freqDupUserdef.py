def check_ele(lis, l, freq, x):
    for i in range(l):
        if lis[i] == x:
            freq[x] += 1

def count_frequency(lis, l):
    freq = [0] * 100
    for i in range(100):
        check_ele(lis, l, freq, i)
    for i in range(100):
        if freq[i] > 1:
            print("frequency of", i, "is ", freq[i])

lis = list(map(int,input("Enter numbers: ").split()))
l = len(lis)
count_frequency(lis, l)
