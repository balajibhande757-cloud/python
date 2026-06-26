def marks(**kwargs):
    for item in kwargs.keys():
        print(f"marks of {item} is {kwargs[item]}")

marks(lala=58,kishan=87,mahesh=78,pooja=76)





# COMBINED ARGS AND KWARGS

def func1(*args,**kwargs):
    print(args)
    print(kwargs)

func1(7,8,2,554,4,lala=78,mahesh=98,pooja=92)