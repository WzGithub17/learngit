from bs4 import BeautifulSoup
import requests
import time


def get_info(url):
    # url = 'http://zhuanzhuan.58.com/detail/784021218206433284z.shtml?fullCate=5%2C36&fullLocal=2192&from=pc&metric=e5577e0ff944d07ceceab55cd1de9eb5&PGTID=0d300024-0089-0482-c03c-2190bdb9b637&ClickID=2'
    time.sleep(4)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')

    position_list = soup.select('#nav > div > span:nth-of-type(3) > a')
    position = position_list[0].text.strip()
    title_list = soup.select('div.box_left_top > h1')
    title = title_list[0].text
    price_list = soup.select('span.price_now > i')
    price = price_list[0].text
    area_list = soup.select('div.palce_li > span > i')
    area = area_list[0].text
    label_list = soup.select('div.biaoqian_li')
    labels = label_list[0].text.strip()
    # img_list = soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.banner > div')
    description_list = soup.select('div.box_left > div:nth-of-type(3) > div > div > p')
    description = description_list[0].text
    connection = url
    data = {
        'position': position,
        'title': title,
        'price': price,
        'area': area,
        'label': labels,
        'description': description,
        'connection': connection
    }
    print(data)


def get_all_info():
    page = 1
    while page <= 3:
        print('第%d页' % page)
        url = 'http://sg.58.com/shouji/pn'+str(page)+'/?zz=zz'
        htmls = requests.get(url)
        soup = BeautifulSoup(htmls.text, 'lxml')

        hrefs_list = soup.select('a.t')
        for href in hrefs_list:
            link = href.get('href')
            if 'zhuanzhuan' in link:
                get_info(link)

        page += 1


get_all_info()
