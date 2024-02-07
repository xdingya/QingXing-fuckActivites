 # 中国青星活动抢票助手

## 前言
这是我第一个 Python 作品 <u>第一个就这么刑ヾ(≧▽≦*)o</u> 不喜勿喷！玻璃心~ 

## 简介

本项目旨在帮助用户自动化参与中国青星（HNQX）的活动报名，提高抢票成功率。通过使用Python脚本，用户可以避免因手速或网速慢而错过活动报名。此脚本适用于所有基于DTcms系统的活动报名。

## 安装与配置

### 安装依赖

确保你已经安装了Python和pip。然后，安装所需的库：

```bash
pip install requests
pip install BeautifulSoup
```

### 配置脚本

在脚本中，你需要配置以下参数：

- `username`: 你的登录用户名。
- `password`: 你的登录密码。
- `activityID`: 你想要报名的活动ID。

```python
##### 配置面板 #####
username = "your_username"
password = "your_password"
activityID = "your_activity_id"
##### ###### #####
```

## 使用方法

1. 将上述配置中的`your_username`、`your_password`和`your_activity_id`替换为你的实际信息。
2. 运行脚本。

## 注意事项

- 本脚本在尝试报名时会不断重试，直到成功或遇到错误。
- 如果活动已发布或被删除，脚本会相应地输出提示信息。
- 请确保你的网络连接稳定，以避免因网络问题导致的错误。
- 使用此脚本时，请遵守相关法律法规和网站的使用条款。

## 代码示例

```python
import requests
import time
from fun import *

##### 配置面板 #####
username = "your_username"
password = "your_password"
activityID = "your_activity_id"
##### ###### #####

# 登录并获取cookies
with requests.Session() as session:
    # ... 登录逻辑 ...

# 活动报名逻辑
# ... 报名逻辑 ...

# 活动信息输出
# ... 输出逻辑 ...

# 异常处理
# ... 异常处理逻辑 ...
```

## 免责声明

本脚本仅供学习和研究使用，使用前请确保你了解并遵守所有相关法律法规。作者不对因使用此脚本产生的任何后果负责。
