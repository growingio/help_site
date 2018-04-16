# SDK 接入指南（微信内嵌页）

包括微信公众号、服务号中内嵌的页面。这些页面中，如果需要登录微信账号后才能访问，则无法使用传统的网页圈选，需要作简单的配置。

如果此页面已经集成过JS SDK，只需要补充一行代码：

```
<script type='text/javascript' src='https://assets.growingio.com/sdk/wx/vds-wx-plugin.js'></script>
```

如果是新集成，请按照下面的步骤进行。

## 一、初次基本配置

### 1. 进入集成页面

![](/assets/QQ20170213-185303.png)

### 2. 集成代码

您项目 ID 为 :xxxxxxxxxxxx

将以下JS代码复制到您所需分析页面中的&lt;head&gt;和&lt;/head&gt;标签之间即可。

安装成功后，除 localhost 和 IP 地址外，所有网址下的行为数据都将会被收集。

```
<script type='text/javascript'>
      var _vds = _vds || [];
      window._vds = _vds;
      (function(){
        _vds.push(['setAccountId', 'xxxxxxxxxxxx']);
        (function() {
          var vds = document.createElement('script');
          vds.type='text/javascript';
          vds.async = true;
          vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(vds, s);
        })();
      })();
  </script>
  <script type='text/javascript' src='https://assets.growingio.com/sdk/wx/vds-wx-plugin.js'></script>
```

### 3. 修改页面地址

安装完成后需要在“项目管理”中选择“应用管理”，在微信内嵌页面应用一行，点击“编辑”修改集成项目的地址为您的**微信页面入口**的地址

![](http://note.youdao.com/yws/public/resource/93072dd459a9ba620ba14899d0d6b7b2/xmlnote/A577570CC42B4C3DA18771F9905756E4/43073)

例如：www.growingio.com ，修改为：www.growingio.com/wechart.html

### 4. 重要配置选项（可选）

以下配置项非必须填写。如果需要分析登录用户行为、页面属性等，需要进行配置。

#### 用户自定义维度

GrowingIO的数据分析工具提供了例如“应用版本”，“渠道”，“城市”，“设备型号”等等这些通用维度。但在使用过程中，有时无法满足用户对特定数据维度的分析要求。

为了能够让数据分析变得更加的灵活，我们提供了自定义维度的接口，使用者可以对各种对象设置属性。

这些属性在作图时，将表现为维度。

#### 配置用户属性

用户属性只能用来表示

登录用户

本身的属性，至少包括用户ID。

根据需求，可以用来指定用户的各种属性

1. 自然属性，比如性别、出生年月等。
2. 账户属性，比如等级、类型标签等。
3. 行为特征，比如是否有过购买记录之类。

用户属性被称为CS字段，最多支持十个，从CS1到CS10，接口如下：

```
_vds.push(['setCS1', 'CS1的key', 'CS1的value']); 
_vds.push(['setCS2', 'CS2的key', 'CS2的value']); 
_vds.push(['setCS3', 'CS3的key', 'CS3的value']); 
_vds.push(['setCS10', 'CS10的key', 'CS10的value']);
```

在下面的例子中，总计上传5个用户属性，分别是：

CS1: user\_id:100324

CS2: company\_id:943123

CS3: user\_name:王同学

CS4: company\_name:GrowingIO

CS5: sales\_name:销售员小王

```
<script type='text/javascript'>
      var _vds = _vds || [];
      window._vds = _vds;
      (function(){
        _vds.push(['setAccountId', '9d2805xxxxde8c0d']);

        _vds.push(['setCS1', 'user_id', '100324']);
        _vds.push(['setCS2', 'company_id', '943123']);
        _vds.push(['setCS3', 'user_name', '王同学']);
        _vds.push(['setCS4', 'company_name', 'GrowingIO']);
        _vds.push(['setCS5', 'sales_name', '销售员小王']);

        (function() {
          var vds = document.createElement('script');
          vds.type='text/javascript';
          vds.async = true;
          vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
          var s = document.getElementsByTagName('script')[0];
          s.parentNode.insertBefore(vds, s);
        })();
      })();
  </script>
```

## 二、CS字段设置条件和限制

1. CS 字段
   不能
   是和用户没有直接关系的属性，比如不能是订单 ID，商品 ID 等。
2. CS1 字段：在 GrowingIO 系统中用于识别注册用户的身份，因此
   CS1 的 value 必须填写用户的唯一身份标示 ID
   。
3. CS2 字段：在 GrowingIO 系统中用于识别 SaaS 客户的租户，因此所有的 SaaS 用户必须填写租户的唯一身份标示 ID，非 SaaS 用户不做限定。
4. 对于未登录用户，不要设置任何CS字段。
5. 如果没有用到所有的 CS 字段，剩下的可以不设置。
6. 同一个 CS 字段，必须保持在
   各个平台意义相同。

在上传成功之后，请联系在线客服，我们会为您配置并且激活相应的属性字段

## 三、配置页面属性

针对一些非常重要的页面，我们可以设置该页面的一些公共属性，比如搜索结果页、商品详情页、购物车页面、结算页面、支付页面、支付成功/失败确认页面等等。我们把每组不同类型的页面称做 PageGroup。

针对页面设置属性，比如某个商品的详情页，您可以将商品的类别，尺码、颜色、生产厂商等信息设置为属性，更加灵活的分析用户行为。在商品详情页上面所有的按钮点击，都会和这些页面属性形成一个关联关系，可以使用该页面的属性来分析点击页面上按钮等行为。

我们在 JS SDK 中提供了自定义页面属性接口：

```
_vds.push([’setPageGroup‘, ‘PageGroup的名称’];
_vds.push([‘setPS1’, ‘PS1的值’]);
_vds.push([‘setPS2’, ‘PS2的值’]);
_vds.push([‘setPS3’, ‘PS1的值’]);
```

在JS SDK中，需要设置 PageGroup，每个 PageGroup 支持最多6个自定义维度 PS1-PS6，PageGroup 个数不限。

如下例子：

某商品详情页：adidas 运动 t-shirt；

定义 PageGroup 产品详情页：“ProductInfoPage”

上传4个页面属性，分别是

PS1： 商品ID：1234567

PS2： 商品名称：Adidas 运动 t-shirt

PS3： 商品品牌：Adidas

PS4： 商品品类：运动

```
<script type='text/javascript'>
        var _vds = _vds || [];
        window._vds = _vds;
        (function(){
          _vds.push(['setAccountId', '您的项目ID']);

          _vds.push(['setPageGroup', 'ProductDetailsPage']);
          _vds.push(['setPS1', '1234567']);
          _vds.push(['setPS2', 'Adidas 运动 t-shirt']);
          _vds.push(['setPS3', 'Adidas']);
          _vds.push(['setPS4', '运动']);


          (function() {
            var vds = document.createElement('script');
            vds.type='text/javascript';
            vds.async = true;
            vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(vds, s);
          })();
        })();
    </script>
```

这样就可以分别分析某个或者某个品牌、类别的商品浏览、转化情况。

同时，对于用户将商品“adidas 运动 t-shirt”加入购物车这个事件，也可以使用商品品牌、品类来做分析。

此功能暂时处于beta测试阶段，在上传成功之后，请联系在线客服，我们会为您配置并且激活相应的属性字段。

## 注意事项

微信内嵌页开启圈选的原理是在圈选页面点击对应产品时跳转到应用管理设置的入口页并在url上添加三个参数gr\_circle，gr\_project\_id，gr\_login\_token，然后SDK根据当前页面是否具备这三个参数来开启圈选，所以请集成SDK的开发者不要在应用管理设置的入口页进行重定向，否则导致应用无法正常开启圈选。

