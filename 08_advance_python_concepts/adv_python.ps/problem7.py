# while(text:=input("Enter something:"))!="quit":
#     print(f"you Entered text:{text}")




words=["python", "rocks", "ai"]
lengths=[n for w in words if(n:=len(w))>=4]
print(lengths)