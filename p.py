n=5
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print(i,end="")
    print()
n=8
for i in range(1,n,1):
    print(""*i,end="")
    print("*"*i,end="")
    print() 
    for i in range(1,5):
        print(str(i)*i)   
list=[3,4,5,9,6,6]
a=set(list)
print(a)        