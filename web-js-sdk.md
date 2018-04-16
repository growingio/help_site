# Web JS SDK 2.x

<font color=red>重要：如果您目前使用的是 1.x 版本的 SDK，希望升级至 2.x 版本，请注意：您需要联系您的 GrowingIO 对接人，我们需要帮您开启后台 2.x 版本所对应功能。如果您直接集成 2.x 版本，而后台对应功能未开启的话，可能会造成数据丢失的问题</font>

###GrowingIO Web JS SDK 2.1 分为两个部分

1. 页面代码（Page Code）
2. gio.js库文件（Library）

####页面代码如下所示：

```
<!-- GrowingIO Analytics code version 2.1 -->
<!-- Copyright 2015-2017 GrowingIO, Inc. More info available at http://www.growingio.com -->
<script type='text/javascript'>
!function(e,t,n,g,i){e[i]=e[i]||function(){(e[i].q=e[i].q||[]).push(arguments)},n=t.createElement("script"),tag=t.getElementsByTagName("script")[0],n.async=1,n.src=('https:'==document.location.protocol?'https://':'http://')+g,tag.parentNode.insertBefore(n,tag)}(window,document,"script","assets.growingio.com/2.1/gio.js","gio");
  gio('init', 'your accountId', {'setImp':'false'});

  //custom page code begin here
  
  
  //custom page code end here

  gio('send');
</script>
<!-- End GrowingIO Analytics code version: 2.1 -->
```

可以看到页面代码中有对gio.js文件的引用，gio.js的地址为[http://assets.growingio.com/2.1/gio.js](/assets.growingio.com/2.1/gio.js)

