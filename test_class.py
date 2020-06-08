# 执行类中的测试
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print(tmpdir)
    print('-s  会打印出函数或者方法中的打印语句内容')
    assert 0

