# WEB UI Automation --Basic Practice Version
Python Selenium Cucumber 

```shell
$ Commons : 仅联系版本--随心情更新
```

## 特点
三层调用：Feature-->Step-->Page

### 基础框架构成：
* Features: 存放用例
* Steps ： 存放用例所调用到的方法名
* Pages ： 存放方法的具体实现逻辑
* Function ：公用方法的封装
* Browser.py ： 基类，所有用例均会调用Browser中的方法，且其中还存放一些对Selenium基础函数的二次封装
* Environment.py ：环境变量
* Config.py : 各项配置，项目中切换脚本运行环境可直接update environment一个变量即可

