Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']


# using normal list to find names that has 2 or more 'a' characters
def using_normal_list(names):
    l = []
    for name in names:
        if name.count('a') >= 2:
            l.append(name)
    return l


# using list comprehension to find names that has 2 or more 'a' characters
def using_list_comprehension(names):
    return [x for x in names if x.count('a')>=2]


# using functional programming to find names that has 2 or more 'a' characters
def using_functional_programming(names):
    return list(filter(lambda name: name.count('a')>=2, Names))


print(using_normal_list(Names))
print(using_list_comprehension(Names))
print(using_functional_programming(Names))