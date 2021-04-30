

def identifySubsets(subset,arry,k):
	final_subsets = []
	for x in range(len(subset)):
		if(arry[x][k] == 1):
			final_subsets.append(subset[x])
			base = x
			break

	counter = k
	while(counter>=0):
		if arry[base-1][counter] == 1:
			final_subsets.append(subset[base-1])
			if(sum(final_subsets)==k):
				break
			else:
				base = base - 1

		counter = counter - 1 

	final_subsets.sort()
	return final_subsets


def printMatrix(arry,row,col,j_for_sums,snail):
	j_for_sums.insert(0,"-")
	print("[!] ARRAY: ")
	for x in j_for_sums:
		print(x,end=" ")
	print("\n")
	for x in range(row):
		print(snail[x],end=" ")
		for y in range(col):
			print(arry[x][y],end=" ")
		print("\n")


def main():
	
	snail = [1,2,3]
	k = 5
	values = [6,10,12]
	

	snail.sort()

	print("\n")
	#create a multidimensional array
	dyna_array = [[0 for x in range(k+1)] for x in range(len(snail))]

	j_for_sums = [i for i in range(k+1)]

	snail_updated = []

	for i in range(len(snail)):
		dyna_array[i][0] = 1

	#identify the indexes that can be marked as 1
	for i in range(len(snail)):
		snail_updated.append(snail[i])
		for j in range(1,k+1):
			if (j_for_sums[j] in snail_updated):
				dyna_array[i][j] = 1
			if(i>0):
				if(dyna_array[i-1][j] == 1):
					dyna_array[i][j] = 1
				elif(j>snail[i]):
					if(dyna_array[i-1][j-snail[i]] == 1):
						dyna_array[i][j] = 1

	printMatrix(dyna_array,len(snail),k+1,j_for_sums,snail)




	#check if there is a solution
	answer = 0
	valuess = []
	if(dyna_array[len(snail)-1][k]):
		answer = identifySubsets(snail,dyna_array,k)
		print("Answer: ",answer)

	else:
		print("[!] There is no solution")

	for i in answer:
		valuess.append(values[i-1])
		

	print(sum(valuess))


main()

