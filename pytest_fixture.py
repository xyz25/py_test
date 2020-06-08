"""
pytest.fixture装饰器来标记固定的函数和方法或者类
被装饰的函数可在其他函数、类、模块，甚至整个项目调用之前，被执行，一般用于完成预置处理和重复操作
"""
import pytest


class TestABC:
    @pytest.fixture  # 使用pytest.fixture装饰
    def before(self) -> None:
        print('before----')

    def test_a(self, before):  # 传入被pytest.fixture装饰的函数before 在当前函数被测试之前，执行before函数
        print("test test_a func ")
        assert 0  # 断言


@pytest.fixture
def before1():
    print("before2----")


@pytest.mark.usefixtures("before1")  # 使用装饰器为类 、函数、方法添加fixture测试
def test_b():
    print("test_b----")
    assert 0


if __name__ == '__main__':
    pytest.main(["-s",  "pytest_fixture.py"])  # main([指令])
