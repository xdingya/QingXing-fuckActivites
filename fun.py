import requests
from bs4 import BeautifulSoup


def getActiveData(activeID):
    activeID = str(activeID)
    response = requests.get("http://www.hnqingxing.com/huodong/show-" + activeID + ".aspx")
    activeDict = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('h1', class_='article-title')

        if title_tag:
            title = title_tag.get_text()
        else:
            return False

        hierar_divs = soup.find_all('div', class_='msg hierar')
        detail_dict = {}
        for hierar_div in hierar_divs:
            attr_name = hierar_div.find('span', class_='attr-name').text.replace("：", "")
            attr_value = hierar_div.find('span', class_='attr-value').text.replace("人", "")
            detail_dict[attr_name] = attr_value

        message_div = soup.find('div', {'id': 'message'})
        container_div = message_div.find('div', {'class': 'container'})
        article_attrs_divs = container_div.find_all('div', {'class': 'article-attrs'})
        second_article_attrs_div = article_attrs_divs[1]
        article_attr_div = second_article_attrs_div.find('div', {'class': 'article-attr'})
        paragraphs = article_attr_div.find_all('p')
        processed_content = ""
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            if text:
                processed_content += text + "\n"
        info = processed_content.strip()

        activeDict["name"] = title
        activeDict["attendTime"] = detail_dict["集合时间"]
        activeDict["totalPerson"] = detail_dict["名额"]
        activeDict["attendPerson"] = detail_dict["已报人数"]
        activeDict["detail"] = info

        return activeDict

    else:
        return False


def activityPack(activityID):
    print("{:*^50}".format(" 以下为活动信息 "))
    activeDate = getActiveData(activityID)
    output = "- 活动名称：" + activeDate["name"] + "\n- 活动时间：" + activeDate["attendTime"] + "\n- 报名人数：" + \
             activeDate["attendPerson"] + "/" + activeDate["totalPerson"] + "\n- 活动简介：" + activeDate["detail"]
    print(output)
    print("{:*^59}".format(""))
