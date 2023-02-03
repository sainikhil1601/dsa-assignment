def count_frequency(lis, l):
    freq = [0] * 100
    for i in range(l):
        freq[lis[i]] += 1
    for i in range(100):
        if freq[i] > 1:
            print("frequency of", i, "is ", freq[i])

lis = list(map(int,input("Enter numbers:").split()))
l = len(lis)
count_frequency(lis, l)
