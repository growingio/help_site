# Web JS SDK 2.1 页面代码安装

** 请将以下的页面代码放置到需要分析的页面中的&lt;head&gt;和&lt;/head&gt;标签之间，即可完成Web JS SDK 2.1页面代码的安装。**

```text
<!-- GrowingIO Analytics code version 2.1 -->
<!-- Copyright 2015-2017 GrowingIO, Inc. More info available at http://www.growingio.com -->
<script type='text/javascript'>
!function(e,t,n,g,i){e[i]=e[i]||function(){(e[i].q=e[i].q||[]).push(arguments)},n=t.createElement("script"),tag=t.getElementsByTagName("script")[0],n.async=1,n.src=('https:'==document.location.protocol?'https://':'http://')+g,tag.parentNode.insertBefore(n,tag)}(window,document,"script","assets.growingio.com/2.1/gio.js","gio");
  gio('init', 'your projectId', {});

  //custom page code begin here


  //custom page code end here

  gio('send');
</script>
<!-- End GrowingIO Analytics code version: 2.1 -->
```

请注意使用具体的项目ID替换上述代码中‘your  projectId’的部分。

建议在安装页面代码结束之后，建议使用GrowingIO Web Debugger验证一下服务器请求发送是否正常。

