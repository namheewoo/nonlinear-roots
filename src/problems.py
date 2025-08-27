import math
from typing import Callable, Optional, Tuple

class Problem:
    """
    Root-finding 문제 정의 클래스
    f: 함수
    df: 도함수 (없으면 None)
    interval: (a,b) 구간 (bisection/false position용)
    x0, x1: 초기값 (Newton, Secant 등 사용)
    name: 문제 이름 
    """
    def __init__(self,
                 f: Callable[[float], float],
                 df: Optional[Callable[[float], float]] = None,
                 interval: Optional[Tuple[float, float]] = None,
                 x0: Optional[float] = None,
                 x1: Optional[float] = None,
                 name: str = "problem"):
        self.f = f
        self.df = df
        self.interval = interval
        self.x0 = x0
        self.x1 = x1
        self.name = name

def pack():
    """
    여러 테스트 문제를 한 번에 반환.
    CLI에서 --problem 옵션으로 선택 가능.
    """
    return [
        # === Easy ===
        # 1. [단순 다항식] x^3 - 2 = 0 (근: ∛2 ≈ 1.2599)
        Problem(
            f=lambda x: x**3 - 2,
            df=lambda x: 3*x**2,
            interval=(0, 2),
            x0=1.0, x1=1.5,
            name="x^3 - 2 (easy)"
        ),

        # 2. [트랜센던트 함수] cos(x) - x = 0  (근: ≈ 0.739085...)
        Problem(
            f=lambda x: math.cos(x) - x,
            df=lambda x: -math.sin(x) - 1,
            interval=(0, 1),
            x0=0.5, x1=0.6,
            name="cos(x) - x (easy)"
        ),

        # 3. exp(-x) - x = 0 (근: ≈ 0.567143... Lambert W 관련)
        Problem(
            f=lambda x: math.exp(-x) - x,
            df=lambda x: -math.exp(-x) - 1,
            interval=(0, 1),
            x0=0.5, x1=0.7,
            name="exp(-x) - x (easy)"
        ),

        # === Medium ===
        # 4. [다중근] (x-1)^2(x+2) = 0 (중근 x=1 ,근 x=-2)
        Problem(
            f=lambda x: (x - 1)**2 * (x + 2),
            df=lambda x: 2*(x - 1)*(x + 2) + (x - 1)**2,
            interval=(-3, 3),
            x0=0.2, x1=1.5,
            name="(x-1)^2(x+2) (double root)"
        ),

        # 5. [비선형+여러 근] sin(x) - x/2 = 0 (근: x=0과 x≈1.895)
        Problem(
            f=lambda x: math.sin(x) - 0.5*x,
            df=lambda x: math.cos(x) - 0.5,
            interval=(0, 3),
            x0=2.0, x1=2.5,
            name="sin(x) - x/2 (medium)"
        ),

        # === Hard ===
        # 6. tanh(10x) = 0, 평탄한 기울기 (근 x = 0) -> 수렴 느림
        Problem(
            f=lambda x: math.tanh(10*x),
            df=lambda x: 10*(1 - math.tanh(10*x)**2),
            interval=(-0.5, 0.5),
            x0=0.1, x1=-0.1,
            name="tanh(10x) (hard flat slope)"
        ),

        # 7. [스케일이 큰 경우] 1e6*x - 1 = 0 (근: ≈ 1e-6)
        Problem(
            f=lambda x: 1e6 * x - 1,
            df=lambda x: 1e6,
            interval=(0, 1),
            x0=0.0, x1=0.1,
            name="1e6*x - 1 (hard scaled)"
        ),
    ]