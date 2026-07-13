import numpy as np

from gaussian_elimination import back_substitution, forward_elimination


def test_back_substitution_upper_triangular():
    # [A | b] already upper triangular: 2x + y = 5, 3y = 9  ->  y=3, x=1
    tri = np.array([[2.0, 1.0, 5.0], [0.0, 3.0, 9.0]])
    x = back_substitution(tri)
    np.testing.assert_allclose(x, [1.0, 3.0])


def test_forward_elimination_zeros_below_diagonal():
    # x + y = 3, 2x + 3y = 8  ->  eliminate to upper triangular
    aug = np.array([[1.0, 1.0, 3.0], [2.0, 3.0, 8.0]])
    forward_elimination(aug)
    # subtracting 2*row0 from row1 zeros the (1,0) entry
    np.testing.assert_allclose(aug, [[1.0, 1.0, 3.0], [0.0, 1.0, 2.0]])


def test_forward_elimination_3x3():
    # 3x3 system; check the subdiagonal is zeroed out
    aug = np.array([
        [2.0, 1.0, -1.0, 8.0],
        [-3.0, -1.0, 2.0, -11.0],
        [-2.0, 1.0, 2.0, -3.0],
    ])
    forward_elimination(aug)
    # everything strictly below the diagonal of A should be ~0
    np.testing.assert_allclose(np.tril(aug[:, :3], -1), np.zeros((3, 3)), atol=1e-12)


def test_forward_then_back_solves_system():
    # end-to-end: 2x + y - z = 8, -3x - y + 2z = -11, -2x + y + 2z = -3
    # known solution x=2, y=3, z=-1
    aug = np.array([
        [2.0, 1.0, -1.0, 8.0],
        [-3.0, -1.0, 2.0, -11.0],
        [-2.0, 1.0, 2.0, -3.0],
    ])
    forward_elimination(aug)
    x = back_substitution(aug)
    np.testing.assert_allclose(x, [2.0, 3.0, -1.0])
