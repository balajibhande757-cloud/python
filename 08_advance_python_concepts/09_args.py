def sum(*args):
    #ARGS WILL BE TUPLE OF ALL THE VALUES PASS TO SUM
    total=0
    for item in args:
        total+=item
    return total
print(sum(9,7,258,876))