import math

def countingSort(A, B):
	print("length of a: ", len(A))
	print("length of b: ", len(B))

	sizeA = len(A)
	max_val = int(max(A))


	C = [0] * (max_val+1)

	for i in range(0, sizeA):
		j = A[i]
		C[j] += 1 

	for i in range(1, max_val+1):
		C[i] += C[i-1]

	for i in range(sizeA-1, -1, -1):
		j = A[i]
		C[j] -= 1
		B[C[j]] = A[i]
		#C[j] -= 1

	return B

def insertionSort(A):
	sizeA = len(A)
	for i in range(1, sizeA):
		j = i-1
		key = A[i]
		while (j>=0 and key < A[j]):
			A[j+1] = A[j]
			j = j-1
		A[j+1] = key
	
	return A


def selectionSort(A):
	sizeA = len(A)
	for j in range(0, sizeA-1):
		iMin = j
		for i in range(j+1, sizeA):
			if (A[i] < A[iMin]):
				iMin = i
		(A[j], A[iMin]) = (A[iMin], A[j])
	return A

def partition(A, p, r):
	
	x = A[r]
	i = p-1

	for j in range(p, r):
		if (A[j] <= x):
			i += 1
			(A[i], A[j]) = (A[j], A[i])
	
	(A[i+1], A[r]) = (A[r], A[i+1])
	
	return i+1 


def quickSort(A, p, r):
	
	if (p<r):
		q = partition(A, p, r)
		quickSort(A, p, q-1)
		quickSort(A, q+1, r)

	return A


def mergeSort(A):

	sizeA = len(A) 
	if sizeA > 1:
		m = sizeA // 2
		l = A[:m]
		r = A[m:]

		mergeSort(l)
		mergeSort(r)

		i = 0
		j = 0
		k = 0

		sizeL = len(l)
		sizeR = len(r)

		while (i < sizeL and j < sizeR):
			if (l[i] < r[j]):
				A[k] = l[i]
				i+= 1
			else:
				A[k] = r[j]
				j+= 1
			k += 1

		while i < sizeL:
			A[k] = l[i]
			i+= 1
			k+= 1

		while j < sizeR:
			A[k] = r[j]
			j+=1
			k+=1


def heapify(A, heapsize, parent):
	
	largest = parent

	print("parent, largest: ", parent, largest)

	lChild = 2 * parent  
	rChild = 2 * parent + 1

	print("l child: ", lChild)
	print("r child: ", rChild)


	if (A[lChild] > A[parent] and lChild < heapsize):
		largest = lChild

	if (A[rChild] > A[largest] and rChild < heapsize):
		largest = rChild

	if (largest != parent):
		(A[parent], A[largest]) = (A[largest], A[parent])
		heapify(A, heapsize, largest)

def heapSort(A):
	heapsize = len(A)
	
	print("heapsize: ", heapsize)
	for i in range(heapsize//2 - 1, -1, -1):
		heapify(A, heapsize,i)
	
	for i in range(heapsize-1, 0, -1):
		(A[i], A[0]) = (A[0], A[i])
		heapify(A, i, 0) 


A = [12, 11, 13, 5, 6, 7]
B = [0] * (len(A))
print(A)
B = countingSort(A,B)
print(B)


