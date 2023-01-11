import sys
import random
allowed = set("gcta")
a = input()
b = input()
if(len(a) != 16 or len(b) != 16):
        print("Wrong input")
        sys.exit()
# if(not a.is(allowed)):
#         print("Wrong input")
#         sys.exit()

str1 = [i for i in a]
str2 = [i for i in b]
        
random.shuffle(str1)
random.shuffle(str2)

print(str1)
print(str2)

gene1 = []
gene2 = []

for i in range(16):
    if(not str1[i] in gene1):
        gene1.append(str1[i])
    if(not str2[i] in gene2):
        gene2.append(str2[i])
        
print(gene1)
print(gene2)

num_rows = 5
num_columns = 5

matrix = [[0 for i in range(num_columns)] for i in range(num_rows)]

def mat_mul(matrix,i,j,gene1,gene2):
    if(gene1[i-1] ==  gene2[j-1]):
        matrix[i][j] = 5 + matrix[(i-1)][(j-1)]
    else:
        p = max(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])
        matrix[i][j] = p - 4
    if(i<4):
        mat_mul(matrix,(i+1),j,gene1,gene2)
    else:
        if(j < 4):
            mat_mul(matrix,1,(j+1),gene1,gene2)

mat_mul(matrix,1,1,gene1,gene2)

for i in range(4):
    for j in range(4):
        print(matrix[i+1][j+1])
    print("\n")
        
        
    