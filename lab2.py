def first_list():
	list1=[5,10,15,20,25]
	list2=[list1[0],list1[-1]]
	print (list2)

first_list();

def under5():
	under=[]
	y= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	num = int(input("write a number"))
	for x in y:
		if x < num:
			under.append(x)
	print(under)

under5();

def common(lista, listb):
	listc= []
	for value in lista:
		if value in listb:
			listc.append (value)
