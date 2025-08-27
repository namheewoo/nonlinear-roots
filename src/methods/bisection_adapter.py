from typing import Callable, Optional
from ..core import RootSolver, SolverResult
from .bisect_fn import bisect

class BisectionMATLABLike(RootSolver):
    def solve(self, f: Callable[[float], float], df: Optional[Callable[[float], float]] = None,
              a: Optional[float] = None, b: Optional[float] = None,
              x0: Optional[float] = None, x1: Optional[float] = None,
              tol: float = 1e-10, maxit: int = 100) -> SolverResult:
        if a is None or b is None:
            raise ValueError("Bisection needs interval [a,b].")

        # tol은 절대 오차, bisect_fn은 상대오차(%)를 받으므로 변환
        es_percent = tol * 100.0

        #bisect() 함수 호출
        root, fx, ea_percent, iters = bisect(f, a, b, es=es_percent, maxit=maxit)

        # 함수평가 수(n_f): 대략적인 함수 평가 횟수 추정 (초기 2회 + 반복 횟수)
        n_f = 2 + iters

        return SolverResult(
            root=root,
            converged=(ea_percent <= es_percent),
            iters=iters,
            n_f=n_f,
            n_df=0,
            residual=abs(fx),
            history=[]  # 필요하면 bisect()에서 히스토리 리스트를 반환하도록 확장
        )
