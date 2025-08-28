from .bisection import Bisection as BisectionSolver
from .newton import Newton as NewtonSolver
from .secant import Secant as SecantSolver      #OPP

from .bisect_fn import bisect as BisectFunction
from .newton_fn import Newton as NewtonFunction      
from .secant_fn import Secant as SecantFunction    #function

from .bisection_adapter import BisectionMATLABLike as BisectionAdapter
from .newton_adapter import NewtonMATLABLike as NewtonAdapter
from .secant_adapter import SecantMATLABLike as SecantAdapter  # Adapters

def solvers(matlab_mode: bool = False):
    if matlab_mode:
        return {
            "bisection": BisectionAdapter(),
            "newton":    NewtonAdapter(),
            "secant":    SecantAdapter()
        }
    return {
        "bisection": BisectionSolver(),
        "newton":    NewtonSolver(),
        "secant":    SecantSolver()
    }

__all__ = [
    "BisectionSolver", "NewtonSolver", "SecantSolver",
    "BisectFunction", "NewtonFunction", "SecantFunction",
    "BisectionAdapter", "NewtonAdapter", "SecantAdapter",
    "solvers"
]
