# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

Nx = 4
Ny = 4
a = 0; b = 1
c = 0; d = 1
hx = (b-a)/Nx; hy = (d-c)/Ny
X = np.arange(Nx); Y = np.arange(Ny)
G = np.meshgrid(X, Y)

#Ecrase les valeurs des points sur les bords pour forcer condtion de Dirichlet
def points_fantomes(Psi, m, hx, hy):
    Nx = len(Psi)-2
    Ny = len(Psi[0])-2
    for j in (0, Ny+1):
        y = hy*(j-Ny//2)
        for i in range(Nx+2):
            x = hx*(i-Nx//2)
            theta = np.arctan2(y, x)
            Psi[i][j] = np.exp(1j*m*theta)
    for i in (0, Nx+1):
        x = hx*(i-Nx//2)
        for j in range(1, Ny+1):
            y = hy*(j-Ny//2)
            theta = np.arctan2(y, x)
            Psi[i][j] = np.exp(1j*m*theta)
    return
            
    
#Il sera nécessaire de créer matriceLaplacien(Nx+2, Ny+2 pour compenser les points fantomes)
def matriceLaplacien(Nx, Ny):
    A = np.zeros((Nx*Ny, Nx*Ny))
    for i in range(Nx):
        for j in range(Ny):
            k = Ny*i+j
            if (i == 0 or i == Nx-1 or j == 0 or j == Ny-1):
                A[k][k] = 1
            else:
                A[k][k] = -4
                A[k][k-Ny] = 1
                A[k][k+Ny] = 1
                A[k][k+1] = 1
                A[k][k-1] = 1
    return A