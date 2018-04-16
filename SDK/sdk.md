# SDK 接入指南（微信小程序）

GrowingIO 提供微信小程序 SDK，将 SDK 插入到客户的微信小程序以后，就可以接收用户的行为数据了。

### 获取微信小程序 SDK

您可以通过如下的简单步骤，新建网站产品，并且获取到 GrowingIO JS SDK：

1.登录 GrowingIO； 
2.点击左上角的新建按钮；
3.点击添加新产品； 
4.选择平台「微信小程序」即可看到SDK的集成步骤。
![](/assets/QQ20170213-185547.png)

### 集成微信小程序SDK

1.下载 vds-mina.zip，并将解压后得到的 vds-mina.js 文件放在微信小程序项目根目录下。
（附下载链接：https://assets.growingio.com/sdk/wx/vds-mina.zip ）

2.在微信小程序项目根目录的 app.js 文件中添加以下 JS 代码：

```
var gio = require('vds-mina.js')
gio.projectId = “您的项目ID"
gio.appId = "AppID(小程序ID)"
```

3.小程序后台配置：在设置-开发设置-服务器域名-request合法域名中添加：```
https://api.growingio.com```


![](/assets/微信小程序集成.png)


### 重要配置选项

**1. 设置渠道**

进行渠道设置后，便于您追踪扫码的来源。通过微信后台生成自定义二维码时，在页面路径后添加参数：

giochannel=渠道名

例如：pages/index?query=1&giochannel=春节线下推广001

渠道名支持中英文字符，在使用growingio产品分析时，可以使用“App渠道”进行区分。

**2. 设置按钮文本内容**

配置按钮文本内容后优先采集文本，在圈选时会显示配置的文本内容。建议在集成时进行配置。

我们支持 data-growing-title 这个 key 的值作为内容：

```
<button data-growing-title="文本内容" bindtap="setPlain"></button>
```

**3. 设置元素位置**

对于列表元素，我们支持data-growing-idx这个key的值作为位置：

```
<button data-growing-idx="1" bindtap="setPlain"></button>
```
**4. 设置自定义用户属性**

用户属性用于标记用户的特征，便于您后续进行分群分析；我们支持10个自定义维度，其中 CS1 字段建议使用 openid，CS2 字段建议上传 unionid；如果您的其他应用已经设置过 CS1、CS2 字段，建议选择其他 CS 字段。

```
var gio = require("vds-mina.js")
gio.setCS1("CS1的key", "CS1的vale")
gio.setCS2("CS2的key", "CS2的vale")
gio.setCS3("CS3的key", "CS3的vale")
gio.setCS4("CS4的key", "CS4的vale")
gio.setCS5("CS5的key", "CS5的vale")
gio.setCS6("CS6的key", "CS6的vale")
gio.setCS7("CS7的key", "CS7的vale")
gio.setCS8("CS8的key", "CS8的vale")
gio.setCS9("CS9的key", "CS9的vale")
gio.setCS10("CS10的key", "CS10的vale”)
```
完成以上集成步骤，您就可以开始进行微信小程序的数据圈选了， <a href="https://docs.growingio.com/Features/circle.html">**点击这里**</a> 查看如何圈选。




