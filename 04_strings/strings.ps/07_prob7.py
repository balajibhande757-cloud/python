sent="python is the best programming language"
sum=0
vowels=["a","e","i","o","u"]
for char in sent.lower():
    if(char in vowels):
        sum+=1

print(f"there are {sum} vowels are in sentence")