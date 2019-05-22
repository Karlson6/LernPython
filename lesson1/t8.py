def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    c = f'{one}{delimiter}{two}'
    return c
print(get_summ("Learn", "python", delimiter='&').upper())