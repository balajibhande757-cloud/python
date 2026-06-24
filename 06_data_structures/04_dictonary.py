# MUTABLE(CHANGABLE)
Marks={"mahesh":99,"lala":58,"pooja":54,
       "jhatu":55}

print(Marks,type(Marks))
print(Marks["pooja"])
Marks["jhatu"]=5
print(Marks)
print(Marks.keys())
print(Marks.values())
# Marks.clear()
Marks.pop("lala")
print(Marks)


table_of_five={i:5*i for i in range(1,11)}
print(table_of_five)