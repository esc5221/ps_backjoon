# get N and N integer list
T = int(input())
N = []
for t in range(T):
    N.append(int(input()))

counts = [[0, 0] for _ in range(41)]


def fibonacci_count(n):
    if counts[n] != [0, 0]:
        #print(n, "!!")
        return counts[n]

    #print("  not counted on ", n)
    if n == 0:
        counts[0] = [1, 0]
        return [1, 0]
    elif n == 1:
        counts[1] = [0, 1]
        return [0, 1]
    else:
        n_1 = fibonacci_count(n-1)
        n_2 = fibonacci_count(n-2)
        counts[n] = [n_1[0] + n_2[0], n_1[1] + n_2[1]]
        return counts[n]


for i in N:
    res = fibonacci_count(i)
    print(res[0], res[1])
