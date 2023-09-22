Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']


# Using normal list:
def using_normal_list(names):
    l = []
    for name in names:
        l.append(len(name))
    return l



# Using list comprehension:
def using_list_comprehension(names):
    return [len(x) for x in Names]


# Using functional programming:
def using_functaional_programming(names):
    return list(map(len, Names))


print(using_normal_list(Names))
print(using_list_comprehension(Names))
print(using_functaional_programming(Names))