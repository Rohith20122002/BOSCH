str="[({ })](]"
list1=["(","[","{"]
list2=[")","]","}"]
stck1=[]
stck2=[]
flag=1
for i in range(len(str)):
    if(str[i] in list1):
        stck1.append(str[i])
    else:
        if(stck1[-1]=="(" and str[i]==")" or
           stck1[-1]=="[" and str[i]=="]" or
           stck1[-1]=="{" and str[i]=="}" ):
            stck1.pop()
        else:
            flag=0
print(stck1)
if(len(stck1)==0) and flag==1:
    print("you are python king")
else:
    print("you are python slave")

#print(stck2)
