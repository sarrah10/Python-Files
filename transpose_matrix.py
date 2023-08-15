A=[[4,5,6,7],
[8,9,4,6],
[3,2,5,7]
]
print("Before Transporse: ") 
for i in A:
    print(i)
print("After Transporse: ") 
trans=[[0,0,0],
[0,0,0],
[0,0,0],
[0,0,0]]
for a in range(len(A)):
    for b in range(len(A[0])):
        trans[b][a]=A[a][b] 
for result in trans:
    print(result)
