import os
import requests
import pandas as pd


# 保存图片
def savepictures(img_urls, titles):
    for i in range(len(img_urls)):
        img_url = img_urls[i]
        title = titles[i]
        # 下载图片
        img_data = requests.get(img_url).content
        # 为图片文件命名，并保存
        with open(str(title) + '.jpg', 'wb') as f:
            f.write(img_data)


if __name__ == '__main__':
    if 'Pictures' not in os.listdir():
        os.mkdir('Pictures')
    os.chdir('Pictures')

    # 从爬取好的文件中读出图片路径和书名
    books_data = pd.read_csv('E:\\PyCharm-Workspace\\crawlerTest\\result.csv')
    img_urls = books_data['img_urls']
    titles = books_data['titles']
    savepictures(img_urls, titles)
