"""
模块名与文件名只相差一个后缀
首次导入模块：
  1.会产生一个模块的名称空间
  2.执行.py,将执行过程中产生的名字放到模块空间中
  3.在当前执行文件的名称空间中拿到一个模块名，该名字指向模块的名称空间
import 模块                                                               同文件包下访问不同文件                     使用不便，但十分精准
from 模块 import 各种变量名或函数名或类                                       访问不同包下的文件                        使用方便，但容易冲突
from 文件夹 import                            绝对导入                        找到文件夹所在位置就可确定模块             以执行文件为主
from 文件夹.模块名 import 函数           from matplotlib.pyplot import pyplot as plt
相对导入：从当前模块开始算起

只有先导入包后才能使用，      不能在执行文件时使用
调用了包1，结果包1又要调用包2，那么在包1内可以使用相对导入来导入包2                             直接导入包2不就完了吗
from .文件夹 import                      从当前文件夹导入
from ..文件夹 import                     从上一级文件夹导入
from ...文件夹 import                    从上上级文件夹导入

"""

import span
da = span.pri()
print("现在的时间是{0}".format(da))
print(span.da)