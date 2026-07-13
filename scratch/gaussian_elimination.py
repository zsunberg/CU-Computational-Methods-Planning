import numpy as np

def gaussian_elimination(A, b):
    """Solve Ax = b."""

    aug = np.column_stack((A, b))

    forward_elimination_partial_pivot(aug)
    x = back_substitution(aug)

    return x

def back_substitution(tri):
    """Solve Ax = b by back substitution, given augmented matrix tri = [A | b] with A upper triangular."""

    n = tri.shape[0]
    b = tri[:, n]
    a = tri[:, 0:n]

    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i+1:n], x[i+1:n])) / a[i, i]

    return x

def forward_elimination(aug):
    
    n = aug.shape[0]
    
    for col in range(n):
        for row in range(col+1, n):
            factor = aug[row, col]/aug[col,col]
            aug[row, :] -= factor*aug[col,:]

    return None

def forward_elimination_partial_pivot(aug):

    n = aug.shape[0]

    for col in range(n):
        pivot = col + np.argmax(np.abs(aug[col:, col]))
        aug[[col, pivot], :] = aug[[pivot, col], :]
        for row in range(col+1, n):
            factor = aug[row, col]/aug[col,col]
            aug[row, :] -= factor*aug[col,:]

    return None
