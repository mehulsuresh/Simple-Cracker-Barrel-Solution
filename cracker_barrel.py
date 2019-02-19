import random
a = []
num = int(input("Enter the number of rows : "))
# num = 4
for i in range(num):
	a.append([])
	for j in range(i+1):
		a[i].append(1)
b = [i+1 for i in range(num)]
slct = random.randint(1, sum(b))
count=0
for idx,val in enumerate(a):
	for idj,vlv in enumerate(val):
			count+=1
			if count == slct:
				a[idx][idj]=0
def ret_tf(a, x , y):
	if x < 0 or y < 0:
		return False
	try:
		n = a[x][y]
		if n == 0:
			return True
		else:
			return False
	except:
		return False
def remainder(a):	 
	count=0
	for idx,val in enumerate(a):
		for idj,vlv in enumerate(val):
				if vlv==1:
					count+=1
	return count
def can_make_move(a1,x1,y1,x2,y2,x3,y3):
	if a1[x1][y1]==1:
		if a1[x2][y2]==1:
			if a1[x3][y3]==0:
#				  a[x1][y1]=0
#				  a[x2][y2]=0
#				  a[x3][y3]=1
				return True
			else:
				return False
		else:
			return False
	else:
		return False
def do_make_move(a1,x1,y1,x2,y2,x3,y3):
	a1[x1][y1]=0
	a1[x2][y2]=0
	a1[x3][y3]=1
	return a1
disp ={}
for i in range(1,sum(b)):
	disp[i]=[]
import copy

def solve(a):
	disp[remainder(a)]=copy.deepcopy(a)
	if remainder(a) == 1:
		print(a)
		we_are_done()
		return True
	for i in range(num):
		for j in range(i+1):
#			  print(i,j)
			if ret_tf(a,i-2,j):
				if can_make_move(a,i,j,i-1,j,i-2,j)==True:
					a1 = copy.deepcopy(a)
#					  print("wt1",a)
					a = do_make_move(a,i,j,i-1,j,i-2,j)
					if solve(a)==False:
#						  print("Dead End1")
#						  print(a,a1)
						a = copy.deepcopy(a1)
					else:
						return True
						break
					
			
			if ret_tf(a,i+2,j):
				if can_make_move(a,i,j,i+1,j,i+2,j)==True:
					a2 = copy.deepcopy(a)
#					  print("wt2",a)
					a = do_make_move(a,i,j,i+1,j,i+2,j)
					if solve(a)==False:
#						  print("Dead End2")
#						  print(a,a2)
						a = copy.deepcopy(a2)
					else:
						return True
						break
					
			
			if ret_tf(a,i,j-2):
				if can_make_move(a,i,j,i,j-1,i,j-2)==True:
					a3 = copy.deepcopy(a)
#					  print("wt3",a)
					a = do_make_move(a,i,j,i,j-1,i,j-2)
					if solve(a)==False:
#						  print("Dead End3")
#						  print(a,a3)
						a = copy.deepcopy(a3)
					else:
						return True
						break
			
			if ret_tf(a,i,j+2):
				if can_make_move(a,i,j,i,j+1,i,j+2)==True:
					a4 = copy.deepcopy(a)
#					  print("wt4",a)
					a = do_make_move(a,i,j,i,j+1,i,j+2)
					if solve(a)==False:
#						  print("Dead End4")
#						  print(a,a4)
						a = copy.deepcopy(a4)
					else:
						return True
						break
			
			if ret_tf(a,i-2,j-2):
				if can_make_move(a,i,j,i-1,j-1,i-2,j-2)==True:
					a5 = copy.deepcopy(a)
#					  print("wt5",a)
					a = do_make_move(a,i,j,i-1,j-1,i-2,j-2)
					if solve(a)==False:
#						  print("Dead End5")
#						  print(a,a5)
						a = copy.deepcopy(a5)
					else:
						return True
						break
						
			
			if ret_tf(a,i+2,j+2):
				if can_make_move(a,i,j,i+1,j+1,i+2,j+2)==True:
					a6 = copy.deepcopy(a)
#					  print("wt6",a)
					a = do_make_move(a,i,j,i+1,j+1,i+2,j+2)
					if solve(a)==False:
#						  print("Dead End6")
#						  print(a,a6)
						a = copy.deepcopy(a6)
					else:
						return True
						break
	if remainder(a) != 1:
		return False
def we_are_done():
	for i,j in disp.items():
		for k in j:
			print(k)
	exit()

solve(a)