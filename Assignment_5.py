# Assignment_5

import numpy as np

# ------------------------------------------
# 1. MATRIX AND VECTOR OPERATIONS
# ------------------------------------------

print("\n---1. Creating a 3 × 3 matrix A and a 3 × 1 vector B---")

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
B = np.array([1, 2, 3])

# Matrix-vector multiplication

try:
    result = A @ B
    print("Matrix-Vector Multiplication A x B:\n", result)
except ValueError as e:
    print("Multiplication error:", e)

# Trace of A
trace_A = np.trace(A)
print("Trace of A:", trace_A)

# Eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues of A:\n", eigvals)
print("Eigenvectors of A:\n", eigvecs)

print("\n----2. Replace the last row of matrix A with [10, 11, 12] and: ----")

A[-1] = [10, 11, 12]
print("Updated Matrix A:\n", A)

# Determinant
det_A = np.linalg.det(A)
print("Determinant of updated A:", det_A)

# Check singularity
if np.isclose(det_A, 0):
    print("Matrix A is Singular")
else:
    print("Matrix A is Non-Singular")

# ------------------------------------------
# 2. INVERTIBILITY OF MATRICES
# ------------------------------------------

print("\n--- Section 1: Invertibility of Matrices ---")

if not np.isclose(det_A, 0):
    try:
        A_inv = np.linalg.inv(A)
        print("Inverse of A:\n", A_inv)
    except np.linalg.LinAlgError:
        print("Matrix A is not invertible.")
else:
    print("Skipping inverse calculation. Matrix is singular.")

# Solve A x X = B
try:
    X = np.linalg.solve(A, B)
    print("Solution X to A x X = B:\n", X)
except np.linalg.LinAlgError as e:
    print("Cannot solve linear system:", e)

# ------------------------------------------
# 3. PRACTICAL MATRIX OPERATIONS
# ------------------------------------------

print("\n--- Section 3: Practical Matrix Operations ---")

#  1. Create a 4 × 4 matrix C with random integers between 1 and 20:

C = np.random.randint(1, 21, size=(4, 4))
print("Matrix C:\n", C)

# Rank of C
rank_C = np.linalg.matrix_rank(C)
print("Rank of C:", rank_C)

# Submatrix (first 2 rows, last 2 columns)
sub_C = C[:2, -2:]
print("Submatrix of C (first 2 rows, last 2 cols):\n", sub_C)

# Frobenius Norm
fro_norm = np.linalg.norm(C, 'fro')
print("Frobenius Norm of C:", fro_norm)

#  2. Matrix Multiplication A x C_trim
C_trim = C[:3, :3]
print("Trimmed C (3x3):\n", C_trim)

if A.shape[1] == C_trim.shape[0]:
    AC_product = A @ C_trim
    print("A x C_trim:\n", AC_product)
else:
    print("Matrix multiplication not valid due to shape mismatch.")

# ------------------------------------------
# 4. DATA SCIENCE CONTEXT
# ------------------------------------------

print("\n--- Section 4: Data Science Context ---")



D = np.array([[3, 5, 7, 9, 11],
              [2, 4, 6, 8, 10],
              [1, 3, 5, 7, 9],
              [4, 6, 8, 10, 12],
              [5, 7, 9, 11, 13]])
print("Dataset D:\n", D)

# Standardize D
mean = np.mean(D, axis=0)
std = np.std(D, axis=0)
D_std = (D - mean) / std
print("Standardized D:\n", D_std)

# Covariance matrix
cov_matrix = np.cov(D_std, rowvar=False)
print("Covariance Matrix:\n", cov_matrix)

# PCA: Eigen decomposition
eigvals_D, eigvecs_D = np.linalg.eig(cov_matrix)
print("Eigenvalues of covariance matrix:\n", eigvals_D)
print("Eigenvectors:\n", eigvecs_D)

# Reduce to 2 principal components
sorted_indices = np.argsort(eigvals_D)[::-1]
top2_eigvecs = eigvecs_D[:, sorted_indices[:2]]
D_reduced = D_std @ top2_eigvecs
print("Data reduced to 2 principal components:\n", D_reduced)
