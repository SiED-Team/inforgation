import requests
from base64 import b64encode
from rich.table import Table
from rich.progress import Progress
import re

progress = Progress()


class fofa:

    def __init__(self, mail, apikey):
        self.mail = mail
        self.apikey = apikey

    def get_result(self, ip, timeout=5):
        self.table = Table()
        progress.console.rule('[green][INFO] 正在FOFA上查询 %s 的信息...' % ip)
        # base64编码查询语句
        words = b64encode(bytes('ip="{}"'.format(str(ip)).encode())).decode()
        # 拼接url
        self.url = 'https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&fields=host,title,country_name,' \
                   'province,city,server,protocol,banner,isp'.format(
            self.mail, self.apikey, words)
        try:
            self.data = requests.get(self.url, timeout=timeout).json()
        except requests.ReadTimeout:
            progress.console.print("[red][WRONG] 查询FOFA信息超时!")
            return None
        except BaseException:
            progress.console.print('[red][WRONG] 查询FOFA出错!(原因是在FOFA查询时，个别IP使用语法ip="*.*.*.*"会报错)')
        # api请求错误
        if self.data['error']:
            progress.console.print("[red][WRONG] FOFA查询 %s 失败！" % ip)
            return None
        if self.data['size'] == 0:
            progress.console.print("[yellow][WARNING] 没有在FOFA上查询到 %s 的相关信息！" % ip)
            return None
        self.table.add_column('host', justify="left")
        self.table.add_column('标题', justify="left")
        self.table.add_column('地理位置', justify="left")
        self.table.add_column('服务名', justify="left")
        self.table.add_column('协议', justify="left")
        for item in self.data['results']:
            self.table.add_row(item[0], item[1], item[2] + " " + item[3] + " " + item[4], item[5], item[6])
        return self.table

    def get_domain(self):
        try:
            content = re.compile(r'[a-zA-Z]')
            domain_list = []
            for item in self.table.columns[0]._cells:
                item = item.replace("https://", "").replace("http://", "")
                if re.match(content, item):
                    domain_list.append(item)
            return domain_list
        except BaseException as e:
            return []
