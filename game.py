tyikftoftgi

num = {}
num[0] = ['a','b','c','d','e','f']
num[1] = ['b','c']
num[2] = ['a','b','d','e','g']
num[3] = ['a','b','c','d','g']
num[4] = ['b','c','f','g']
num[5] = ['a','c','d','f','g']
num[6] = ['a','c','d','e','f','g']
num[7] = ['a','b','c']
num[8] = ['a','b','c','d','e','f','g']
num[9] = ['a','b','c','d','f','g']
#for ele in num:
	#print num[ele]
	
near = {}
#near[0] = [8,9,6,7,5,3,2,4,1]
#near[1] = [7,4,3,9,0,8,5,2,6]
#near[2] = [8,3,9,6,0,7,5,4,1]
#near[3] = [9,8,7,5,2,6,4,1,0]
#near[4] = []	

near[0] = [(0, 0),(1, 4),(2, 3),(3, 3),(4, 4),(5, 3),(6, 2),(7, 3),(8, 1),(9, 2)]
near[1] = [(0, 4),(1, 0),(2, 5),(3, 3),(4, 2),(5, 5),(6, 6),(7, 1),(8, 5),(9, 4)]
near[2] = [(0, 3),(1, 5),(2, 0),(3, 2),(4, 5),(5, 4),(6, 3),(7, 4),(8, 2),(9, 3)]
near[3] = [(0, 3),(1, 3),(2, 2),(3, 0),(4, 3),(5, 2),(6, 3),(7, 2),(8, 2),(9, 1)]
near[4] = [(0, 4),(1, 2),(2, 5),(3, 3),(4, 0),(5, 3),(6, 4),(7, 3),(8, 3),(9, 2)]
near[5] = [(0, 3),(1, 5),(2, 4),(3, 2),(4, 3),(5, 0),(6, 1),(7, 4),(8, 2),(9, 1)]
near[6] = [(0, 2),(1, 6),(2, 3),(3, 3),(4, 4),(5, 1),(6, 0),(7, 5),(8, 1),(9, 2)]
near[7] = [(0, 3),(1, 1),(2, 4),(3, 2),(4, 3),(5, 4),(6, 5),(7, 0),(8, 4),(9, 3)]
near[8] = [(0, 1),(1, 5),(2, 2),(3, 2),(4, 3),(5, 2),(6, 1),(7, 4),(8, 0),(9, 1)]
near[9] = [(0, 2),(1, 4),(2, 3),(3, 1),(4, 2),(5, 1),(6, 2),(7, 3),(8, 1),(9, 0)]


def getcount(x,y):
	delete = set(num[x]) - set(num[y])
	add = set(num[y]) - set(num[x])
	return len(delete)+len(add)
	
def change(x,y,ch):
	delete = set(num[x]) - set(num[y])
	add = set(num[y]) - set(num[x])
	for ele in delete:
		print 'Delete', ele,'from',ch
	for ele in add:
		print 'Add', ele, 'to', ch 

#-----------------------------------------------#	
A,B,C,D = map(int,raw_input("enter\n").split())
ans = C * 10 + D
print A,'+',B,' = ',"%02d" % ans
if ans > 18:
	print "not possible"
	sys.exit(0)

#-----------------------------------------------#	
left = A + B  #CD is changing
a = getcount(C,left/10)+getcount(D,left%10)

right = ans
#-----------------------------------------------#	
temp = ans - B   #A is changing
if temp <= 9:
	b = getcount(A,temp)
else:
	b = 50  # high value

#-----------------------------------------------#	
temp = ans - A  #B is changing
if temp <= 9:
	c = getcount(B,temp)
else:
	c = 50  #high value

#-----------------------------------------------#	
# both A and B changes    -->  5 + 5 = 12 => 6 + 6 = 12
d = [50,0,0]
if right < 10:
	i = 0
	max = right
else:
	i = right - 9
	max = 9
while i <= max:
	j = right - i
	cache = getcount(A,i) + getcount(B,j)
	if cache < d[0]:
		d = [cache,i,j]
	i = i + 1

print a,b,c,d[0],min(a,b,c,d[0])
minimum = min(a,b,c,d[0])
if a == minimum:
	change(C,left/10,'C')
	change(D,left%10,'D')
	print A,'+',B,' = ',"%02d" % left

elif b == minimum:
	temp = ans - B
	change(A,temp,'A')
	print temp,'+',B,' = ',"%02d" % ans
	
elif c == minimum:
	temp = ans - A	
	change(B,temp,'B')
	print A,'+',temp,' = ',"%02d" % ans

else:
	change(A,d[1],'A')
	change(B,d[2],'B')
	print d[1],'+',d[2],' = ',"%02d" % ans






