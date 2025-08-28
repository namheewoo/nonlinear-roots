from typing import Callable, Optional
from ..core import RootSolver, SolverResult

class Newton(RootSolver):
    def solve(self, f: Callable[[float], float], df: Optional[Callable[[float], float]] = None,
              a: Optional[float] = None, b: Optional[float] = None,
              x0: Optional[float] = None, x1: Optional[float] = None,
              tol: float = 1e-10, maxit: int = 100) -> SolverResult:
        if x0 is None:
            raise ValueError("Newton needs initial guess x0.")
        if df is None:
            raise ValueError("Newton needs derivative function df.")

        x = x0
        n_f, n_df = 0, 0
        history = [x]

        for iters in range(1, maxit + 1):
            fx = f(x); n_f += 1
            dfx = df(x); n_df += 1
            if dfx == 0:
                return SolverResult(x, False, iters - 1, n_f, n_df, abs(fx), history)

            x_new = x - fx / dfx
            history.append(x_new)

            if abs(fx) <= tol or abs(x_new - x) <= tol:
                return SolverResult(x_new, True, iters, n_f, n_df, abs(fx), history)

            x = x_new

        fx = f(x); n_f += 1
        return SolverResult(x, False, maxit, n_f, n_df, abs(fx), history)
