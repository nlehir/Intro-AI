def badrec(x):
    if x > 0:
        return badrec(x / 2)
    else:
        return 1


print(badrec(3))
