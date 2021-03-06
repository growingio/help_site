# 指标

---

在 GrowingIO 数据模型中，提供了 21 个预定义指标，支持丰富的分析场景，同时也可以通过圈选或打点创建自定义事件：

- 名词解释 · 指标
    - 第一部分：访问级指标
        - [1.访问量（web/app）](#1.访问量（web/app）)
        - 2.访问用户人均访问次数（web/app）
        - 3.每次访问页面浏览量（web/app） 
        - 4.总访问时长（web/app）
        - 5.平均访问时长（web/app）
        - 6.退出次数（web/app）
        - 7.退出率（web/app）
        - 8.页面停留时长（web）
        - 9.平均页面停留时长（web）
        - 10.进入量（web）
        - 11.访问用户人均进入次数（web）
        - 12.总进入时长（web）
        - 13.平均进入时长（web）
        - 14.每次进入页面浏览量（web）
        - 15.跳出次数（web）
        - 16.跳出率（web） 
    - 第二部分：用户级指标
        - 17.访问用户量（web/app）
        - 18.新访问用户量（web/app）
        - 19.登录用户量（web/app）
        - 20.新登录用户量（web/app）
    - 第三部分：页面级指标
        - 21.页面浏览量（web/app）
        - 22.通过圈选定义的页面浏览量（web/app）
    - 第四部分：事件级指标
        - 23.通过圈选定义的元素指标化后（web/app）
        - 24.自定义事件（web/app）
    - [常见问题 FAQ]

> 1-21 为系统预定义指标，可以直接使用；22-24 可按照需要灵活定义。


## 第一部分：访问级指标

> **衡量网站总体访问情况**

### 1.访问量（web/app）
访问的数量。与页面级变量一起使用时，代表着该页面被访问的次数。

### 2.访问用户人均访问次数（web/app） [ 访问用户 / 访问量 ]
平均每个用户访问网站（打开 App）的次数。

### 3.每次访问页面浏览量（web/app） [ 访问量 / 页面浏览量 ]
平均每次访问浏览的页面的数量。

### 4.总访问时长（web/app）
所有访问的总时长，以分钟作为单位展示。不能使用页面级维度（域名、页面、自定义页面级变量）分解。

### 5.平均访问时长（web/app） [ 总访问时长 / 访问量 ]
平均每次访问时长，以分钟作为单位展示。不能使用页面级维度（域名、页面、自定义页面级变量）分解。

### 6.退出次数（web/app）
用户退出网站的数量，通常需要在一定范围内，因为所有的用户最终都会退出网站。
与页面级变量一起使用时，统计的是该页面作为用户一次访问中的最后一个页面的访问的次数。

### 7.退出率（web/app） [ 退出次数 / 访问量 ]
如果与页面级变量一起使用，统计的是该页面作为退出页的次数，占这个页面被访问的总体数量的比例。
每个页面都有可能成为退出页，因为用户总要离开网站，但是如果关键流程中的页面退出率高，就说明页面出现了问题，用户本应该继续完成操作，但是中途退出了。
*退出页：用户在一次访问中访问的最后一个页面，是这次访问的退出页，也就是用户的这次访问是在这里结束的。

### 8.页面停留时长（web）

总页面停留时长（分钟）指标只能被页面级维度（域名、页面、自定义页面级变量）分解，代表着用户在当前页面上停留的总时长，即访问结束的时间点减去访问开始的时间点。

### 9.平均页面停留时长（web）[ 总页面停留时长/（页面浏览量 - 退出次数）]

平均页面停留时长（分钟）指标只能被页面级维度（域名、页面、自定义页面级变量）分解，代表着用户在当前页面上停留的平均时长。

**案例**： 在「事件分析」中使用访问级指标进行作图，评估用户访问网站的质量。

![][1]


>  **衡量进入页（即落地页）的访问情况**

*进入页是指用户进入网站时访问的第一个页面，也就是我们常说的落地页。*

### 10.进入量（web）
访问用户进入网站进行访问的数量。

### 11.访问用户人均进入次数（web）  [ 进入量 / 访问用户量 ]
平均每个访问用户进入网站进行访问的数量。

### 12.总进入时长（web）
用户进入网站进行访问的总时长，以分钟作为单位展示。
与页面级变量一起使用时，统计的是该页面作为用户一次访问中的第一个页面的访问的时长。

### 13.平均进入时长（web） [ 总进入时长 / 进入量 ]
用户平均每次进入网站进行访问的平均时长，以分钟作为单位展示。

### 14.每次进入页面浏览量（web） [ 进入总页面浏览量 / 进入量 ]
平均每次进入带来的页面浏览的数量。

### 15.跳出次数（web）
访问一个页面就离开的次数。即一次访问中只访问了一个页面。

### 16.跳出率（web） [ 跳出次数 / 进入量 ]
只有一个页面浏览的访问占所有访问的比率。

> 高跳出率表示访问者对到达站内时访问的第一个页面不感兴趣，没有继续访问更深入的页面，或者是登录页面设计存在问题，与目标用户不匹配，因此他们访问了一个页面就离开了。跳出率可以通过调整广告渠道/优化落地页面内容来降低。

**案例：**在「事件分析」中选择衡量进入页的指标，分析这个页面作为进入页时的表现情况。
步骤：第一步，选择「访问级指标」；第二步，选择维度为「页面」。

![此处输入图片的描述][2]

我们可以看到除了首页“/”之外，下载电子书和秘籍这两个活动落地页的进入量最高。

## 第二部分：用户级指标

> **用户级指标：区分不同用户的状态**

### 17.访问用户量（web/app）
访问用户的数量。

### 18.新访问用户量（web/app） 
（接入 GrowingIO 后）365 天内第一次访问网站的访问用户数量。

### 19.登录用户量（web/app）
登录用户的数量，需要上传登录用户 ID 。

### 20.新登录用户量（web/app）
（接入 GrowingIO 后）第一次登录网站的用户数量。 

> 访问用户的技术说明
>     Web：根据 cookie 。
>     APP：根据用户唯一 Id 区分访问用户（Android 用户的唯一 ID 为：Android_ID 或 IMEI；iOS 的唯一 ID 为：IDFV 或 IDFA）。即使用户删除应用再安装，用户 ID 仍然不变。

## 第三部分：页面级指标

> **衡量页面的访问情况**

### 21.页面浏览量（web/app）
用户实际浏览过的网页数量。

### 22.通过圈选定义的页面浏览量（web/app）
可以定义一个页面，也可以定义一组页面，统计定义页面的浏览量。

**案例：**可以通过页面浏览量（PV）和访问用户量（UV）制作一个「事件分析」图表，来查看产品的数据情况。

![此处输入图片的描述][3]

## 第四部分：事件级指标

> **可以通过圈选和创建自定义事件来实现**

### 23.通过圈选定义的元素指标化后（web/app）
通过圈选定义的元素，在使用的时候，会指标化为「该元素点击 / 浏览的人数或次数」。

### 24.自定义事件（web/app）
通过打点实施创建自定义事件。

#### 仍有疑问？请参考[常见问题－名词解释](../../faq/definitions.md)

  [1]: http://growing.cn-bj.ufileos.com/mmm1.png
  [2]: http://growing.cn-bj.ufileos.com/mmm2.png
  [3]: http://growing.cn-bj.ufileos.com/mmm3.png
  



