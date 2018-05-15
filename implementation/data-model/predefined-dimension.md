# 预定义维度

## **页面 \(**_**Web Page**_**\)**

**定义**：按 URI 列出的已访问网页。URI 是指网页网址中跟在域名后面的部分；例如 [https://www.growingio.com/joinus](https://www.growingio.com/joinus) 中的 URI 就是 /joinus。

**举例** : 页面可以区分跨页面元素在不同页面的表现情况。比如某些网站的导航栏在网站的每个页面都出现（在上述情况下导航栏就是跨页面元素）。

## **页面来源 \(**_**Referral Path**_**\)**

**定义**：页面来源帮您了解当前访问页面的上级页面。制作单图时以 URI 方式进行展现。\(ps:此处 URI 中所带的查询参数会被忽略掉）

**举例**：我们可以制作横向Bar图，观察目标页面（如注册页面，或者购买页面）由哪些页面引入，从而可以对那些表现低于预期的页面进行优化。

**技术说明／备注**：GrowingIO 系统会统计每一个事件发生时所对应的页面来源。

## **域名 \(**_**Domain**_**\)**

**定义**: 是由一串用点分隔的名字组成的Internet上某一台计算机或计算机组的名称，用于在数据传输时标识计算机的电子方位。域名就相当于一个家庭的门牌号码，别人通过这个号码可以很容易的找到你。比如说大家在网站URL栏目输入：www.growingio.com 就能进入 GrowingIO 的网站。

**举例**：GrowingIO 分析中你可以使用报表系统，选择域名作为维度，选择PV，UV等作为指标，分析不同子域名下的页面浏览访问量等。

## 浏览器 \(_Browser _\)

**定义**: 用户所用浏览器的类型，常见的值有：Chrome，Chrome Mobile，Safari，IE等该维度中不包括内部的版本号。

**举例**:可以使用浏览器来区分不同使用不同浏览器的用户对指标的贡献情况。

## ** 浏览器版本（**_**Browser Version**_**）**

**定义**: 同「浏览器」，但是会按照不同的版本进行区分。如：Chrome 47.0.2526。

## ** 操作系统（**_**Operating System **_**）**

**定义**:用户所使用的操作系统，包含PC和Mobile，如：Windows 8 ，Windows 7 ，Mac OS X ，Android。

## ** 操作系统语言（**_**Operating System Language **_**）**

**定义**:将操作系统的语言作为维度值，以统计不同的操作系统语言的使用情况。

## ** 城市（**_**City **_**）**

**定义**:以城市作为维度值，帮助了解不同城市的访问情况。目前只支持国内城市。

**技术说明／备注**：GrowingIO 基于IP地址得到城市地址。城市判断为「未知」的原因：可能是用户使用移动网络（不包括WLAN网络），或开了代理。

## ** 地区（**_**Area  **_**）**

**定义**:该维度包含国内省级以上行政区，以及国外地区。

**举例**:地区帮您了解各个地域带来的流量及转化情况。您也可以选择来源过滤，查看特定来源各地域的数据。

**技术说明／备注**：GrowingIO 基于IP地址得到地区地址。

## ** 国家代码（**_**Country Code **_**）**

**定义**:用户所在的国家的英文缩写，常见的维度值有：CN，US，JP，SG等。

## ** 国家名称（**_**Country **_**）**

**定义**:用户所在的国家的名称，常见的有：中国，美国，英国，新加坡等。

### ** 网站／手机应用（**_**Web/App **_**）**

**定义**:用于区分 Web 类应用和 App 类应用，对应项目底下的三种应用类型。

### ** 访问来源（**_**Source  **_**）**

**定义**:访问来源可以帮助您了解该网站流量来源，访问来源可以是百度，谷歌，优酷等站外渠道，也可能是直接访问该网站。

**技术说明／备注：**Traffic Source 的最细分的级别是Referring Sites，即哪些网站或是搜索引擎为你贡献了流量，但却无法细分到具体的广告。可以通过设置UTM参数来确定流量具体是哪个广告带来的。

### ** 一级访问来源**

**定义**:一级访问来源将访问来源分为直接访问，搜索引擎，社交媒体，外部链接四大部分。

**技术说明／备注：**

**直接访问：** 当一个直接访问发生的时候，有可能是一个人直接在浏览器中输入了一个域名或使用书签进行访问。然而，直接访问还包括其他更多的实例。其中包括：

1.从邮件中点击链接访问网站取决于电子邮件的提供商/程序）；

2.从Microsoft Office 或 PDF 文件中点击链接访问网站；

3.通过点击由原 url 生成的短链接访问网站；

4.通过移动应用点击链接访问网站（比如今日头条、微博、微信中的链接）；

5.通过点击一个 https 类型的 url 访问一个 http 类型的 url（比如如果点击 https：//example.com 转到 [http://example2.com](http://example2.com), 对于 example2.com 的分析会认为是直接访问）；

6.部分浏览器（特别是移动端浏览器）会把搜索跳转当成直接访问；

所以如果要准确追踪投放渠道的情况，建议设置 utm 参数。[查看 utm 设置方法](../../ad-tracking/tutorial/utm-parameters.md)

**搜索引擎：** 来自以下地址的均属于搜索引擎：www.baidu.com，m.baidu.com，bzclk.baidu.com， so.com, sogou.com（soso.com已指向这里）, bing.com, youdao.com，zhongsou.com，google.xx.xx（Google在全世界有各种各样的域名），sm.cn（神马搜索\),yahoo.com。

**社交媒体：** 来自以下地址均属于社交媒体：weibo.com，t.cn, weibo.cn,zhihu.com，linkedin.com，lnkd.in，renren.com，facebook.com，twitter.com，mp.weixin.qq.com，wx.qq.com，im.dingtalk.com，mp.weixinbridge.com。

**外部链接：** 除了社交媒体，搜索网站之外的来源。

### ** 搜索词（**_**Search Query **_**）**

**定义**: 用户从搜索引擎进入网站所使用的搜索词。支持对 Google（含DoubleClick）、百度（baidu）、搜狗（sogou）、好搜（haosou）、Bing等5个搜索引擎的用户搜索词进行解析，包括付费搜索和自然搜索结果。注意: 由于Google和百度对于自然搜索结果启用了搜索词屏蔽，我们无法获取这两个渠道的自然搜索结果。付费搜索的搜索词可以获取。

### ** 广告关键字（**_**utm\_term **_**）**

**定义**: GrowingIO 使用utm\_term 来标识付费关键词。

### ** 广告来源（**_**utm\_source **_**）**

**定义**:GrowingIO 使用 utm\_source 来标识 搜索 引擎、简报名称或其他来源。 示例：utm\_source=baidu。"

### ** 广告媒介（**_**utm\_medium **_**）**

**定义**:GrowingIO utm\_medium标识广告传播媒介或者营销媒介。

### ** 广告内容（**_**utm\_content **_**）**

**定义**:GrowingIO 使用 utm\_content 区分指向同一网址的 广告或链接。

示例：utm\_content=logolink 或utm\_content=textlink。

**举例**:在链接"[http://www.example/com?utm\_source=sina&utm\_medium=banner&utm\_content=linktag&utm\_term=grow&utm\_campaign=IloveWA](http://www.example/com?utm_source=sina&utm_medium=banner&utm_content=linktag&utm_term=grow&utm_campaign=IloveWA) 中

| utm参数 | 含义 |
| --- | --- |
| utm\_source | 指广告所处的网站位置 |
| utm\_medium | 指广告的具体形式 |
| utm\_content | 指广告的具体内容 |
| utm\_campaign | 指投放广告的这次营销活动的名称 |

具体设置方法请参见：[5.1.渠道跟踪](../../ad-tracking/tutorial/utm-parameters.md)

**技术说明／备注**：UTM 广告系列参数对着陆页面的url进行标注，可以区别衡量各种营销渠道所带来的访客价值。在这里渠道归因采取的是非直接访问最后点击模型。 比如，访客于9:30分访问网站。我们进行渠道归因时，会统计在10:00点开始，回溯30天时间，其最后一次通过外站（非直接流量）进来时的UTM参数，关键词和refer URL。举个例子，访客A通过百度推广进入网站，然后通过sina Banner再次进入网站，最后一次通过直接输入URL进入网站完成购买，我们会认为这次转化由Sina Banner贡献。

### **用户传输字段**

**定义**:用户可以上传自定义用户属性类数据,并将其设为维度来针对自己的产品做更深度的细分。  
**技术说明／备注**： 用户上传的自定义字段用CS1～CS20表示。其中CS1 强制填写userID数据；CS2建议填写CompanyID；CS3~CS20由用户自主设置；一般情况下用户可以通过接口\(Server to Server\)和JS将数据传递给我们。通过接口传递的数据，数据不是时时更新的，只有企业客户出发更新，GrowingIO 才能获得最新结果。若使用JS，数据则是时时更新的。 具体设置方法请参见：[属性数据\(CS\)上传 API 说明文档](https://help.growingio.com/AttributeDataDocumentation.html)

## APP专有维度

### ** 设备品牌（**_**Device Brand **_**）**

**定义**:将不同设备的品牌作为维度值。

### ** 设备型号（**_**Device Type **_**）**

**定义**:不同的设备型号作为维度值，可用于区分具体的机型。

### ** 设备类型（**_**App/Pad **_**）**

**定义**:设备的类型，平板和手机，用于App分析

### ** 安卓渠道（**_**Android Store **_**）**

**定义**:表示app下载地址（安卓市场）。

### ** 设备方向（**_**Device Orientation **_**）**

**定义**:移动设备的方向，水平和竖直。

#### 仍有疑问？请参考[常见问题－名词解释](../../chang-jian-wen-ti/ming-ci-jie-shi.md)，查看关于维度的常见问题

