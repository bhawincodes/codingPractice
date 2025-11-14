t = int(input())
for i in range(t):
    len = int(input())
    str = input()
    dict = {}
    cost = 0
    for j in range(len):
        if(str[j] in dict):
            dict[str[j]] = dict[str[j]] + 1
        else:
            dict[str[j]] = 1
    # checking if any off values present in the dictionary
    for key, value in dict.items():
        if value % 2 != 0:
            cost = cost + 1
    print(0 if cost == 0 else cost-1)