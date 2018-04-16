# Web JS 系统变量

Web JS SDK可以配置一些系统变量来控制 Web JS SDK的数据发送。

有以下系统变量在实施时可以使用以下这些系统变量：

#### imp系统变量

作用：禁止元素浏览量采集

GrowingIO 提供两种采集，元素浏览和元素点击/修改等交互行为。对于内容基本固定的网站来说，可以直接禁用元素浏览量采集。

```
gio('config', {'imp':false});
```

#### hashtag系统变量

作用：启用 hashtag 作为标识页面的一部分

默认值：false

GrowingIO默认不会把 hashtag 识别成页面URL的一部分。对于使用 hashtag 作为单页应用页面切换的网站来说，可以使用

```
gio('config', {'hashtag':true});
```

来监听 hashtag 的变化，并区分页面来收集页面数据，每次 hashtag 改变都会触发一次PV，hashtag 的信息也会记录在页面URL中。

