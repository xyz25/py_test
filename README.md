# py_test

## 安装 
`pip install pytest`

## `pytest.ini` 配置文件
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

