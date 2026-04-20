def fungsi_list_aneh(n):
    list_aneh= []

    for i in range(0, n):
        list_aneh.insert(0, i)

    return list_aneh

print(fungsi_list_aneh(5))