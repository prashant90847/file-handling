import os 
if os.path.exists("practice.txt"):

    with open("practice.txt","r") as f:
        content=f.read()
        print(content)
else:
    print("file not exist ")
    