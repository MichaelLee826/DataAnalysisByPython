import requests
import pandas as pd
from bs4 import BeautifulSoup


# 1.获取数据
def get_data():
    # 豆瓣上的最新书列表
    url = "https://book.douban.com/latest"
    # http://httpbin.org/get
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    # GET方式
    data = requests.get(url, headers=headers)
    # print(data.text)
    return data


# 解析数据
def parse_data(data):
    # 将网页数据转换为BeautifulSoup对象
    soup = BeautifulSoup(data.text, "lxml")

    # 查看网页的源代码，根据HTML标签，找出所需内容
    books_left = soup.find('ul', {'class': 'cover-col-4 clearfix'})
    books_left = books_left.find_all('li')

    books_right = soup.find('ul', {'class': 'cover-col-4 pl20 clearfix'})
    books_right = books_right.find_all('li')

    books = list(books_left) + list(books_right)

    img_urls = []
    titles = []
    ratings = []
    authors = []
    details = []

    for book in books:
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)

        title = book.find_all('a')[1].get_text()
        titles.append(title)

        rating = book.find('p', {'class': 'rating'}).get_text()
        rating = rating.replace('\n', '').replace(' ', '')
        ratings.append(rating)

        author = book.find('p', {'class': 'color-gray'}).get_text()
        author = author.replace('\n', '').replace(' ', '')
        authors.append(author)

        # detail = book.find('p', {'class': 'detail'}).get_text()
        detail = book.find_all('p')[2].get_text()
        detail = detail.replace('\n', '').replace(' ', '')
        details.append(detail)

        # print("图片链接：", img_urls[6])
        # print("书名", titles[6])
        # print("评价", ratings[6])
        # print("作者", authors[6])
        # print("简介", details[6])
        # 问题：爬取的内容跟网页上所显示的内容有出入，如，某本书网页上评分为9.3，爬取里显示为9.5

    return img_urls, titles, ratings, authors, details


# 存储数据
def save_data(img_urls, titles, ratings, authors, details):
    # 创建空的DataFrame数据框
    result = pd.DataFrame()

    # 将对应数据填充到数据框
    result['img_urls'] = img_urls
    result['titles'] = titles
    result['ratings'] = ratings
    result['authors'] = authors
    result['details'] = details

    # 将DataFrame转化为CSV格式，生成的CSV文件保存在当前目录下
    result.to_csv('result.csv', index=None)


# 开始爬取
def run():
    data = get_data()
    img_urls, titles, ratings, authors, details = parse_data(data)
    save_data(img_urls, titles, ratings, authors, details)


if __name__ == '__main__':
    run()
