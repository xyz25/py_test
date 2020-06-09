import pytest


class TestClass:
    def setup(self):    # 作用域在当前类中
        print("setup func in class ")

    def test_a(self):
        print("test  test_a")
        assert 0

    def test_b(self):
        print("test test_b")
        assert 0

    def teardown(self):     # 作用域在当前类中
        print("teardown  func in class")


def setup():
    print("setup outside")


def test_c():
    print("test test_c")
    assert 0


def test_d():
    print("test test_d")
    assert 0


def teardown():
    print("teardown outside")


if __name__ == '__main__':
    pytest.main(["-s", "test_setup_teardown_fun.py"])
