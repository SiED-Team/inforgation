# inforgarion蓝队信息聚合查询工具

### 某次蓝队值守时写的，没有算法基础，各种逻辑写得比较一般
### 特别感谢[狼组安全团队的TIG 威胁情报收集](https://github.com/wgpsec/tig#tig--%E5%A8%81%E8%83%81%E6%83%85%E6%8A%A5%E6%94%B6%E9%9B%86-) ,本工具也是在TIG的基础上进行开发，加入了更多平台的查询。

ps:已知问题：shodan平台查询结果输出到报告时，会出现将特殊字符转义的情况（\n），因此临时用'、'替代，等后续版本更新

# inforgarion支持的平台如下：

## 鹰图
> [奇安信鹰图平台](https://hunter.qianxin.com/) 
> 
> [鹰图API获取地址](https://hunter.qianxin.com/home/userInfo)
## fofa
> [fofa平台](https://fofa.info/)
> 
> [fofa API获取地址](https://fofa.info/personalData)
## 微步
> [微步社区](https://x.threatbook.cn/)
> 
> [微步API获取地址](https://x.threatbook.cn/v5/myApi)
## shodan
> [shodan平台](https://www.shodan.io/)
> 
> [shodan API获取地址](https://account.shodan.io/)
## 0zero
> [0zero平台](https://0.zone/)
> 
> [0zero API获取地址](https://0.zone/applyParticulars?type=site)
### and more......
# 使用方法：
1、clone至本地后首先安装依赖

`pip(3) -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
`

2、接着配置config.ini，往里面添加自己的APIKEY，config.ini如下：
```editorconfig
[鹰图/hunter]
# 鹰图地址：https://hunter.qianxin.com/
# 鹰图APIKEY获取地址：https://hunter.qianxin.com/home/userInfo
username = 
apikey = 

[fofa]
# fofa地址：https://fofa.info/
# fofa APIKEY获取地址：https://fofa.info/personalData
mail = 
apikey = 

[微步/weibu]
# 微步社区地址：https://x.threatbook.cn/
# 微步APIKEY获取地址：https://x.threatbook.cn/v5/myApi
apikey = 

[shodan]
# shodan地址：https://www.shodan.io/
# shodan APIKEY获取地址：https://account.shodan.io/
apikey = 

[0zero]
# 0zero地址：https://0.zone/
# 0zero APIKEY获取地址：https://0.zone/applyParticulars?type=site
apikey = 
```
3、运行：`python3 inforgation.py`，使用`-i`参数指定要查询的单个IP，使用`-o`参数指定输出的文件名，如：
`python3 inforgation.py -i 114.114.114.114 -o gogole`，运行结果如下：
```editorconfig

 _        __                       _   _
(_)_ __  / _| ___  _ __ __ _  __ _| |_(_) ___  _ __
| | '_ \| |_ / _ \| '__/ _` |/ _` | __| |/ _ \| '_ \
| | | | |  _| (_) | | | (_| | (_| | |_| | (_) | | | |
|_|_| |_|_|  \___/|_|  \__, |\__,_|\__|_|\___/|_| |_|
Powered by BigBigBan   |___/          version 1.0

─────────────────────────────────────────────── [INFO] 正在鹰图上查询 114.114.114.114 的信息... ───────────────────────────────────────────────
[INFO] 消耗积分：1
[INFO] 今日剩余积分：30670
[WARNING] 没有在鹰图上查询到 114.114.114.114 的相关信息

─────────────────────────────────────────────── [INFO] 正在FOFA上查询 114.114.114.114 的信息... ───────────────────────────────────────────────
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━┓
┃ host               ┃ 标题                                         ┃ 地理位置 ┃ 服务名       ┃ 协议 ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━┩
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ wiki.ministep.cn   │ ministep                                     │ China    │ nginx/1.16.1 │ http │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ baipeng66.fun      │                                              │ China    │              │ http │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ 114.114.114.114:53 │                                              │ China    │              │ dns  │
│ illucidhome.com    │ Jiangyi Lighting Co. LTD &#8211; Mirror lamp │ China    │ Apache       │ http │
└────────────────────┴──────────────────────────────────────────────┴──────────┴──────────────┴──────┘
───────────────────────────────────────────── [INFO] 正在微步上查询 114.114.114.114 的威胁情报... ─────────────────────────────────────────────
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┓
┃ 威胁等级  ┃    IP类型判断      ┃ 威胁类型  ┃       运营商        ┃ 地理位置   ┃  场景   ┃ 情报可信度   ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━┩
│  无威胁   │ 白名单,IDC服务器   │          │ 美国Cogent通信公司   │   中国    │ Anycast │     高     │
└──────────┴──────────────────┴──────────┴────────────────────┴──────────┴─────────┴────────────┘
────────────────────────────────────────────── [INFO] 正在shodan上查询 114.114.114.114 的信息... ──────────────────────────────────────────────
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┓
┃       IP        ┃ 开放的端口   ┃ 域名        ┃ 子域名              ┃ 运营商                 ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━┩
│ 114.114.114.114 │ 53         │ 114dns.com │ public1.114dns.com │ Cogent Communications │
│                 │            │            │                    │                       │
└─────────────────┴────────────┴────────────┴────────────────────┴───────────────────────┘
──────────────────────────────────────────── [INFO] 正在0zero上查询 114.114.114.114 的威胁情报... ─────────────────────────────────────────────
┏━━━━━━━━━━━━━━━━━┳━━━━━━┳━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━┓
┃ IP              ┃ 端口  ┃ url ┃ 网页标题  ┃ 操作系统  ┃ 服务器   ┃ 运营商  ┃ 协议  ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━╇━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━┩
│ 114.114.114.114 │ 53   │ N/A │   N/A    │ unknown  │ unknown │ 114DNS │ N/A  │
└─────────────────┴──────┴─────┴──────────┴──────────┴─────────┴────────┴──────┘
```
查询完毕后会在output目录中生成google.html的查询报告，如果使用`-o`指定文件名，则会在output目录下以IP跟时间为名生成报告

# TODO
- [ ] 批量查询
- [ ] 算法优化（看到一大堆if else自己都头大）
- [ ] 情报聚合后的去重
- [ ] 域名反查、whois查询
- [ ] 添加更多平台查询

# 最后，欢迎各位师傅提issue！万分感谢🙏