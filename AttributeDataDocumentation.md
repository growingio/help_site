#属性数据(CS)上传服务说明文档
##属性数据简介  
属性数据（CS字段）可以更好的帮助您进行基于用户的数据分析。我们提供了cs1-cs20的共20个字段，用于自定义的上传用户相关属性。上传这些属性可以帮助您做到：区分访问用户与注册用户，更精确的统计用户数量，进行跨平台分析，更详细的进行用户画像......  除此以外，我们将有更多的新功能基于属性数据进行构架。上传属性数据，可以帮助您更好的进行数据分析，实现增长。<font color=green>**在上传成功之后，请联系在线客服，我们会为您配置并且激活相应的属性字段。

注：属性数据（CS）当前只适用于上传用户的属性,不能用于其他类型数据的上传。例如：订单ID，商品ID...

##数据优先级
SDK采集的CS属性  > 用户属性数据CS1-CS10 >公司属性数据CS2-CS10  
即：如果您在 SDK，用户属性数据（User数据），公司属性数据（Company数据）中都上传了同一个字段，以SDK中上传的为准

##接口说明
为了接口安全，我们会为您分配三个认证字段：  
* projectKeyId: 由GrowingIO分配给您的项目ID. <font color=red>使用管理员及以上权限登录在项目管理中可以看到项目ID</font>. 也简称为ai  
* secretKey: 由GrowingIO分配给您的项目的传输用私钥  
* publicKey: 由GrowingIO分配给您的项目的传输用公钥 

此key分配后，联调测试通过后才会正式环境上启用。

## <font color=red>接口联调测试
请使用地址：<font color=red>testdata.growingio.com</font> 替换文档中 data.growingio.com 来进行联调测试。

##用户属性数据上传接口
协议：HTTPS  
方法：POST  
URL：https://data.growingio.com/saas/{projectKeyId}/user?auth={auth_token, 算法参见后续文档}  

Headers: 
* Access-Token = publicKey  
* Content-Type = application/json  


数据：

| 字段名 | 类型 | 说明 |
| -- | -- | -- |
| cs1 | string | 唯一标示一个注册用户的ID |
| cs2 | string | Saas企业建议传递客户公司的唯一ID |
| cs3 | string | 自定义,上传后对数据生效 |
| cs4 | string | 自定义,上传后对数据生效 |
| cs5 | string | 自定义,上传后对数据生效 |
| cs6 | string | 自定义,上传后对数据生效 |
| cs7 | string | 自定义,上传后对数据生效 |
| cs8 | string | 自定义,上传后对数据生效 |
| cs9 | string | 自定义,上传后对数据生效 |
| cs10 | string | 自定义,上传后对数据生效 |
| cs11 | double | 自定义,覆盖历史数据生效 |
| cs12 | double | 自定义,覆盖历史数据生效 |
| cs13 | double | 自定义,覆盖历史数据生效 |
| cs14 | double | 自定义,覆盖历史数据生效 |
| cs15 | double | 自定义,覆盖历史数据生效 |
| cs16 | string | 自定义,覆盖历史数据生效 |
| cs17 | string | 自定义,覆盖历史数据生效 |
| cs18 | string | 自定义,覆盖历史数据生效 |
| cs19 | string | 自定义,覆盖历史数据生效 |
| cs20 | string | 自定义,覆盖历史数据生效 |


 备注：  
*  上传后对数据生效：不会覆盖历史数据，当用历史数据进行分析时，CS字段的值仍保留历史时间的值  
    *举例：在2014-2015年，CS3的值为A，当前值为B。当对2014-2015年的数据进行分析时，CS3值为A  *

*  覆盖历史数据生效：会以当前的字段值覆盖历史上的所有值，不保留历史数据


* <font color=red>对于未登陆用户（访客用户），请不要上传用户ID（例如：userid:0）,以及其他属性字段

* <font color=red>对于注册用户，请不要漏传某些字段。</font>  
    *举例：cs3字段代表手机号码，一部分用户没有手机号码。请上传「无」「-」...等方便您自己辨识意义的字符 * 


格式：  
一次上传多条记录：  
举例：  
```js
[
  {
    "cs1": "user_id:12345",
    "cs2": "tenant_id:67890",
    "cs3": "rep_id:13579"
  },
  {
    "cs1": "user_id:12346",
    "cs2": "tenant_id:67891",
    "cs3": "rep_id:13580"
  },
  ...
]
```

一次上传单条记录：  
举例：  
```js
{
  "cs1": "user_id:12346",
  "cs2": "tenant_id:67891",
  "cs3": "rep_id:13580"
}
```
数据大小：单个请求上传的数据包总大小不超过1MB，内含json对象不超过100个  

返回值（status code）：  
成功：  
* 200, message = “Data uploaded.” 
 
失败：  
* 400  
message = “Authentication failed.”  
message = “Request too large.”  
message = “Project not found.”  



## 公司属性数据上传接口（SaaS企业适用）

您可以使用该接口上传相关的公司和用户属性，并且在 SDK 中上传cs1，cs2字段。这样我们就能够将您上传的数据进行绑定。运用这样的方式能够大大提高您的上传效率，减少您发送的数据量。

协议：HTTPS  
方法：POST  
URL：https://data.growingio.com/saas/{projectKeyId}/company?auth={auth_token, 算法参见后续文档}

Headers:  
Access-Token = publicKey  
Content-Type = application/json  
数据：

| 字段名 | 类型 | 说明 |
| -- | -- | -- |
| cs2 | string | Saas企业建议传递客户公司的唯一ID |
| cs3 | string | 自定义,上传后对数据生效 |
| cs4 | string | 自定义,上传后对数据生效 |
| cs5 | string | 自定义,上传后对数据生效 |
| cs6 | string | 自定义,上传后对数据生效 |
| cs7 | string | 自定义,上传后对数据生效 |
| cs8 | string | 自定义,上传后对数据生效 |
| cs9 | string | 自定义,上传后对数据生效 |
| cs10 | string | 自定义,上传后对数据生效 |
| cs11 | double | 自定义,覆盖历史数据生效 |
| cs12 | double | 自定义,覆盖历史数据生效 |
| cs13 | double | 自定义,覆盖历史数据生效 |
| cs14 | double | 自定义,覆盖历史数据生效 |
| cs15 | double | 自定义,覆盖历史数据生效 |
| cs16 | string | 自定义,覆盖历史数据生效 |
| cs17 | string | 自定义,覆盖历史数据生效 |
| cs18 | string | 自定义,覆盖历史数据生效 |
| cs19 | string | 自定义,覆盖历史数据生效 |
| cs20 | string | 自定义,覆盖历史数据生效 |	
 
格式：序列化的json对象  
举例：  
```js
[
  {
    "cs2": "tenant_id:67890",
    "cs3": "rep_id:13579",
  },
  {
    "cs2": "tenant_id:67891",
    "cs3": "rep_id:13580",
  },
  ...
]
```
也支持单个json对象，例如
```js
{
  "cs2": "tenant_id:67891",
  "cs3": "rep_id:13580",
}
```


## auth_token的计算方式 

 
* projectKeyId: 由GrowingIO分配给您的项目ID
 
* secretKey：由GrowingIO分配给您的私钥  
* keyArray：  
    * 对于一次上传多条记录时，取多条数据中的每个对象的主键的值（User接口为CS1，Company接口为CS2），并用逗号连接成为一个字符串  
    * 对于一次上传单条记录时，取该对象的主键的值（User接口为CS1，Company接口为CS2）  

Java:
```java
public String authToken(String projectKeyId, String secretKey, String keyArray) throws Exception {
    String message = "ai="+projectKeyId+"&cs="+keyArray;
    Mac hmac = Mac.getInstance("HmacSHA256");
    hmac.init(new SecretKeySpec(secretKey.getBytes("UTF-8"), "HmacSHA256"));
    byte[] signature = hmac.doFinal(message.getBytes("UTF-8"));
    return Hex.encodeHexString(signature);
}
```


Scala: 
```scala
def authToken(projectKeyId: String, secretKey: String, keyArray: String): String = {
  val message = s"ai=$projectKeyId&cs=$keyArray"
  val hmac: Mac = Mac.getInstance("HmacSHA256")
  hmac.init(new SecretKeySpec(secretKey.getBytes("UTF-8"), "HmacSHA256"))
  val signature = hmac.doFinal(message.getBytes("UTF-8"))
  Hex.encodeHexString(signature)
}
```

Python：
```python
#coding:utf-8 
import hashlib
import hmac

def authToken(projectKeyId,secretKey,keyArray):
    message = ("ai=" + projectKeyId + "&cs=" + keyArray).encode('utf-8')
    signature = hmac.new(bytes(secretKey.encode('utf-8')), bytes(message), digestmod=hashlib.sha256).hexdigest()
    return signature
   
```

PHP:
```php
function authToken($projectKeyId, $secretKey, $keyArray)
{
   $message="ai=".$projectKeyId."&cs=".$keyArray;
   return hash_hmac('sha256',$message, $secretKey, false);
}
```


举例：对于上述的json
```js
{
  "cs1": "user_id:12346",
  "cs2": "tenant_id:67891",
  "cs3": "rep_id:13580"
}
```

对应keyArray 的值是**<font color=red>user_id:12346</font>**



##用户属性字段的新增和修改说明
以下情况下，您需要联系我们的客户服务人员进行配合，帮助您进行字段的新增和修改：
1. 新增任何一个CS字段
2. 对任何一个CS字段的名称和意义进行修改
3. 对CS字段的值进行重新传输


**<font color=red>注：当您对新应用上传所属项目下的相同字段时，不需要重新进行配置。**