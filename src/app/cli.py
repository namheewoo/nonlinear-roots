import argparse
from src.methods.bisection_adapter import BisectionMATLABLike
from src.methods.newton import Newton
from src.methods.secant import Secant
from src.problems import pack

SOLVERS = {
    "bisection": BisectionMATLABLike(),
    "newton": Newton(),
    "secant": Secant(),
}

def list_problems():
    problems = pack()
    print("Available problems:")
    for i, p in enumerate(problems):
        print(f"  [{i}] {p.name}")

def list_methods():
    print("Available methods:")
    for k in SOLVERS.keys():
        print(f"  - {k}")

def main():
    parser = argparse.ArgumentParser(description="Nonlinear root finding demo")
    parser.add_argument("--method", choices=SOLVERS.keys(), default="bisection",
                        help="solver method")
    parser.add_argument("--problem", type=int, default=0,
                        help="index of problem from pack()")
    parser.add_argument("--tol", type=float, default=1e-10, help="tolerance")
    parser.add_argument("--maxit", type=int, default=100, help="max iterations")
    parser.add_argument("--list", action="store_true",
                        help="list available problems and exit")
    parser.add_argument("--list-methods", action="store_true",
                        help="list available methods and exit")
    args = parser.parse_args()

    if args.list:
        list_problems()
        return

    if args.list_methods:
        list_methods()
        return

    problems = pack()
    if not (0 <= args.problem < len(problems)):
        raise IndexError(f"--problem must be in [0, {len(problems)-1}]")

    prob = problems[args.problem]
    solver = SOLVERS[args.method]

    kwargs = {"tol": args.tol, "maxit": args.maxit}
    if args.method == "bisection":
        a, b = prob.interval
        res = solver.solve(prob.f, a=a, b=b, **kwargs)
    elif args.method == "newton":
        res = solver.solve(prob.f, df=prob.df, x0=prob.x0, **kwargs)
    else:  # secant
        res = solver.solve(prob.f, x0=prob.x0, x1=prob.x1, **kwargs)

    print(f"[{prob.name}] {args.method} -> converged={res.converged}, "
          f"root={res.root:.12g}, iters={res.iters}, "
          f"Nf={res.n_f}, Ndf={res.n_df}, residual={res.residual:.2e}")

if __name__ == "__main__":
    main()

