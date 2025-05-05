{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d9594151-79fe-42e5-99bc-8f6c44ccb374",
   "metadata": {},
   "source": [
    "## Assignment_5"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd86cb7b-6347-441f-b70d-ec1f40e4080b",
   "metadata": {},
   "source": [
    "## Matrix and Vector Operations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cbe8f61a-eb9b-4a67-9313-adc62824daf7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "96fb1f42-a19a-446a-8f91-739e029f5ef6",
   "metadata": {},
   "source": [
    "### 1. Create a 3 × 3 matrix A and a 3 × 1 vector B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "id": "bbde8985-ce90-4ec0-8665-f24a291594e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix A:\n",
      " [[1 2 3]\n",
      " [4 5 6]\n",
      " [7 8 9]]\n",
      "Vector B:\n",
      " [1 2 3]\n"
     ]
    }
   ],
   "source": [
    "A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])\n",
    "B = np.array([1, 2, 3])\n",
    "\n",
    "print(\"Matrix A:\\n\", A)\n",
    "print(\"Vector B:\\n\", B)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33b117a1-80d7-4763-919c-53724089eba8",
   "metadata": {},
   "source": [
    "***(a). Perform matrix-vector multiplication  A X B***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "5141fab3-0839-43e0-b3f4-70ca86881567",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A x B =\n",
      " [14 32 50]\n"
     ]
    }
   ],
   "source": [
    "product = A @ B\n",
    "print(\"A x B =\\n\", product)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "84623314-7ff9-4f08-acb1-0f3ae885c5fd",
   "metadata": {},
   "source": [
    "***(b). Calculate the trace of matrix  A  (sum of diagonal elements)***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "2d62e7f4-0a9d-45b0-b88d-1ef247e8231f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Trace of A = 15\n"
     ]
    }
   ],
   "source": [
    "trace_A = np.trace(A)\n",
    "print(\"Trace of A =\", trace_A)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b45e5cc-f0a1-4205-9ac9-0028e1670a81",
   "metadata": {},
   "source": [
    "***(c). Find the eigenvalues and eigenvectors of A***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5a1dd220-855a-4fca-9903-7fee32a98af5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eigenvalues of A:\n",
      " [ 1.61168440e+01 -1.11684397e+00 -3.38433605e-16]\n",
      "Eigenvectors of A:\n",
      " [[-0.23197069 -0.78583024  0.40824829]\n",
      " [-0.52532209 -0.08675134 -0.81649658]\n",
      " [-0.8186735   0.61232756  0.40824829]]\n"
     ]
    }
   ],
   "source": [
    "eigvals, eigvecs = np.linalg.eig(A)\n",
    "print(\"Eigenvalues of A:\\n\", eigvals)\n",
    "print(\"Eigenvectors of A:\\n\", eigvecs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "338b675c-8be4-4fce-8dae-e31b011d651b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c4dc2288-f164-44ea-99c1-08b3e7cdcf2c",
   "metadata": {},
   "source": [
    "### 2. Replace the last row of matrix A with [10, 11, 12]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "a3b62dbf-7a42-414c-a7fc-64e5a90fa8ae",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Updated Matrix A:\n",
      " [[ 1  2  3]\n",
      " [ 4  5  6]\n",
      " [10 11 12]]\n"
     ]
    }
   ],
   "source": [
    "A[2] = [10, 11, 12]\n",
    "print(\"Updated Matrix A:\\n\", A)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32c79b4e-205c-4855-9297-2ad2abf78902",
   "metadata": {},
   "source": [
    "***(a). Compute the determinant of the updated matrix A***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "03eb57dc-413e-44f1-8e88-b9f9a6655bf9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Determinant of updated A = 2.86437540353291e-15\n"
     ]
    }
   ],
   "source": [
    "# Determinant and Singularity\n",
    "try:\n",
    "    det_A = np.linalg.det(A)\n",
    "    print(\"Determinant of updated A =\", det_A)\n",
    "except LinAlgError as e:\n",
    "    print(\"Error computing determinant:\", e)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f44c8f1-0a65-431e-936e-a33256627880",
   "metadata": {},
   "source": [
    "***(b). Identify if the updated matrix is singular or non-singular***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "6da4d297-0b20-4e5b-a41f-8561e734c426",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Updated matrix A is singular.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    if np.isclose(det_A, 0):\n",
    "        print(\"Updated matrix A is singular.\")\n",
    "    else:\n",
    "        print(\"Updated matrix A is non-singular.\")\n",
    "except LinAlgError as e:\n",
    "    print(\"Error computing determinant:\", e)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05772800-eb5f-47f3-ad00-04a6dcabc151",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "4ce1ef38-00ec-46fd-ac02-abec4b103de0",
   "metadata": {},
   "source": [
    "## Invertibility of Matrices "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "ca538268-4f03-43cc-b1d6-0dd4f0c815ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix A is not invertible. Skipping inverse and solve.\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    if not np.isclose(det_A, 0):\n",
    "        inv_A = np.linalg.inv(A)\n",
    "        print(\"Inverse of updated A:\\n\", inv_A)\n",
    "\n",
    "        # Solve A·X = B\n",
    "        X = np.linalg.solve(A, B)\n",
    "        print(\"Solution X for A·X = B:\\n\", X)\n",
    "    else:\n",
    "        print(\"Matrix A is not invertible. Skipping inverse and solve.\")\n",
    "except LinAlgError as e:\n",
    "    print(\"Linear algebra error:\", e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2bceb18-3704-41a5-924b-f3deaa156e5d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "59cbf7c5-8ce5-405b-8070-00410ff9d514",
   "metadata": {},
   "source": [
    "## Practical Matrix Operations"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7c557639-e303-4b84-82d9-9c90a351a77f",
   "metadata": {},
   "source": [
    "***1. Create a 4 × 4 matrix C with random integers between 1 and 20:***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "5d683100-519e-4446-97f9-9c9044f3271d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random 4x4 Matrix C:\n",
      " [[11 14 13  2]\n",
      " [14 11 10 13]\n",
      " [ 4  3  5 11]\n",
      " [17  4 17 11]]\n"
     ]
    }
   ],
   "source": [
    "C = np.random.randint(1, 21, size=(4, 4))\n",
    "print(\"Random 4x4 Matrix C:\\n\", C)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43034217-c3f1-42e0-b2a1-3f8c24331b0a",
   "metadata": {},
   "source": [
    "***1(a). Compute the rank of C***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "a1c84c2e-1039-4742-8718-ea472513b05d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rank of C = 4\n"
     ]
    }
   ],
   "source": [
    "rank_C = np.linalg.matrix_rank(C)\n",
    "print(\"Rank of C =\", rank_C)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "00a0f222-7405-4b59-a7da-cec85be18fbb",
   "metadata": {},
   "source": [
    "***1(b). Extract the submatrix consisting of the first 2 rows and last 2 columns of C***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "52d9c0f9-874c-4969-a919-f0da6a27aef6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Submatrix (first 2 rows, last 2 cols):\n",
      " [[16  6]\n",
      " [ 4 16]]\n"
     ]
    }
   ],
   "source": [
    "sub_C = C[:2, -2:]\n",
    "print(\"Submatrix (first 2 rows, last 2 cols):\\n\", sub_C)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4c1649db-c2a5-41f2-a96d-0b2cc8475f95",
   "metadata": {},
   "source": [
    "***1(c).Calculate the Frobenius norm of C***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "c20a8f06-8807-4737-914c-5116587160aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Frobenius norm of C = 47.4236228055175\n"
     ]
    }
   ],
   "source": [
    "norm_C = np.linalg.norm(C, 'fro')\n",
    "print(\"Frobenius norm of C =\", norm_C)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "658e1ce4-8295-4e84-be05-69f598827087",
   "metadata": {},
   "source": [
    "### 2. Perform matrix multiplication between A (updated to 3 × 3) and C (trimmed to 3 × 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "6846985f-faef-4937-9d84-50c501b05784",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Trimmed C to 3x3:\n",
      " [[20  2 16]\n",
      " [ 2 14  4]\n",
      " [ 3 18 11]]\n"
     ]
    }
   ],
   "source": [
    "if C.shape != (3, 3):\n",
    "    C_trimmed = C[:3, :3]\n",
    "    print(\"Trimmed C to 3x3:\\n\", C_trimmed)\n",
    "else:\n",
    "    C_trimmed = C\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "47384187-6518-4431-8fbd-982b5a9b1e55",
   "metadata": {},
   "source": [
    "***2(a). Check if the multiplication is valid. If not, reshape C to make it compatible with A***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "bef4c98d-0955-460f-ba26-dc975c47eadb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A × C_trimmed =\n",
      " [[ 33  84  57]\n",
      " [108 186 150]\n",
      " [258 390 336]]\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    result_AC = A @ C_trimmed\n",
    "    print(\"A × C_trimmed =\\n\", result_AC)\n",
    "except ValueError as e:\n",
    "    print(\"Matrix multiplication error:\", e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66b2ae5a-fdfe-4f5c-bbf0-53fb9cb42d72",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "6f240fb4-44e2-41fd-af1b-c96e87d51e3c",
   "metadata": {},
   "source": [
    "## Data Science Context"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee48e33e-94c7-4cb1-b8e7-c85dac6f368a",
   "metadata": {},
   "source": [
    "***1. Create a dataset as a 5 × 5 matrix D, where each column represents a feature, and each row represents a data point:***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ed2c6cb0-261e-4881-b7f2-339f9aed0a4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original Dataset D:\n",
      " [[ 3  5  7  9 11]\n",
      " [ 2  4  6  8 10]\n",
      " [ 1  3  5  7  9]\n",
      " [ 4  6  8 10 12]\n",
      " [ 5  7  9 11 13]]\n"
     ]
    }
   ],
   "source": [
    "D = np.array([[3, 5, 7, 9, 11],\n",
    "              [2, 4, 6, 8, 10],\n",
    "              [1, 3, 5, 7, 9],\n",
    "              [4, 6, 8, 10, 12],\n",
    "              [5, 7, 9, 11, 13]])\n",
    "\n",
    "print(\"Original Dataset D:\\n\", D)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "23e82a5c-ebc7-499e-9c5e-fbc6e577e3f4",
   "metadata": {},
   "source": [
    "***1(a). Standardize D column-wise (mean = 0, variance = 1)***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "25707972-dd36-4d4b-9b93-e92b85727366",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Standardized D:\n",
      " [[ 0.          0.          0.          0.          0.        ]\n",
      " [-0.70710678 -0.70710678 -0.70710678 -0.70710678 -0.70710678]\n",
      " [-1.41421356 -1.41421356 -1.41421356 -1.41421356 -1.41421356]\n",
      " [ 0.70710678  0.70710678  0.70710678  0.70710678  0.70710678]\n",
      " [ 1.41421356  1.41421356  1.41421356  1.41421356  1.41421356]]\n"
     ]
    }
   ],
   "source": [
    "D_mean = np.mean(D, axis=0)\n",
    "D_std = np.std(D, axis=0)\n",
    "D_stdized = (D - D_mean) / D_std\n",
    "print(\"Standardized D:\\n\", D_stdized)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b8ff9f60-25a8-4948-9baa-9678b7967359",
   "metadata": {},
   "source": [
    "***1(b). Compute the covariance matrix of D***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "109b27e8-2dce-4655-aa4f-8669b0ba540b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Covariance Matrix of D:\n",
      " [[1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]\n",
      " [1.25 1.25 1.25 1.25 1.25]]\n"
     ]
    }
   ],
   "source": [
    "cov_D = np.cov(D_stdized.T)\n",
    "print(\"Covariance Matrix of D:\\n\", cov_D)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c14c25a0-c516-4fce-9051-f673d42370fa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "bf43f803-415c-4322-bbc4-ad82387cc7c8",
   "metadata": {},
   "source": [
    "### Principal Component Analysis (PCA)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3bc7a672-1892-41bb-86ed-9030a07e29a9",
   "metadata": {},
   "source": [
    "***Find the eigenvalues and eigenvectors of the covariance matrix***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "162cefdb-92fd-4e9b-b277-271442341b3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eigenvalues:\n",
      " [ 6.25000000e+00 -3.69778549e-32 -4.19340966e-17  0.00000000e+00\n",
      " -2.28523622e-64]\n",
      "Eigenvectors:\n",
      " [[ 4.47213595e-01 -2.01000734e-16 -3.25055279e-01 -4.98525175e-49\n",
      "   8.98516042e-34]\n",
      " [ 4.47213595e-01  8.66025404e-01  8.88074128e-01  5.96701066e-33\n",
      "  -1.29791556e-17]\n",
      " [ 4.47213595e-01 -2.88675135e-01 -1.87672950e-01 -5.16969603e-16\n",
      "   8.16496581e-01]\n",
      " [ 4.47213595e-01 -2.88675135e-01 -1.87672950e-01 -7.07106781e-01\n",
      "  -4.08248290e-01]\n",
      " [ 4.47213595e-01 -2.88675135e-01 -1.87672950e-01  7.07106781e-01\n",
      "  -4.08248290e-01]]\n"
     ]
    }
   ],
   "source": [
    "eigvals_D, eigvecs_D = np.linalg.eig(cov_D)\n",
    "print(\"Eigenvalues:\\n\", eigvals_D)\n",
    "print(\"Eigenvectors:\\n\", eigvecs_D)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "85b4dfa9-2476-4204-85e6-f9db2a9ca5df",
   "metadata": {},
   "source": [
    "***Reduce D to 2 principal components***"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "7a5fcaaf-8f77-4d80-86d1-2215b2247a41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "D reduced to 2 principal components:\n",
      " [[ 0.00000000e+00  0.00000000e+00]\n",
      " [-1.58113883e+00 -3.58404070e-17]\n",
      " [-3.16227766e+00 -7.16808141e-17]\n",
      " [ 1.58113883e+00  3.58404070e-17]\n",
      " [ 3.16227766e+00  7.16808141e-17]]\n"
     ]
    }
   ],
   "source": [
    "sorted_indices = np.argsort(eigvals_D)[::-1]\n",
    "top2_eigvecs = eigvecs_D[:, sorted_indices[:2]]\n",
    "D_reduced = D_stdized @ top2_eigvecs\n",
    "print(\"D reduced to 2 principal components:\\n\", D_reduced)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
