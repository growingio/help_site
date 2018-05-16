# SDK上传说明文档

当您上传字段数量在 10 个之内时，请使用 SDK 上传方式。只有在超过 10 个的情况下，才推荐使用 API 上传方式。

## SDK上传须知

### 用户属性字段设置条件和限制

1. 用户属性字段不能是和用户没有直接关系的属性，比如不能是订单 ID，商品 ID 等。
2. CS1 字段：在 GrowingIO 系统中用于识别注册用户的身份，因此 CS1 的 value 必须填写用户的唯一身份标示 ID。
3. CS2 字段：在 GrowingIO 系统中用于识别 SaaS 客户的租户，因此所有的 SaaS 用户必须填写租户的唯一身份标示 ID，非 SaaS 用户不做限定。
4. 对于未登录用户，不要设置任何用户属性字段。 在用户未登录即 CS1 为空时，其他用户属性字段均为空。
5. 只需配置用到的用户属性字段，剩下的可以不配置。
6. 同一个用户属性字段，必须保持在各个平台意义相同。
7. 强烈建议在所有页面均上传所有CS字段，以提升数据有效性。
8. 上传 cs 字段值不能包含冒号。

### 上传后需要进行配置

在上传成功两小时后，您需要在「项目管理-项目配置-CS 配置中」进行字段配置和激活。配置成功后便可开始使用用户属性字段进行分析。配置过程可参考[用户属性数据上传配置文档](config-manual.md)。

## SDK上传接口示例

在如下例子中，总计上传 5 个用户属性。分别是：

 **CS1:** user\_id:100324

 **CS2:** company\_id:943123

 **CS3:** user\_name:张溪梦

 **CS4:** company\_name:GrowingIO

 **CS5:** sales\_name:销售员小王

### JS SDK示例

接口如下：

```text
_vds.push(['setCS1', 'CS1的key', 'CS1的value']);
_vds.push(['setCS2', 'CS2的key', 'CS2的value']);
_vds.push(['setCS3', 'CS3的key', 'CS3的value']);
...
_vds.push(['setCS10', 'CS10的key', 'CS10的value']);
```

示例如下：

```text
    <script type='text/javascript'>
        var _vds = _vds || [];
        window._vds = _vds;
        (function(){
          _vds.push(['setAccountId', '您的项目ID']);

          _vds.push(['setCS1', 'user_id', '100324']);
          _vds.push(['setCS2', 'company_id', '943123']);
          _vds.push(['setCS3', 'user_name', '张溪梦']);
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

### iOS SDK 接口和示例

接口如下：

```text
-(void)someMethod
{
    …
    [Growing setCS1Value:@"CS1的value" forKey:@"CS1的key"];
    [Growing setCS2Value:@"CS2的value" forKey:@"CS2的value"];
    [Growing setCS3Value:@"CS3的value" forKey:@"CS3的value"];
    [Growing setCS4Value:@"CS4的value" forKey:@"CS4的value"];
    [Growing setCS5Value:@"CS5的value" forKey:@"CS5的value"];
    …
}
```

示例如下：

```text
-(void)someMethod
{
    …
    [Growing setCS1Value:@"100324" forKey:@"user_id"];
    [Growing setCS2Value:@"943123" forKey:@"company_id"];
    [Growing setCS3Value:@"张溪梦" forKey:@"user_name"];
    [Growing setCS4Value:@"GrowingIO" forKey:@"company_name"];
    [Growing setCS5Value:@"销售员小王" forKey:@"sales_name"];
    …
}
```

### Android SDK 接口和示例

接口如下：

```java
GrowingIO growingIO = GrowingIO.getInstance();
growingIO.setCS1("CS1的key", "CS1的value");
growingIO.setCS2("CS2的key", "CS2的value");
...
growingIO.setCS10("CS10的key", "CS10的value");
```

示例如下：

```text
private void setGrowingIOCS() {
    GrowingIO growingIO = GrowingIO.getInstance();
    growingIO.setCS1("user_id", "100324");
    growingIO.setCS2("company_id", "943123");
    growingIO.setCS3("user_name", "张溪梦");
    growingIO.setCS4("company_name", "GrowingIO");
    growingIO.setCS5("sales_name", "销售员小王");
}
```

