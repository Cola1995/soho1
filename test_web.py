from selenium import webdriver
import time
driver = webdriver.Chrome()
# cookies = {
# '_ga':'GA1.2.1790995068.1559540304',
#  'gr_user_id':'d29fbc7f-37ea-4e1a-b2df-6c7775054f55',
#  'grwng_uid':'663ec0b3-68cf-4370-800d-1742acec7018',
#  '_gid':'GA1.2.680907725.1560740623',
#  'Hm_lvt_2e77cccb66fdf75371af65a8b6b96331':'1560139278,1560753172,1560827393',
#  'ba42bd083ce7556e_gr_session_id':'c9c9c3b4-7c54-454b-a872-f56a14d93a5d',
#  'ba42bd083ce7556e_gr_session_id_c9c9c3b4-7c54-454b-a872-f56a14d93a5d':'true',
#  '_csrf':'x4HLoSibR2g9asLZfY_mpoDF',
# 'Hm_lpvt_2e77cccb66fdf75371af65a8b6b96331':'1560846706'
# }
# cookie_list=[
# {'domain': '.dev.bitsdaq.io', 'expiry': 1560853895.667082, 'httpOnly': True, 'name': 'KOSESSID', 'path': '/','secure': False, 'value': 'f93d33c1-b85c-439d-8875-641465a8de33'},
#  {'domain': '.bitsdaq.io', 'expiry': 1592386181.475488, 'httpOnly': True, 'name': '__cfduid', 'path': '/', 'secure': True, 'value': 'dcf2c201a23e33309341428cee02c31721560850179'},
#  {'domain': '.bitsdaq.io', 'expiry': 1560852107, 'httpOnly': False, 'name': 'ba42bd083ce7556e_gr_session_id_0bdfb5ac-5305-495e-bd19-a40425a6e8f7', 'path': '/', 'secure': False, 'value': 'true'},
#     {'domain': '.dev.bitsdaq.io', 'expiry': 1592386185, 'httpOnly': False, 'name': 'Hm_lvt_2e77cccb66fdf75371af65a8b6b96331', 'path': '/', 'secure': False, 'value': '1560850185'},
#  {'domain': '.bitsdaq.io', 'expiry': 1876210185, 'httpOnly': False, 'name': 'gr_user_id', 'path': '/', 'secure': False, 'value': 'c1dae71d-12ff-4beb-a9a7-f7118bc7b957'},
#     {'domain': '.bitsdaq.io', 'expiry': 1560936583, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.407317920.1560850184'},
#  {'domain': '.bitsdaq.io', 'expiry': 1623922183, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1176158733.1560850184'},
#  {'domain': '.dev.bitsdaq.io', 'httpOnly': False, 'name': 'Hm_lpvt_2e77cccb66fdf75371af65a8b6b96331', 'path': '/', 'secure': False, 'value': '1560850185'},
#     {'domain': '.bitsdaq.io', 'expiry': 1876210185, 'httpOnly': False, 'name': 'grwng_uid', 'path': '/', 'secure': False, 'value': '1d69b695-ae51-4d8c-852e-d3e5c84cd913'},
#  {'domain': '.bitsdaq.io', 'expiry': 1560852107, 'httpOnly': False, 'name': 'ba42bd083ce7556e_gr_session_id', 'path': '/', 'secure': False, 'value': '0bdfb5ac-5305-495e-bd19-a40425a6e8f7'},
#     {'domain': 'dev.bitsdaq.io', 'httpOnly': False, 'name': '_csrf', 'path': '/', 'secure': False, 'value': 'S9yOI_LKUGX1WJqYQHyzmm-B'},
#  {'domain': 'dev.bitsdaq.io', 'httpOnly': True, 'name': 'csrfToken', 'path': '/', 'secure': False, 'value': 'y5rhEIRn-lwC8NQQf6-ZTlJTsOuUb-01dcM4'}]

driver.get("https://dev.bitsdaq.io/")
time.sleep(60)
cookie_list = driver.get_cookies()
print(cookie_list)

driver.delete_all_cookies()
for cookie in cookie_list:
     #k代表着add_cookie的参数cookie_dict中的键名，这次我们要传入这5个键
    for k in {'name', 'value', 'domain', 'path', 'expiry'}:
        #cookie.keys()属于'dict_keys'类，通过list将它转化为列表
       if k not in list(cookie.keys()):
           #saveCookies中的第一个元素，由于记录的是登录前的状态，所以它没有'expiry'的键名，我们给它增加
            if k == 'expiry':
                t = time.time()
                cookie[k] = int(t)    #时间戳s
    #将每一次遍历的cookie中的这五个键名和键值添加到cookie
    driver.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path', 'expiry'}})
print(driver.get_cookies())

 #加载我们想要看到的页面的url




# driver.add_cookie(cookie_dict=cookies)
driver.get("https://dev.bitsdaq.io/wallets")






