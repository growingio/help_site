#SDK 集成

* <a href="#before-sdk">集成 SDK 前</a><br/>
* <a href="#during-sdk">集成 SDK 时</a><br/>
* <a href="#after-sdk">集成 SDK 后</a>

<a id='before-sdk' name='before-sdk'></a>
## 集成 SDK 前：

### 1.APP 里调用了一个网页，如果该网页上已经加了统计，APP 里还要再加吗？
对于 APP 里内嵌 H5 页面的统计，在哪里添加了代码，就去哪里看：
1. 如果该网页上加入了统计代码，那么在 App 内加载时，仍然会被统计到网页的数据中；
2. 如果在 APP 内集成了 SDK，那么 H5 页面会被统计到 APP 中；
3. 如果网页和 APP 都集成了，那么在 App 内打开 H5 页面时，会得到两份数据，分别发送到 Web 和 App 的应用下。

### 2.全 H5 的 APP 使用哪个平台的 SDK？
全 H5 的 App 一般需要看实现的框架，PhoneGap、HBuilder、Cordova 框架暂时不支持（JS SDK 也不支持）。

### 3.我们有一个 PC 站，还有一些二级域名移动站，该怎么加载 SDK 呢？
只要在主站添加 SDK 就行。

### 4.SDK 能加在 body 里面吗？
把SDK加在 body 里面也没有问题，但是推荐加在&lt;head&gt;里面，因为大部分网站是很多 pages 共用一个 head ，这种情况下就不用重复加载 SDK 了。

### 5.在同一个项目下面建立 2 个应用可以吗？（例如存在两套环境，一套为测试环境，一套为线上环境）
不可以，需要分别建立 2 个项目。


### 6.可以在本地环境添加 SDK 吗？
不可以，需要线上环境。


### 7.用 angularjs 写的 web，只有一个 head 文件，怎样统计所有页面？
如果想要将具有多域名的网站进行统一分析，您只需要在这些域名下集成同一个项目ID的代码，不需要再另外单独创建项目或是添加应用。若您想要独立分析的话，就将不同域名的网站独立创建成不同的项目。

### 8.集成 SDK 会对网页的打开时间造成影响吗?
不会。我们的 SDK 是异步加载方式，网站的所有元素加载完代码才会运行，所以不会影响用户体验。

### 9.GrowingIO的 SDK 会和其他公司的 SDK 有冲突吗？会影响性能吗？
没有冲突，不会影响性能。


### 10. iOS 端无痕采集是用 swizzling 方法做的吗？我集成了你们的包以后会对代码里写的 swizzling 会有影响吗？
是，一般来说没有影响的。

### 11.同一个项目里的网站已经上传 CS 字段，APP 还用上传吗？
还需要上传，如果在保证两个平台 CS 字段 Key 一致的情况下，不用再配置。

### 12.APP 端是否对设备ID做唯一标识？
安卓和 iOS 有对设备 ID 做唯一标识。安卓默认采集设备的 android_id，用户也可以自己配置。iOS 默认采集的是 IDFV，经配置后也可以采集 IDFA 或者随机字符串或者其他用户自定义的字符串。用户卸载 APP 后这两个值都不会变。

### 13.APP 端 SDK 集成大概占多少内存？
安卓集成 SDK 需要占用约 200k 内存，IOS SDK 每个框架约占 500k 内存，一般需要使用2-3种框架， 约占1M－1.5M。

<a id='during-sdk' name='during-sdk'></a>
## 集成 SDK 时：

### 1.为什么要添加URL Scheme？
URL Scheme 用于定义指标，为了防止普通用户唤醒定义功能以及从安全角度考虑，通过 GrowingIO APP 进行第一步权限认证后，从 GrowingIO APP 调起您的 APP 并进行定义操作。这个认证是服务端和客户端一起来做的，所以需要您手动添加一下我们生成的 URL Scheme。

### 2.集成 SDK 时 scheme 怎么获取？注意什么？	
URL Scheme 获取方式有两种，需要管理者及以上权限：

1. 添加新应用：登录官网 - 点击新建，选择添加新应用 -> 选择添加 Android 应用 -> 在第二段“添加URLScheme”中标黄字体。 

2. 现有应用管理）：登录官网 -> 右上角点击用户头像 -> 点击“项目管理” -> 点击左侧的“应用管理” -> 找到对应产品的 URL Scheme 。

### 3.pod 安装 SDK 的时候时间长或一直失败？

请您稍等一会儿，或者查看下网络，可能需要一些时间。

### 4.怎样启用 hashtag 作为页面收集？

我们默认不会把 hashtag 识别成页面 URL 的一部分，对于使用 hashtag 作为单页应用页面切换的网站来说，您可以使用 enableHT 来监听 hashtag 的变化，并区分页面来收集页面数据，每次 hashtag 改变都会触发一次 PV，hashtag 的信息也会记录在页面 URL 中。

	_vds.push(['enableHT', true]) 

### 5.怎样设置显示内容的黑名单？
**<font color="red">Web：</font>**

如果你希望过滤一些内容，可以在网站 DOM 结点上设置 growing-ignore 属性，这样这个容器里所有的元素的浏览量和点击量都不会被采集。
    
    <div growing-ignore='true'> 
    … 
    </div>

**<font color="red">iOS：</font>**


	UIView *view; 
    … 
    view.growingAttributesDonotTrack = YES;
    
   其中，view是您需要忽略的元素。

**<font color="red">Android：</font>**

	GrowingIO.ignoreView(View view)  
    
   调用这个接口即可。

### 6.怎样开启输入文本框内容采集？
目前只有 Web 端和安卓端支持；

Web：由于输入文本框可能涉及一些隐私信息，比如账号、密码等，GrowingIO 在采集数据的时候默认不采集输入文本框的数据。如果您希望采集某些文本框输入内容，比如搜索词，可以在 input 标签中设置 growing-track 属性，这样该文本框中的输入内容就会被采集到。如果 input 类型是 password，即使开启内容采集，也不会采集该文本框的输入内容。
    
     <input type='text' growing-track='true' />
 
安卓：可以参考 Android 新版集成文档部分。
<a id='after-sdk' name='after-sdk'></a>
## 集成 SDK 后：
  
###1.SDK 安装失败或者报错，是怎么回事？

**<font color="red">Web：</font>**

1.有可能工程师没有按照 4 步流程加载 SDK ；

2.检查项目 ID 是否填写正确，比如说项目ID里没有空格；

3.SDK 重复加载；

4.SDK 加载到某页的 body 中，导致其他页面无法圈选；

5.代码复制错误（通过QQ等某些通讯软件传递代码时，QQ会自动把某些代码转成表情字符）；

6.网址不能是 localhost 或 IP 格式，请换成域名格式的地址。

**<font color="red">iOS：</font>**

1.APP 没有在 Wi-Fi 环境下进行操作；

2.项目ID 没有填写正确；

3.没有添加或添加了错误的 URL Scheme；

4.没有在 AppDelegate 中调用函数 [Growing handleUrl:]；

5.之前集成过，再次集成，把两个URL Scheme写在一起了，随机读取URL Scheme，造成收到的数据一直是之前的URL Scheme的;

6.可能会存在在虚拟机上集成导致数据没发过来的情况，建议用户在真机上打包。

**<font color="red">Android：</font>**

1.App没有在 Wi-Fi 环境下进行操作;

2.项目 ID 没有填写正确;

3.没有添加或添加了错误的 URL Scheme;

4.没有添加初始化函数。

**如果以上情况，经排查后都没有问题，请联系客服人员。**


### 2.怎么看SDK的版本？


**2.1 App 启动时可以在 Log 中看到如下信息**

**Android :** 

> !!! Thank you very much for using GrowingIO. We will do our best to provide you with the best service. !!!  

> !!! GrowingIO version: XXX !!!

**iOS: **

> !!! Thank you very much for using GrowingIO. We will do our best to provide you with the best service. !!! 

> !!! GrowingIO version: XXX !!! 

（SDK版本0.9.12以及上的才会有该版本信息输出）

**2.2 App唤醒圈选后，点击圈选小圆点，可以看到当前SDK版本号。**

如果需要更新SDK，可以参考帮助文档 APP 接入 SDK 部分，去下载最新版本SDK。

### 3.怎么算接入成功？

能看到数据就可以认为安装成功了。