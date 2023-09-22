Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']


# Using normal list:
def get_names_starting_with_t_using_normal_list(Names):
    l = []
    for name in Names:
        if name and name[0] == 't':
            l.append(name)
    return l


# Using list comprehension:
def get_names_starting_with_t_using_list_comprehension(Names):
    return [x for x in Names if x and x[0] == 't']


# Using functional programming:
def get_names_starting_with_t_using_functional_programming(Names):
    return list(filter(lambda x: x and x[0] == 't', Names))


print(get_names_starting_with_t_using_normal_list(Names))
print(get_names_starting_with_t_using_list_comprehension(Names))
print(get_names_starting_with_t_using_functional_programming(Names))