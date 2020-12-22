import math
import re

results = []

def cal(c,v):
	coeff = float(c)
	val = float(v)
	result = coeff*(math.log(val,2))
	return result


def calculation(r,o):
	for i in range(0,len(o)):
		if len(r) == 1:
			break
		if o[i] == '+':
			s = r[0]+r[1]
			del r[0:2]
			r.insert(0,s)
		if o[i] == '-':
			s = r[0]-r[1]
			del r[0:2]
			r.insert(0,s)
	print("The Value of the given expression is:", s)


print("LOG to the Base 2 Calulator")
data = input("\nEnter the expression: ")

data = data.replace(" ", "")

op = re.findall('[+-]{1}',data)

data = re.split('[+-]{1}',data)

for i in range(0,len(data)):
	num = data[i].split("log")
	if not num[0]:
		num[0]="1"
	result = cal(num[0],num[1])
	results.append(result)

calculation(results,op)