from timeit import timeit





a_list = list(range(10_000))
a_set = set(a_list)
a_dict = {e:None for e in a_list}
in_list = timeit('5_000 in a_list', 'from __main__ inport a_list', number=100)
in_set = timeit('5_000 in a_set', 'from __main__ inport a_set', number=100)
in_dict = timeit('5_000 in a_dict', 'from __main__ inport a_dict', number=100)

print(f'{in_list:.6f}')
print(f'{in_set:.6f}')
print(f'{in_dict:.6f}')
