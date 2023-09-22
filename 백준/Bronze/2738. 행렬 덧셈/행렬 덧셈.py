#import numpy as np

row, col = map(int, input().split(' '))

mat1 = [0 for _ in range(row)]

for i in range(row):
    mat1[i] = list(map(int, input().split(' ')))


mat2 = [0 for _ in range(row)]

for i in range(row):
    mat2[i] = list(map(int, input().split(' ')))

#mat1 = np.array(mat1)
#mat2 = np.array(mat2)
#answer = list(mat1 + mat2)

#for i in range(row):
#    print(*answer[i])
 
for i in range(row):
    print(*list(map(lambda x, y: x+y, mat1[i], mat2[i])))
        