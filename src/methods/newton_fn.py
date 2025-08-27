from typing import Callable, Tuple

def Newton(f: Callable[[float], float],
         df: Callable[[float], float],
         x0: float,
         es: float = 1.0e-6,       # 원하는 오차 (기본값 1e-6)
         maxit: int = 50
         ) -> Tuple[float, float, float, int]:
    """
    Newton method (MATLAB)
    반환값: (root, f(root), ea, iter)
    """
    if f is None or df is None or x0 is None:
        raise ValueError("at least 3 input arguments required")

    xr = x0
    iters = 0
    ea = float("inf")

    while True:
        xrold = xr
        xr = xrold - f(xrold) / df(xrold)  # Newton 갱신
        iter_ += 1

        if xr != 0:
            ea = abs(xr - xrold)

        # 종료 조건
        if ea <= es or iters >= maxit:
            break

    root = xr
    fx = f(xr)
    return root, fx, ea, iters

