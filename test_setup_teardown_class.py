import pytest


class TestClass:
    def setup_class(self):    # 作用域在当前类中
        print("setup_class  ")

    def test_a(self):
        print("test  test_a")
        assert 0

    def test_b(self):
        print("test test_b")
        assert 0

    def teardown_class(self):     # 作用域在当前类中
        print("teardown_class")


if __name__ == '__main__':
    pytest.main(["-s", "test_setup_teardown_class.py"])
