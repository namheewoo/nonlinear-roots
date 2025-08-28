from typing import Callable, Optional
from ..core import RootSolver, SolverResult
from .secant_fn import Secant as secant_fn  

class SecantMATLABLike(RootSolver):
    def solve(self, f: Callable[[float], float], df: Optional[Callable[[float], float]] = None,
              a: Optional[float] = None, b: Optional[float] = None,
              x0: Optional[float] = None, x1: Optional[float] = None,
              tol: float = 1e-10, maxit: int = 100) -> SolverResult:
        if x0 is None or x1 is None:
            raise ValueError("Secant needs two initial guesses x0, x1.")

        root, fx, ea, iters = secant_fn(f, x0, x1, es=tol, maxit=maxit)

        # 반복마다 f 평가 1회로 가정
        n_f = iters
        n_df = 0

        return SolverResult(
            root=root,
            converged=(ea <= tol),
            iters=iters,
            n_f=n_f,
            n_df=n_df,
            residual=abs(fx),
            history=[]
        )
