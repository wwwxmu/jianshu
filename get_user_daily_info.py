# -*- coding:utf-8 -*-
import time
import re
import random
import requests
from lxml import etree
from pymongo import MongoClient
client = MongoClient()

def randomUserAgent():
    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]

    return random.choice(USER_AGENTS)

def getResponse(url, **kwargs):
    if 'headers' not in kwargs:
        kwargs['headers'] = {
            'User-Agent': randomUserAgent(),
        }

    r = requests.get(url, **kwargs)

    return r

def getArticleInfo(user):
    print("==getArticleInfo==")
    uid = user['uid']
    article_num = int(user['article_nums'])
    PER_NUM = 9
    max_page = int(article_num / PER_NUM) if (article_num % PER_NUM) == 0 else int(article_num / PER_NUM)+1
    article_urls = ['https://www.jianshu.com/u/{}?order_by=shared_at&page={}'.format(uid, i) for i in
                    range(1, max_page+1)]

    details = []
    for article_url in article_urls:
        r = getResponse(article_url)
        dom = etree.HTML(r.text)
        items = dom.xpath('//ul[@class="note-list"]/li')

        for item in items:
            # 对每个 li标签再提取
            details_xpath = {
                'link': './div/a/@href',
                'title': './div/a/text()',
                'read_num': './/div[@class="meta"]/a[1]/text()',
                'comment_num': './/div[@class="meta"]/a[2]/text()',
                'heart_num': './/div[@class="meta"]/span[1]/text()',
            }

            key_and_path = details_xpath.items()
            detail = {}
            for key, path in key_and_path:
                detail[key] = ''.join(item.xpath(path)).strip()

            try:
                #将数字转换为整数
                for key in ['read_num', 'comment_num', 'heart_num']:
                    detail[key] = int(detail[key])

                details.append(detail)
            except ValueError:
                pass

    #返回爬取结果
    return details

def getUserInfo(uid):
    print('==getUserInfo==')
    url = 'https://www.jianshu.com/u/{}'.format(uid)
    r = getResponse(url)
    dom = etree.HTML(r.text)
    user_info = dict()
    user_info['uid'] = uid
    user_info['following']= dom.xpath('//div[@class="meta-block"]/a/p/text()')[0]
    user_info['follows'] = dom.xpath('//div[@class="meta-block"]/a/p/text()')[1]
    user_info['article_nums'] = dom.xpath('//div[@class="meta-block"]/a/p/text()')[2]
    user_info['word_nums'] = dom.xpath('//div[@class="meta-block"]/p/text()')[0]
    user_info['like_nums'] = dom.xpath('//div[@class="meta-block"]/p/text()')[1]
    return user_info

def getFollowsInfo(user_info):
    print("==getFollowsInfo==")
    follows = []
    uid = user_info['uid']
    follow_num = int(user_info['follows'])
    PER_NUM = 9
    max_page = int(follow_num / PER_NUM) if (follow_num % PER_NUM) == 0 else int(follow_num / PER_NUM)+1
    following_urls = ['https://www.jianshu.com/users/{}/followers?page={}'.format(uid, i) for i in
                          range(1, max_page+1)]
    for following_url in following_urls:
        r = getResponse(following_url)
        dom = etree.HTML(r.text)
        items = dom.xpath('//ul/li//div[@class="info"]')
        for item in items:
            user = {}
            try:
                user['uid'] = item.xpath('./a/@href')[0].split('/')[2]
                user['following'] = item.xpath('./div/span[1]/text()')[0].replace('关注', '').strip()
                user['follows'] = item.xpath('./div/span[2]/text()')[0].replace('粉丝', '').strip()
                user['article_nums'] = item.xpath('./div/span[3]/text()')[0].replace('文章', '').strip()
                s = item.xpath('./div[2]/text()')[0]
                num = re.findall(r"\d+",s)
                if len(num) == 2:
                    user['word_nums'] = num[0]
                    user['like_nums'] = num[1]
                follows.append(user)
            except ValueError:
                pass
    return follows

if __name__ == "__main__":
    uid = "67eb7ed414d3"
    date = time.strftime("%Y-%m-%d", time.localtime())
    user_info = getUserInfo(uid)
    details = getArticleInfo(user_info)
    follows = getFollowsInfo(user_info)
    data = {'uid': uid, 'date': date, 'following': user_info['following'],
            'follows': user_info['follows'], 'article_nums': user_info['article_nums'],
            'word_nums': user_info['word_nums'], 'like_nums': user_info['like_nums'],
            'article_details': details, 'follows_details': follows}

    db  = client.jianshu
    posts = db.author_info
    result = posts.insert_one(data)
    print(result)
