from typing import Callable, Optional
from ..core import RootSolver, SolverResult

class Secant(RootSolver):
    def solve(self, f: Callable[[float], float], df: Optional[Callable[[float], float]] = None,
              a: Optional[float] = None, b: Optional[float] = None,
              x0: Optional[float] = None, x1: Optional[float] = None,
              tol: float = 1e-10, maxit: int = 100) -> SolverResult:
        if x0 is None or x1 is None:
            raise ValueError("Secant needs two initial guesses x0, x1.")

        n_f, n_df = 0, 0
        history = [x0, x1]

        f0 = f(x0); f1 = f(x1); n_f += 2

        for iters in range(1, maxit + 1):
            denom = (f1 - f0)
            if denom == 0:
                return SolverResult(x1, False, iters - 1, n_f, n_df, abs(f1), history)

            x2 = x1 - f1 * (x1 - x0) / denom
            fx2 = f(x2); n_f += 1
            history.append(x2)

            if abs(fx2) <= tol or abs(x2 - x1) <= tol:
                return SolverResult(x2, True, iters, n_f, n_df, abs(fx2), history)

            x0, f0 = x1, f1
            x1, f1 = x2, fx2

        return SolverResult(x1, False, maxit, n_f, n_df, abs(f1), history)
