import random
"""
import re
from bs4 import BeautifulSoup
import requests
line = "收到好友 C-C（x_x；）(1732373074) 的消息: 你好 (-24457316) "
line_1 = "收到群 QQ机器人测试群(736038975) 内 额额(1732373074) 的消息: 你好 (-518732955) "
msg = re.findall(r"收到好友 (.*)\((.*)\) 的消息: (.*) \((.*)\)", line)
print(msg[0])

msg = re.findall(r"收到群 (.*)\((.*)\) 内 (.*)\((.*)\) 的消息: (.*) \((.*)\)",line_1)
print(msg[0])

"""
import subprocess  # 拦截cmd输出使用的库
import re  # 使用正则匹配消息
import threading  # 多线程加快运行速度
import time
import requests  # 进行消息回答的获取以及回复
import pandas as pd  # 准备实现本地词库
from api import news_api  # 实现新闻
from api import music_api  # 实现点歌
from api import api_group_1  # 实现每日一言等
from bs4 import BeautifulSoup




num = random.choice([1,2,3])

print(num)