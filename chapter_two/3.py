a, b = map(int,input().split())
a_list = list(map(int, input().split()))
result_list = []

a_list.sort(reverse=True)

for i in range(len(a_list)):
    for j in range(len(a_list) - 1):
        for k in range(len(a_list) - 2):
            sum = a_list[i] + a_list[j+1] + a_list[k+2]
            result_list.append(sum)
            new_list = list(dict.fromkeys(result_list))
            if len(new_list) == b :
                print(new_list)
                break
            sum = 0

print(new_list[b - 1])




