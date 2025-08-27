from typing import Callable, Optional
from ..core import RootSolver, SolverResult
from .newton_fn import mynt

class NewtonMATLABLike(RootSolver):
    def solve(self, f: Callable[[float], float], df: Optional[Callable[[float], float]] = None,
              a: Optional[float] = None, b: Optional[float] = None,
              x0: Optional[float] = None, x1: Optional[float] = None,
              tol: float = 1e-10, maxit: int = 100) -> SolverResult:
        if x0 is None:
            raise ValueError("Newton needs an initial guess x0.")
        if df is None:
            raise ValueError("Newton needs derivative df.")

        # mynt는 절대오차(es) -> tol 그대로 전달
        root, fx, ea, iters = mynt(f, df, x0, es=tol, maxit=maxit)

        # 함수 평가 수 추정: 각 반복마다 f, df 한 번 → 대략 2*iters
        n_f = iters
        n_df = iters

        return SolverResult(
            root=root,
            converged=(ea <= tol),
            iters=iters,
            n_f=n_f,
            n_df=n_df,
            residual=abs(fx),
            history=[]
        )
