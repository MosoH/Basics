#Python Programming Group Question FB.
list1=[1,3,3,4,4,5,2,7,8,9,2,0,6,9,13,25,10]
list2=[3,1,4,5,4,6,8,9,12,13,10]
a=[]
b=set(list1)
c=set(list2)
print(b,c)
for i in b:
	if i in c:
		a.append(i)
print(a)