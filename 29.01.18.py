from collections import Counter
f = open ('text-in.txt', 'r')
A,B,No = {},{},{}
def N(x):
	global No
	mass = [mass.append(value).sort() for value in x.values()]
		if (len(mass)) != 1:
		eins,zwei = mass[0], mass[1]
		for key in x.keys():
			if eins == x[key]:
				1key = str(key)
				del x[key]
				break
		for key in x.keys():
			if zwei == x[key]:
				2key = str(key)   
				del x[key]         
				break
		x[(1key + 2key)], n[(1key + 2key)] = (eins + zwei), {1key: eins, 2key: zwei}
		No.update(n) 
		N(x)  

def K(x):
	global B
	1k = [1k.append(key) for key in x.keys()]
  2k = [2k if 1k[0] in Nod 2k = [] [ 2k.append(key) for key in Nod[1k[0]].keys()]]
		if len(2k[0]) >= len(2k[1]):
			K({k2[0]: (x[k[0]] + '0')})
			K({k2[1]: (x[k[0]] + '1')})
		else:
			K({k2[1]: (x[k[0]] + '0')})
			K({k2[0]: (x[k[0]] + '1')})
	else:
		B.update(x)

A[i]=[A[i] += 1 if i in A.keys() else A[i] = 1 for line in file]
N(Dic)
nk = ""
Key = []
nk = [key if len(key) > len(nk) for key in No.keys()]
key= [Key.append(key) for key in Nod[nk].keys()]
if len(Key[0]) >= len(Key[1]):
  K({Key[0]: '0'}) 
	K({Key[1]: '1'})
else:
    K({Key[1]: '0'})
    K({Key[0]: '1'})
2f = open('text-in.txt') 
3f = open('text-out.txt', 'w')
for line in 2f:
	for i in line:
		for key in B.keys():
			if i == key:
				of.write(str(B[key]))
				break
