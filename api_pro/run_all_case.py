# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 21:02
# @Author  : 边笑天
# @File    : run_all_case.py
# @Software: PyCharm

import unittest
from common import HTMLTestRunner

casePath = "E:\\pycharm\\api_pro\\case"  #指定测试用例存放路径
discover = unittest.defaultTestLoader.discover(casePath, "test*.py")  #使用unittest框架加载测试用例文件，执行用例

reportPath = "E:\\pycharm\\api_pro\\report\\"+"result.html"  #指定测试报告存放路径，并且将生成的html测试报告放入该路径

fp = open(reportPath,"wb")  #以二进制流覆盖写入模式打开测试报告文件

runner = HTMLTestRunner.HTMLTestRunner(fp,title="北斗星接口自动化测试报告",description="报告描述",verbosity=2,)  #实例化htmltestrunner方法，并传入对应参数
runner.run(discover)  #调用实例方法run，运行用例执行
#fp.close()  #关闭测试报告文件