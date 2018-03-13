import numpy as np
import matplotlib.pyplot as plt
import csv

#main
def main():
        #declear matrix
        row=4
        col=7
        matrix = [[0]*col for i in range(row)]

        #keyword frequency 
        matrix[0][0]=2
        matrix[1][0]=1
        matrix[2][0]=0
        matrix[3][0]=1

        matrix[0][1]=1
        matrix[1][1]=1
        matrix[2][1]=2
        matrix[3][1]=1

        matrix[0][2]=1
        matrix[1][2]=1
        matrix[2][2]=0
        matrix[3][2]=0

        matrix[0][3]=0
        matrix[1][3]=1
        matrix[2][3]=1
        matrix[3][3]=1

        matrix[0][4]=0
        matrix[1][4]=0
        matrix[2][4]=0
        matrix[3][4]=1

        matrix[0][5]=1
        matrix[1][5]=1
        matrix[2][5]=0
        matrix[3][5]=1

        matrix[0][6]=1
        matrix[1][6]=2
        matrix[2][6]=0
        matrix[3][6]=0

        print('Matrix');
        matrix = np.array(matrix)
        print(np.matrix(matrix))

        #calulating weight [C]
        matrixWeight = [[0]*row for i in range(row)]
        #print(matrixWeight);
        
        for i in range(0,row):
            for j in range(0,row):
                sum=0;
                for k in range(0,col):
                    #print(i,j,k);
                    sum=sum+(matrix[i][k]*matrix[j][k])
                    matrixWeight[i][j]=sum
        print('Weight Matrix');
        matrixWeight = np.array(matrixWeight)
        print(np.matrix(matrixWeight))

        #calulating Normalized matrix
        NormalizedMatrix = [[0.0]*row for i in range(row)]
        for i in range(0,row):
            for j in range(0,row):
                NormalizedMatrix[i][j]=(matrixWeight[i][j]/(matrixWeight[i][i]+matrixWeight[j][j]-matrixWeight[i][j]));
                NormalizedMatrix[i][j]= float("{0:.2f}".format(NormalizedMatrix[i][j]))
        print('Normalized Weight Matrix');
        NormalizedMatrix = np.array(NormalizedMatrix)
        print(np.matrix(NormalizedMatrix))
             
main()
