Names = ['mahmoud', 'farida', 'ali', 'hassan', 'mohamed', 'khaled', 'taha']


# using normal list
def transoform_using_normal_list(Names):
    for i in range(len(Names)):
        Names[i] = Names[i].upper()
    return Names


# Using list comprehension
def transform_using_list_comprehension(Names):
    return [x.upper() for x in Names]


# Using functional programming
def transform_using_functional_programming(Names):
    return list(map(lambda x : x.upper(), Names))


print(transoform_using_normal_list(Names))
print(transform_using_list_comprehension(Names))
print(transform_using_functional_programming(Names))