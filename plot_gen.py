#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy as sp
from scipy.stats import ortho_group

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
  plt.close()



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
N = 10
m = sp.sparse.diags(
      [np.random.random(N-1),np.random.random(N),np.random.random(N-1)],
      [-1,0,1],
      shape=(N,N)
    ).todense()
MakeMatrixFig("imgs/rg_tridiagonal.pdf", m)

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

np.random.seed(123456789)
m = ortho_group.rvs(dim=10)
MakeMatrixFig("imgs/rg_orthogonal.pdf", m)


np.random.seed(123456787)
cols = np.random.rand(9)
rows = np.random.rand(10)
m    = sp.linalg.toeplitz(cols,rows)
MakeMatrixFig("imgs/rg_toeplitz.pdf", m)


np.random.seed(123456787)
h         = np.random.rand(5)
h         = h/np.linalg.norm(h)
padding   = np.zeros(h.shape[0] - 1, h.dtype)
first_col = np.r_[h, padding]
first_row = np.r_[h[0], padding]
H         = sp.linalg.toeplitz(first_col, first_row)
MakeMatrixFig("imgs/rg_toeplitz_1d_conv.pdf", H)


a  = np.array(range(10))
a  = np.random.permutation(a)
pm = np.zeros((10,10))
pm[np.arange(10), a] = 1
MakeMatrixFig("imgs/rg_permutation_matrix.pdf", pm)


np.random.seed(123456789)
a   = np.random.rand(10,10)
q,r = np.linalg.qr(a, mode='complete')
MakeMatrixFig("imgs/decomp_qr_a.pdf", a)
MakeMatrixFig("imgs/decomp_qr_q.pdf", q)
MakeMatrixFig("imgs/decomp_qr_r.pdf", r)



np.random.seed(123456789)
a = np.random.rand(10,10)
a = a@np.transpose(a)
L = np.linalg.cholesky(a)
MakeMatrixFig("imgs/decomp_cholesky_a.pdf", a)
MakeMatrixFig("imgs/decomp_cholesky_L.pdf", L)
MakeMatrixFig("imgs/decomp_cholesky_LT.pdf", np.transpose(L))



np.random.seed(123456789)
a           = np.random.rand(10,10)
a           = a@np.transpose(a)
lu, d, perm = sp.linalg.ldl(a)
MakeMatrixFig("imgs/decomp_ldlt_a.pdf", a)
MakeMatrixFig("imgs/decomp_ldlt_L.pdf", lu)
MakeMatrixFig("imgs/decomp_ldlt_D.pdf", d)
MakeMatrixFig("imgs/decomp_ldlt_LT.pdf", np.transpose(lu))