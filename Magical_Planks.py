for _ in range(int(input())):
    n = int(input())
    s = input()
    count = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            count += 1
    if count == 0:
        print(0)
    else:
        print(count - 1)
