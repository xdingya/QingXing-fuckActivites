import requests
import time
from fun import *

##### 配置面板 #####
username = "your_username"
password = "your_password"
activityID = "qingxing_activity_id"
##### ###### #####

login_url = "http://www.hnqingxing.com/tools/submit_ajax.ashx?action=user_login&site_id=1"
login_data = {"txtUserName": username, "txtPassword": password, "chkRemember": "true"}

with requests.Session() as session:
    response = session.post(login_url, headers=None, data=login_data, verify=False)
    callback = response.json()

    if callback.get("status") == 1:
        # 登录成功，保存cookies
        cookies = session.cookies.get_dict()
        print("[成功] 喵~" + callback.get("msg") + "开始进行抢活动！")

    else:
        exit("[失败] " + callback.get("msg"))


url = "http://www.hnqingxing.com/tools/baoming_ajax.ashx?action=baoming"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "ASP.NET_SessionId=" + cookies["ASP.NET_SessionId"] + "; dt_cookie_user_name_remember=" + cookies["dt_cookie_user_name_remember"] + "; dt_cookie_user_pwd_remember=" + cookies["dt_cookie_user_pwd_remember"],
    "Origin": "http://www.hnqingxing.com",
    "Referer": "http://www.hnqingxing.com/jianzhi/show-8240.aspx",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}

data = {"baoming_type": "1", "channel_id": "2", "article_id": activityID}
count = 0
while True:
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)
        result = response.json()
        count += 1

        if result.get("status") == 1 and result.get("msg") == "恭喜您，报名成功！":
            print("[成功] 报名成功！抢占次数：" + str(count) + "\n")
            print("{:*^50}".format(" 以下为活动信息 "))
            activeDate = getActiveData(activityID)
            output = "- 活动名称：" + activeDate["name"] + "\n- 活动时间：" + activeDate["attendTime"] + "\n- 报名人数：" + activeDate["attendPerson"] + "/" + activeDate["totalPerson"] + "\n- 活动简介：" + activeDate["detail"]
            print(output)
            print("{:*^59}".format(""))
            break
        elif result.get("status") == 0 and result.get("msg") == "对不起，该内容已经不存在了！":
            print("[失败] 该活动暂未发布或已被删除" + " (第" + str(count) + "次尝试)")
        elif result.get("status") == 0:
            print("[失败] " + result.get("msg") + " (第" + str(count) + "次尝试)")
        else:
            print("[失败] " + result.get("msg") + " (第" + str(count) + "次尝试)")

        time.sleep(0.5)

    except Exception as e:
        print("发生未知错误：", e)
        break
