# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import json

def filter(res):
    """
    相似网址去重
    :param res:
    :return:
    """
    url_set = []
    url_rule = []
    url = []
    for i in res:
        if i not in url_set:
            url_set.append(i)

        if urlparse(i).path == ('/' or ''):
            rule = ''
        elif len(urlparse(i).path.split('/')) == 2 and '?' in i:
            rule = urlparse(i).path.split('/')[1][:3]
        else:
            rule = urlparse(i).path.split('/')[1][:3]
        for path in urlparse(i).path.split('/')[1:]:
            rule += str(len(path))  # 判断网址相似规则

        if '?' in i:
            for query in urlparse(i).query.split('&'):
                rule += query.split('=')[0][:1]
                rule += query.split('=')[0][-1:]  # 判断网址相似规则

        if rule in url_rule:
            print(1)
            continue
        else:
            url.append(i)
            url_rule.append(rule)
    return url

if __name__ == '__main__':
    with open('sql_url.json') as f:
        urls = f.readlines()
    r = open('target.txt', 'a+')
    for url in urls:
        tmp = json.loads(url)
        results =filter(tmp['url'])
        for result in results:
            r.write(result + '\n')
