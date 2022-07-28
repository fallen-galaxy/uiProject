from selenium.webdriver.common.by import By

from tool.get_log import GetLog
from tool.read_yaml import read_yaml

log = GetLog.get_logger()

"""媒体前台配置"""

mp_url = "http://pc-toutiao-python.itheima.net/#/index"

mp_username = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
mp_authcode = (By.CSS_SELECTOR, '[placeholder="验证码"]')
mp_login_btn = (By.CSS_SELECTOR, '.el-button--primary')
mp_nickname = (By.CSS_SELECTOR, '.user-name')

mp_content_manage = (By.XPATH, '//span[text()="内容管理"]/..')
mp_publish_article = (By.XPATH, "//*[contains(text(),'发布文章')]")
mp_title = (By.CSS_SELECTOR, '[placeholder="文章名称"]')
mp_iframe = (By.CSS_SELECTOR, '#publishTinymce_ifr')
mp_content = (By.CSS_SELECTOR, '#tinymce')
mp_cover = (By.XPATH, "//*[contains(text(),'自动')]")
mp_submit = (By.XPATH, "//*[text()='发表']")
mp_result = (By.XPATH, "//*[contains(text(),'新增文章成功')]")

title = read_yaml("mp_article.yaml")[0][0]
channel = read_yaml("mp_article.yaml")[0][3]

"""管理后台配置"""

mis_url = "http://pc-toutiao-python.itheima.net/#/index"

mis_username = (By.CSS_SELECTOR, '[name="username"]')
mis_password = (By.CSS_SELECTOR, '[name="password"]')
mis_login_btn = (By.CSS_SELECTOR, '#inp1')
mis_nickname = (By.CSS_SELECTOR, '.user-info')

mis_info_manage = (By.XPATH, '//*[text()="信息管理"]/.')
mis_content_audit = (By.XPATH, '//*[text()="内容审核"]/.')
mis_title = (By.CSS_SELECTOR, '[placeholder="请输入：文章名称"]')
mis_channel = (By.CSS_SELECTOR, '[placeholder="请输入：频道"]')
mis_find = (By.CSS_SELECTOR, '.find')
mis_article_id = (By.CSS_SELECTOR, ".cell>span")
mis_pass = (By.XPATH, '//*[text()="通过"]/..')
mis_confirm_pass = (By.CSS_SELECTOR, '.el-button-primary')

"""用户前台配置"""

appPackage = 'com.itcast.toutiaoApp'
appActivity = '.MainActivity'

app_phonenum = (By.XPATH, "//*[@index='1' and @class='android.widget.EditText']")
app_authcode = (By.XPATH, "//*[@index='2' and @class='android.widget.EditText']")
app_login_btn = (By.XPATH, "//*[@text='登录' and @class='android.widget.Button']")
app_mine_unit = (By.XPATH, "//*[@index='3' and @text='我的']")

app_channel_area = (By.XPATH, "//*[@class='android.widget.HorizontalScrollView']")
app_article_ares = (By.XPATH, "//*[@index='2' and @bounds='[0,520][1440,2288]']")
