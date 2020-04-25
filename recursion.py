# lets return reverse of string with recursion !
# yaxchi, getduy

# %% reverse string


def reverse(string):
    if len(string) <= 1:
        return string
    return reverse(string[1:]) + string[0]


print(reverse("aqaq anad ridaltrap narmak"))


# %% multiplication with RECURSION !

def multiply(x, y):
    if y == 0:
        return 0
    else:
        return x + multiply(x, y-1)


print(multiply(4, 7))

# %% quvvete yukseltmation with RECURSION !!!


def power(x, y):
    if y == 0:
        return 1
    return x*power(x, y-1)


print(power(5, 2))

# %% power function using multiply function))


def power_another(x, y):
    if y == 0:
        return 1
    return multiply(x, power_another(x, y-1))


print(power_another(5, 3))
