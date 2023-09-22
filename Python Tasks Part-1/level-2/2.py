Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']


# Using normal list:
def get_names_contains_a_using_normal_list(Names):
    l = []
    for name in Names:
        if 'a' in name:
            l.append(name)
    return l



# Using list comprehension:
def get_names_contains_a_using_list_comprehension(Names):
    return [x for x in Names if 'a' in x]



# Using functional programming:
def get_names_contains_a_using_functional_programming(Names):
    return list(filter(lambda name: 'a' in name, Names))



print(get_names_contains_a_using_normal_list(Names))
print(get_names_contains_a_using_list_comprehension(Names))
print(get_names_contains_a_using_functional_programming(Names))