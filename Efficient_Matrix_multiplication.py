import random as rand
#matrix multiplication 
#getting input from the user in linear array form to produce a matrix of user's choice length 
#r = int(input('Enter the rows of the matrix : '))
#c = int(input('Enter the columns of the matrix : '))
r1 = int(rand.randrange(2,10,1))
c = int(rand.randrange(2,10,1))
mat1 = []
for i in range(r1):
	n = []
	for j in range(c):
		#n.append(int(input('Enter the row-wise value of matrix : ')))
		n.append(int(rand.randrange(10,100,1)))
	mat1.append(n)
	#if (i < r-1 ) :	
		#print('\r Now enter in another row! \r')
	#else :
		#print('Matrix Input Complete! ')	
print('The number of Rows : ',r1)
print('The number of Columuns : ',c)
print('The matrix : ')		
for i in range(r1):
	for j in range(c):
 		print(mat1[i][j],end = ' ')
	print()
# as the number of column of first matrix is equal to the row of second matrix 
c1 = int(rand.randrange(2,10,1))
mat2 = []
for i in range(c):
	m = []
	for j in range(c1):
		m.append(int(rand.randrange(10,100,1)))	
	mat2.append(m)
print()
print('The number of Rows : ',c)
print('The number of Columns : ',c1)
print('The 2nd matrix :  ')
for i in range(c):
	for j in range(c1):
		print(mat2[i][j],end = ' ')
	print()	
#second matrix completed and printed 
# third matrix number of column of second matrix = row of third matrix 
c2 = int(rand.randrange(2,10,1))
mat3 = []
for i in range(c1):
	p = []
	for j in range(c2):
		p.append(int(rand.randrange(10,100,1)))
	mat3.append(p)
print()
print('The number of Rows : ',c1)
print('The number of Columns : ',c2)
print('The 3rd Matrix : ')
for i in range(c1):
	for j in range(c2):
		print(mat3[i][j], end = ' ')
	print()
#printed the 3rd matrix 
# for matrix multiplication we need to fill a new matrix 
#let the new matrix be matA 
matA = []
#this matrix has 3X3 dimension 
# as there as 3 matrices to be multiplied 
# r1 = row of 1st matric 
# c = column of 1st matric and row of 2nd matric 
# c1 = column of 2nd matric and row of 3rd matric 
# c2 = column of 3rd matric 
buffer2 = c*c1*c2 + r1*c1*c2
#buffer2 is the 
buffer1 = r1*c*c1 + r1*c*c2

print()
if(buffer1 > buffer2):
	flag = 1
	print('The other option',buffer1)
else:
	flag = 0 
	print('The other option',buffer2)
print('')
for i in range(3):
	q = []
	for j in range(3):
		if (i == j ):
			q.append(int(0))
		elif((i == 0) and (j == 1)):
			q.append(int(r1*c*c1))
		elif( (i == 1) and (j == 2)):
			q.append(int(c*c1*c2))
		elif(( i == 0) and (j == 2 )):
			if (flag == 1):
				q.append(int(buffer2))
			else :
				q.append(int(buffer1))
		else :
			q.append(int(1))
	matA.append(q)
print('New matrix')
for i in range(3):
	for j in range(3):
		print(matA[i][j], end = " ")
	print()
matB = []
#for finding the arrange of the matrices 
for i in range(3):
	r = []
	for j in range(3):
		if ( i == j ):
			r.append(int(0))
		elif( ( i == 0) and ( j == 1)):
			r.append(int( i + 1 ))
		elif((i == 1) and ( j == 2)):
			r.append(int( i + 1 ))
		elif(( i == 0) and ( j == 2)):
			if ( flag == 0 ):
				r.append(int(2))
			else :
				r.append(int(1))
		else :
			r.append(int(1))
	matB.append(r)
print()
for i in range(3):
	for j in range(3):
		print(matB[i][j], end = ' ')
	print()
print('The arrangement should be : ')
if (flag == 0 )	:
	print('( A1 x A2 ) x A3 ')
else :
	print(' A1 x ( A2 x A3 ) ')
