# !/usr/src/python3
# -*- coding:utf-8 -*-
# Author: Humble test
# @Time: 2019/5/12/16:49

"""
description: 执行所有测试用例
"""

import unittest, os, time
from HTMLTestRunner import HTMLTestRunner_PY3



project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))

# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path + "\\fungoAndroid\\src\\test_case"

# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "\\fungoAndroid\\report\\"

report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())

# 构建测试集,包含src/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(
    start_dir=project_path,
    pattern='test*.py'
)


# 执行测试
if __name__=="__main__":

    report = report_name+"Report.html"
    fb = open(report,'wb')
    runner = HTMLTestRunner_PY3.HTMLTestRunner(
        stream=fb,
        verbosity=1,
        title=r'APP自动化测试报告',
        description=r'项目描述：uat环境'
    )
    runner.run(suite)
    fb.close()