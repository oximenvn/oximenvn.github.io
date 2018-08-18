import time
import random
import dis

def binary_gap(number):
	mark=1
	count0=0
	max0=0
	runner=number

	#find first 1
	while runner>0 and runner&mark!=1:
		runner=runner>>1

	while runner>0:
		#check last number is 1
		if runner&mark==1:
				if count0>max0:
					max0=count0
				pass
				count0=0
		else:
			count0+=1
		pass
		#shift right 1bit
		runner=runner>>1
	pass
	return max0

def binary_gap2(number):
	return len(max( bin(number)[2:].split('1')))


# for i in range(5):
# 	a=random.randint(1,100000000000)
# 	max0=binary_gap(a)
# 	print 'Max is ' +str(max0)+' of '+str(a)+' with binary form '+bin(a)[2:]

for i in range(1000000000,1000010001):
	start_time = time.time()
	max0=binary_gap2(i)
	#print((time.time() - start_time))
	print(str(i-1000000000)+', '+str(time.time() - start_time))
	#print max0+' '+bin(a)

# dis.dis(binary_gap)

# print '+++++++++++++++++++++++'

# dis.dis(binary_gap2)