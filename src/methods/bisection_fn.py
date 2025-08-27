from typing import Callable, Tuple

def bisect(func: Callable[..., float],
           xl: float, xu: float,
           es: float = 0.0001,     # 허용 오차(%), 기본값 0.0001%
           maxit: int = 50,
           *args) -> Tuple[float, float, float, int]:
    """
    bisect: root location using bisection method (MATLAB)
    Returns: root, fx, ea(%), iter
    """
    fl = func(xl, *args)
    fu = func(xu, *args)
    if fl * fu > 0:
        raise ValueError("no sign change: f(xl) and f(xu) must have opposite signs")

    iter_ = 0
    xr = xl
    ea = float("inf")
    fr = fl  # 초기화

    while True:
        xrold = xr
        xr = 0.5 * (xl + xu)        # 중점
        iter_ += 1
        fr = func(xr, *args)

        # 구간 갱신
        if fl * fr < 0:
            xu = xr
            fu = fr
        elif fl * fr > 0:
            xl = xr
            fl = fr
        else:
            ea = 0.0        # 정확히 0이면 바로 종료
            break

        # 상대오차(%) 계산
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100.0

        # 종료 조건 체크
        if ea <= es or iter_ >= maxit:
            break

    root = xr
    fx = fr
    return root, fx, ea, iter_
