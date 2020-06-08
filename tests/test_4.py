import pytest


@pytest.mark.serial   # 需要在pytest.ini中的markers中声明slow
def func():
    print("test func")
    assert 0


@pytest.mark.slow
def func2():
    print(' test func2')
    assert 0