from dataclasses import dataclass
from typing import Callable, Optional, List

@dataclass
class SolverResult:
    root: Optional[float]
    converged: bool
    iters: int
    n_f: int
    n_df: int
    residual: float
    history: List[float]

class RootSolver:
    def solve(
        self,
        f: Callable[[float], float],
        df: Optional[Callable[[float], float]] = None,
        a: Optional[float] = None,
        b: Optional[float] = None,
        x0: Optional[float] = None,
        x1: Optional[float] = None,
        tol: float = 1e-10,
        maxit: int = 100,
    ) -> SolverResult:
        raise NotImplementedError("Implement in subclass")