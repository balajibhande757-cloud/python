# def greater_than_9(a):
#     if a>9:
#         return True
#     else:
#         False

b=[3,12,54,6,66,9,669,36,4,0,3,2,5,85,47,55]

new=list(filter(lambda x : x>9,b))
print(new)