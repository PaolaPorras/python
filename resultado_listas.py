#programa que suma dos matrices
x=[[12,2,5],[2,5,8],[6,9,4]]
y=[[2,6,7],[4,5,7],[20,4,7]]
resultado=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        resultado[i][j]=x[i][j]+y[i][j]
        print(resultado)