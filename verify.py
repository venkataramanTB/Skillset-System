uid = ["Venky","Yash"]
pwd = ["123","123"]
entuid = input().strip()
entpwd = input().strip()
for i in range (2):
    if(entuid==uid[i] && entpwd==uid[i]):
        print(1)
    else:
        print(0)
        