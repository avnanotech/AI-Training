# Definisanje matrica

matx1 = [[-2, 2, -3], [-1, 1, 3], [2, 0, -1]]
matx2 = [[1, 3, 2], [ 1, 0,0], [1,2, 2]]


# Operacije sa matricama

def mymatrix():

    # Matrica A
    print("Matrica A")
    print(matx1)

    det1=matx1[0][0]*(matx1[1][1]*matx1[2][2]-matx1[2][1]*matx1[1][2])-\
        matx1[1][0]*(matx1[0][1]*matx1[2][2]-matx1[2][1]*matx1[0][2])+\
        matx1[2][0]*(matx1[0][1]*matx1[1][2]-matx1[1][1]*matx1[0][2])
    print("Determinanta matrica 1  je",det1)


    # Matrica B
    print("Matrica B")
    print(matx2)


    det2=matx2[0][0]*(matx2[1][1]*matx2[2][2]-matx2[1][2]*matx2[2][1])-\
        matx2[1][0]*(matx2[0][1]*matx2[2][2]-matx2[2][1]*matx2[0][2])+\
        matx2[2][0]*(matx2[0][1]*matx2[1][2]-matx2[1][1]*matx2[0][2])
    print("Determinanta matrica 2  je",det2)

  # Zbir matrice A i matrice B

    print("Zbir matrice A i matrice B")

    smatx=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(smatx)) :
      for j in range(len(smatx[0])):
        smatx[i][j]=matx1[i][j]+matx2[i][j]
    print(smatx)

    # Proizvod matrice A i matrice B

    print("Proizvod matrice A i matrice B")

    pmatx = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(pmatx)):
      for j in range(len(pmatx[0])):
          pmatx[i][j] =0
          for k in range(len(pmatx)):
            pmatx[i][j] = pmatx[i][j] +matx1[i][k]*matx2[k][j]
    print(pmatx)


if __name__ == '__main__':
    mymatrix()
