lst_in = ['1 2 3 4', '5 6 7 8', '9 8 7 6']

lst = list(map(lambda x: x.split(), lst_in))

zip_out = zip(*lst)

for x in zip_out:
    print(*x)