
import math
import pytest
from src.methods.bisect_fn import bisect

def test_bisect_simple_polynomial():
    # f(x) = x^3 - 2, 근 ∛2 ≈ 1.259921
    root, fx, ea, iters = bisect(lambda x: x**3 - 2, 0.0, 2.0,
                                 es=0.001, maxit=100)
    # 근 위치 확인
    assert abs(root - 2**(1/3)) < 1e-3
    # 함수값이 충분히 작아야 함
    assert abs(fx) < 1e-3
    # 상대오차가 설정값 이하인지 확인
    assert ea <= 0.001 or iters >= 100
    # 반복 횟수가 0이면 안됨
    assert iters > 0

def test_bisect_cos_minus_x():
    # f(x) = cos(x) - x, 근 약 0.739085
    root, fx, ea, iters = bisect(lambda x: math.cos(x) - x, 0.0, 1.0,
                                 es=0.001, maxit=100)
    assert abs(root - 0.739085) < 1e-3
    assert abs(fx) < 1e-3
    assert ea <= 0.001 or iters >= 100
    assert iters > 0

def test_bisect_invalid_interval():
    # f(x) = x^2+1은 [0,1]에서 부호 변화 없음 -> 에러 발생
    with pytest.raises(ValueError):
        bisect(lambda x: x**2 + 1, 0.0, 1.0)