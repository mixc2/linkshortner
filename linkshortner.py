
import requests as r
import re
import random
import os
import json
from pprint import pprint

#Colors
m, h, k, b, n = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;97m'

#www.shorturl.at
def shorturl_at(target_domain):
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.shorturl.at','Referer':'https://www.shorturl.at/','sec-ch-ua':'"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    post = r.post('https://www.shorturl.at/shortener.php', headers=headers, data={'u':target_domain}).text

    try:
        result = re.search(r'input id="shortenurl".*?value="(.*?)"', post).group(1)
        return result
    except AttributeError:
        pass

#www.shorturl.asia
def shorturl_asia(target_domain):
    headers = headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.shorturl.asia','Referer':'https://www.shorturl.asia/id/','sec-ch-ua':'"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    data = {'uid':random.randint(0000000000000,9999999999999), 'url':target_domain}
    post = r.post('https://www.shorturl.asia/id/shorturl/shorten', data=data, headers=headers).text

    try:
        result = re.search(r'a id="myInput" href="(.*?)"', post).group(1)
        return result
    except AttributeError:
        pass

#is.gd
def is_gd(target_domain):
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/x-www-form-urlencoded','Origin':'https://is.gd','Referer':'https://is.gd/','sec-ch-ua':'"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
    data = {'optshorturl':0, 'url':target_domain}
    post = r.post('https://is.gd/create.php', data=data, headers=headers).text

    try:
        result = re.search(r'input.*?id="short_url" value="(.*?)"', post).group(1)
        return result
    except AttributeError:
        pass

#cutt.ly
def cut_ly(target_domain):
    headers = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Origin':'https://cutt.ly','Referer':'https://cutt.ly/','sec-ch-ua':'"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
    data = {'domain':0, 'url':target_domain}
    post = r.post('https://cutt.ly/scripts/shortenUrl.php', data=data, headers=headers).text

    if 'incorrect' in post: 
        pass
    else:
        return post

#tiny.cc
def tiny_cc(target_domain):
    ses = r.session()
    ses.headers.update({'Accept':'application/json','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/x-www-form-urlencoded','Origin':'https://tiny.cc','Referer':'https://tiny.cc/','sec-ch-ua':'"Google Chrome";v="118", "Chromium";v="118", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36','X-Requested-With':'XMLHttpRequest'})

    source = ses.get('https://tiny.cc').text
    data = {'_signature':re.search(r'input.*?value="(.*?)" name="_signature"', source).group(1), 'custom':0, 'no_stats':1, 'url':target_domain}
    post = ses.post('https://tiny.cc/tiny/url/create', data=data).json()

    if post['status'] == 1:
        return post['short_url']
    else: 
        pass

#shortenworld.com
def in_run(target_domain):
    ses = r.session()
    ses.headers.update({'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36'})
    source = ses.get('https://shortenworld.com/?shortenit='+ target_domain).text

    data = '{'+ re.search(r'data: \{(.*?)\},', source).group(1)+ '}'
    post = ses.post('https://shortenworld.com/anonymous-links', data=data).json()

    if post['code'] == 0:
        return post['data'][0]['url']
    else:
        pass

#hyperhost.ua
def surl_li(target_domain):
    ses = r.session()

    source = ses.get('https://hyperhost.ua/tools/en/surli').text
    data = {'_token': re.search(r'name="_token" value="(.*?)"', source).group(1), 'url':target_domain}
    ses.headers.update({'Accept':'application/json, text/javascript, */*; q=0.01','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Origin':'https://hyperhost.ua','Referer':'https://hyperhost.ua/tools/en/surli?gclid=Cj0KCQiA3uGqBhDdARIsAFeJ5r1xYI5Rg5x_imA9hyWW-bHMdzBZ1cthQdV8SltBlugwUH__zXttn9UaAhqaEALw_wcB','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36','X-CSRF-TOKEN':'jmljd25zp40krZlELGQxmPBdsTEq055gEy1Tlcus','X-Requested-With':'XMLHttpRequest'})

    try:
        post = ses.post('https://hyperhost.ua/tools/pushData', data=data).json()
        return post['success']
    except:
        pass

#izbdxj7duk.execute-api.us-west-2.amazonaws.com
def urlxz_com(target_domain):
    headers = {'Accept':'application/json, text/plain, */*','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/json','Origin':'https://web.urlxz.com','Referer':'https://web.urlxz.com/','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'cross-site','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36'}
    post = r.post('https://izbdxj7duk.execute-api.us-west-2.amazonaws.com/dev/createShortUrl', data=json.dumps({'long_url':target_domain}), headers=headers).json()

    try:
        return 'https://urlxz.com/'+ post['short_url']
    except KeyError:
        pass

#shorter.me
def shorter_me(target_domain):
    headers = {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Origin':'https://shorter.me','Referer':'https://shorter.me/?gad_source=1&gclid=Cj0KCQiA3uGqBhDdARIsAFeJ5r0lcFp-NWm0d3mmlvImfHvlXrwE7JNAFisC6xpxDe9lcNl-_GG5Z5gaApesEALw_wcB','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36','X-Requested-With':'XMLHttpRequest'}
    data = {'alias':None, 'password':None, 'url':target_domain}

    try:
        post = r.post('https://shorter.me/page/shorten', data=data, headers=headers).json()
        return post['data']
    except:
        pass

#Main, baby
if __name__ == '__main__':
    os.system('clear')
    
    print('LINK SHORTNER')
    print(f'   {m}-{b} Options')
    print(f'{b}•{m}[{n}1{m}]{n} Domain: {h}https://shorturl.at/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}2{m}]{n} Domain: {h}https://shorturl.asia/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}3{m}]{n} Domain: {h}https://is.gd/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}4{m}]{n} Domain: {h}https://cutt.ly/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}5{m}]{n} Domain: {h}https://tiny.cc/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}6{m}]{n} Domain: {h}https://in.run/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}7{m}]{n} Domain: {h}http://surl.li/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}8{m}]{n} Domain: {h}https://urlxz.com/{m}<{n}random{m}>')
    print(f'{b}•{m}[{n}9{m}]{n} Domain: {h}https://shorter.me/{m}<{n}random{m}>')
    print()
    ask = input(f'{m}!{n} Choose a number {m}>>>> {n}')
    print('')
    if ask not in ['1','2','3','4','5','6','7','8','9']:
        exit(f'{m}!{n}Undefined option: {ask}')
#Open&Read list
    lists = input('Enter Your List: ')
    print('')
    with open(lists) as f:
        for url in f:
            if ask == '1' or ask == '01':
               print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{shorturl_at(url)}\n')
            elif ask == '2' or ask == '02':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{shorturl_asia(url)}\n') 
            elif ask == '3' or ask == '03':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{is_gd(url)}\n')
            elif ask == '4' or ask == '04':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{cut_ly(url)}\n')
            elif ask == '5' or ask == '05':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{tiny_cc(url)}\n')
            elif ask == '6' or ask == '06':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{in_run(url)}\n')
            elif ask == '7' or ask == '07':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{surl_li(url)}\n')
            elif ask == '8' or ask == '08':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{urlxz_com(url)}\n')
            elif ask == '9' or ask == '09':
                print(f'{b}➤{m} [{h}Processing{m}]{n} {url}{b}➤ {n}{shorter_me(url)}\n')
               
