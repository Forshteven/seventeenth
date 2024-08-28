def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [12, "moon", [1, 2, 3]]
values_dict = {"Vlad": 25, "Egor": 46, "Chipolino": "Raddari"}


print_params(*values_list)
print_params(**values_dict)