from typing import Callable, Tuple

def Secant(f: Callable[[float], float],
          x0: float,
          x1: float,
          es: float = 1.0e-6,
          maxit: int = 50) -> Tuple[float, float, float, int]:
    """
    Secant method (MATLAB)
    반환값: (root, f(root), ea, iters)
    """
    if f is None or x0 is None or x1 is None:
        raise ValueError("at least 3 input arguments required")

    iters = 0
    ea = float("inf")

    while True:
        f0 = f(x0)
        f1 = f(x1)

        if f1 - f0 == 0:
            raise ZeroDivisionError("Secant method failed: denominator = 0")

        xr = x1 - f1 * (x1 - x0) / (f1 - f0)
        iters += 1

        if xr != 0:
            ea = abs(xr - x1)

        # 종료 조건
        if ea <= es or iters >= maxit:
            break

        # 업데이트
        x0, x1 = x1, xr

    root = xr
    fx = f(root)
    return root, fx, ea, iters
