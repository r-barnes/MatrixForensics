#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

def SaveIfNew(fig, filename, *args, **kwargs):
  if os.path.exists(filename):
    return
  fig.savefig(filename, *args, **kwargs)

def MakeMatrixFig(filename, mat):
  fig = plt.figure(figsize=(2,2), dpi=200)
  ax  = plt.subplot(111)
  ax.matshow(mat, cmap='gray')
  plt.xticks([])
  plt.yticks([])
  SaveIfNew(fig, filename, bbox_inches='tight', pad_inches=0.0)  



#Symmetric Matrix Example
np.random.seed(123456789)
N = 10
a = np.random.rand(N, N)
m = np.tril(a) + np.tril(a, -1).T
MakeMatrixFig("imgs/rg_symmetric_matrix.pdf", m)

np.random.seed(123456789)
N = 10
a = np.random.rand(N, N)
m = np.tril(a)
MakeMatrixFig("imgs/rg_lower_triangular.pdf", m)

np.random.seed(123456789)
N = 10
a = np.random.rand(N, N)
m = np.triu(a)
MakeMatrixFig("imgs/rg_upper_triangular.pdf", m)

np.random.seed(123456789)
N = 10
a = np.random.rand(N)
m = np.diag(a)
MakeMatrixFig("imgs/rg_diagonal.pdf", m)



np.random.seed(123456789)
a     = np.random.rand(10,4)
u,s,v = np.linalg.svd(a, full_matrices=True)
s     = np.diag(s)
s     = np.pad(s, ((0,6),(0,6)), 'constant', constant_values=0)
v     = np.pad(v, ((0,6),(0,6)), 'constant', constant_values=0)
MakeMatrixFig("imgs/decomp_svd_a.pdf", a)
MakeMatrixFig("imgs/decomp_svd_u.pdf", u)
MakeMatrixFig("imgs/decomp_svd_s.pdf", s)
MakeMatrixFig("imgs/decomp_svd_v.pdf", np.transpose(v))

np.random.seed(123456789)
a     = np.random.rand(10,4)
u,s,v = np.linalg.svd(a, full_matrices=False)
s     = np.diag(s)
MakeMatrixFig("imgs/decomp_svd_a_compact.pdf", a)
MakeMatrixFig("imgs/decomp_svd_u_compact.pdf", u)
MakeMatrixFig("imgs/decomp_svd_s_compact.pdf", s)
MakeMatrixFig("imgs/decomp_svd_v_compact.pdf", np.transpose(v))

np.random.seed(123456789)
a    = np.random.rand(6,1)
b    = np.random.rand(10,1)
dyad = a@np.transpose(b)
MakeMatrixFig("imgs/rg_dyad.pdf", dyad)