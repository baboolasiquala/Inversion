def merge_sort(lis, inv):
    l = lis[:len(lis)//2]
    r = lis[len(lis)//2:]
    inv_l = inv
    inv_r = inv
    if len(l) > 1:
        merge_sort(l, inv_l)
    print("inv_l is ", inv_l)
    if len(r) > 1:
        merge_sort(r, inv_r)
    print("inv_r is ", inv_r)
    inv = inv_l + inv_r
    print("inv is ", inv)
    print(l)
    print(r)
    i = 0
    j = 0
    k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            lis[k] = l[i]
            i += 1
        else:
            lis[k] = r[j]
            inv += len(l[i:])
            j += 1
        k += 1
    while i < len(l):
        lis[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        lis[k] = r[j]
        j += 1
        k += 1
    print("inv is ", inv)
    return lis, inv


lis = [6, 5, 4, 3, 2, 1]
inv = 0
print(merge_sort(lis, inv))