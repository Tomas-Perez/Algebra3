def is_tridiagonal_symmetric(a):
    for i in range(len(a)-1):
        if not a[i+1][i] == a[i][i+1]:
            return False
    return True


def upside_down_gauss(a, b):
    n = len(a)
    for k in range(1, n+1):
        div = a[n-k][n-k]
        for m in range(n):
            a[n-k][m] /= div
        b[n-k] /= div
        for i in range(0, n-k):
            mult = a[i][n-k]
            for j in range(0, n-k+1):
                a[i][j] -= mult*a[n-k][j]
            b[i] -= mult*b[n-k]


def solve_lower_diag(a, b):
    n = len(a)
    result = [0 for _ in range(n)]
    result[0] = b[0]
    for i in range(1, n):
        result[i] = b[i]
        for j in range(0, i):
            result[i] -= a[i][j]*result[j]
    return result


def solve_with_upside_down_gauss(a, b):
    upside_down_gauss(a, b)
    return solve_lower_diag(a, b)


if __name__ == '__main__':
    a = [[0.5, 1.5, 0.7],
         [1, 0, 2],
         [2, 1.2, -0.3]]
    b = [-0.3, 3, 0.5]
    print(solve_with_upside_down_gauss(a, b))

