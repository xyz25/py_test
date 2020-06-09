# py_test

***



## 安装 

`pip install pytest`

***



## 在第n个错误后停止测试

```python
pytest -x  # 在第一个错误后停止测试
pytest --maxfail=2 # 在第二个错误处停止 （=左右不能有空格）
```

***



## 指定测试、选择测试

```python
pytest test_a.py 	# 指定测试当前目录下的test_a.py 文件
pytest ./tests # 测试tests目录下的文件

# 按照节点测试
pytest test_1.py::test_answer # 测试test_1.py中的test_answer（可以是函数，类等）
pytest test_class.py::TestClass::test_two # 测试test_class.py中的Testclass中的test_two方法
        
# 按照标记测试

```



***



## Pytest的setup和teardown函数

### 函数级别setup()/teardown()

<small>运行于测试方法的始末，即运行一次测试函数就会运行一次setup函数和teardown函数</small>

```python
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

"""
test_setup_teardown_fun.py 
setup func in class 
test  test_a
Fteardown  func in class
setup func in class 
test test_b
Fteardown  func in class
setup outside
test test_c
Fteardown outside
setup outside
test test_d
Fteardown outside
"""
```



### 类级别setup_class() / teardown_class()

<small>类级别的setup_class和teardown_class只会在测试类的时候前后运行一次，不在乎其中的测试函数的运行</small>

```python
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
    
    
"""
test_setup_teardown_class.py 
setup_class  
test  test_a
Ftest test_b
Fteardown_class
"""

```



***



## pytest配置文件

`pytest.ini`

```python
# pytest的配置文件  一般放在测试目录下

# 配置pytest命令行运行参数
[pytest]
# 空格分割，可添加多个命令行参数 所有参数均为插件包的参数配置测试搜索的路径
addopts = -s --html=./report.html
# addopts = -s --maxfail=1 / -x 出现一个错误时停止测试

# 测试目录为当前文件夹的scripts文件    -可自定义
testpaths = ./

# 配置测试匹配搜索的文件名称  测试目录下的以test开头，.py结尾的文件
python_files = test*.py

# 配置测试匹配的 测试类 名  以Test 开头的所有类
python_classes = Test*

# 配置测试匹配的 测试函数 名 以test_开头的函数名，以Test 开头的类中的 以test_开头的方法
python_functions = test_*
```

***
## pytest测试报告
`pip install pytest-html` <br>
使用方法：`pytest --html=./report.html` 或者`addopts = -s --html=./report.html`<br>
结果：执行`pytest`之后会在. 目录下生成report.html 和asserts文件夹（style.css）
***

## pytest之fixture的使用



