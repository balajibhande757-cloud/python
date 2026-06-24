lala=[3,4,3,5,6,4,5,9,6]
print(lala)
print(set(lala))

d1={"name":"lala"}
d2={"job":"data scientist"}
d1.update(d2)
print(d1)


products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 3000,
    "TV": 60000
}

highest_product =max(products,key=products.get)
print("Product:", highest_product)
print("Price:", products[highest_product])