from typing import Callable, Optional
from ..core import RootSolver, SolverResult

class Bisection(RootSolver):
    def solve(self, f: Callable[[float], float], df: Optional[Callable[[float], float]] = None,
              a: Optional[float] = None, b: Optional[float] = None,
              x0: Optional[float] = None, x1: Optional[float] = None,
              tol: float = 1e-10, maxit: int = 100) -> SolverResult:
        if a is None or b is None:
            raise ValueError("Bisection needs interval [a,b].")
        left, right = a, b
        fl, fr = f(left), f(right)
        n_f, n_df = 2, 0
        if fl == 0.0:
            return SolverResult(left, True, 0, n_f, n_df, 0.0, [left])
        if fr == 0.0:
            return SolverResult(right, True, 0, n_f, n_df, 0.0, [right])
        if fl * fr > 0:
            raise ValueError("Bisection: f(a), f(b) must have opposite signs")
        history = []
        for iters in range(1, maxit + 1):
            mid = 0.5 * (left + right)
            fm = f(mid); n_f += 1
            history.append(mid)

            # 정지 조건
            if abs(fm) <= tol or 0.5 * abs(right - left) <= tol:
                return SolverResult(mid, True, iters, n_f, n_df, abs(fm), history)

            # 구간 갱신
            if fl * fm < 0:
                right, fr = mid, fm
            else:
                left, fl = mid, fm

        # 최대 반복 도달 -> 마지막 중점 반환
        mid = 0.5 * (left + right)
        fm = f(mid); n_f += 1
        history.append(mid)
        return SolverResult(mid, False, maxit, n_f, n_df, abs(fm), history)
