# GrowingIO Mobile Debugger

## 简介

GrowingIO Mobile Debugger是GrowingIO推出的一款调试Mobile SDK所发送数据的工具。在GrowingIO Mobile Debugger的帮助下，实施工程师可以看到在什么样的页面上，在什么时机向GrowingIO发送了什么样的服务器请求。

## 启动Mobile Debugger

#### 第一步、进入Mobile Debugger启动页

在右上侧的项目管理中选择Mobile Debugger，进入Mobile Debugger启动页，如下图

![Mobile Debugger&#x5165;&#x53E3;](../.gitbook/assets/image%20%289%29.png)

![Mobile Debugger&#x542F;&#x52A8;&#x9875;](../.gitbook/assets/image%20%286%29.png)

#### 第二步、扫码唤起APP

1. 选择项目中需要进行测试的应用，并保证手机中已经安装该APP，且该APP已经集成GrowingIO 2.2.0及以上的SDK。
2. 使用手机浏览器扫描入口的二维码唤起Debug的APP，需要注意微信中扫码无法唤起APP。

## 使用Mobile Debugger测试数据

在唤起Debug的APP后，该APP采集的行为数据以及当前页面截图就会出现在网页上，测试同学可以根据数据看数据的采集以及发送情况，对数据进行测试。

![Debugger&#x5DE5;&#x4F5C;&#x53F0;](../.gitbook/assets/image%20%285%29.png)

在此概览中可能出现的数据日志含义分别有：

page：页面浏览数据

vst：用户访问数据

clck：点击行为数据

chng：输入框行为数据

cstm：“事件以及关联的事件级变量” 数据

pvar：“页面级变量” 数据

evar：“转化变量” 数据

ppl：“用户变量” 数据

imp（元素浏览数据）数据量级过大，影响Mobile Debugger性能，Mobile Debugger不展示这部分数据。

