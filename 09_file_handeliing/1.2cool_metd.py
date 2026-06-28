with open("jon-doe.txt","r") as f: #CONTEX MANAGER
    content=f.read()
    print(content)
    
    
# NO NEED TO WRITE F.CLOSE BECAUSE FILE IS ALREADY CLOSE DEFAULT USING WITH SYNX