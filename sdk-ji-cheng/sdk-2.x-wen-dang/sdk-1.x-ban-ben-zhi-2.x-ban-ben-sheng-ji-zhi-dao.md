# SDK 1.x 版本至 2.x 版本升级指导

首先，欢迎您选择升级至 2.x 版本。在 2.x 版本内，您会体验到更加强大的自定义数据分析，帮助您将自有数据与 GrowingIO 采集的行为数据打通分析。

如果您目前使用的是 1.x 版本的 SDK，希望升级至 2.x 版本，请注意：您需要联系您的 GrowingIO 对接人，我们需要帮您开启后台 2.x 版本所对应功能。如果您直接集成 2.x 版本，而后台对应功能未开启的话，可能会造成数据丢失的问题。

 本文旨在帮助您从 1.x 版本无缝升级至 2.x 版本，由于两个版本的诸多接口、方法、字段含义均有较大变动，因此建议您在升级前一定参照本文完成必要的实施工作。

## 升级步骤

要完成从 1.x 版本至 2.x 版本的升级，您需要完成以下几个步骤：

#### 1. 重新集成 SDK

请您参考以下开发文档，完成SDK初始化代码的添加。

* [Web 2.x 版本 SDK 开发文档](web-js-sdk-2.x/)
* [Android 2.x 版本 SDK 开发文档](android-sdk-2.x/)
* [iOS 2.x 版本 SDK 开发文档](ios-sdk-2.x/)

Tips：建议您在开发中，使用 debug mode 校验 GrowingIO SDK 的数据是否正常上传。开启 debug mode 的方式请见上述文档中初始化方法部分。

#### 2. 迁移用户属性字段（CS字段）

如果您未做用户属性字段上传，请忽略此部分。

用户属性字段（简称CS字段）是 1.x 版本的概念，升级至 2.x 版本后：

* CS1字段，会强制命名为“登陆用户ID”，并且上传接口与其他变量不同。
* CS2-10字段，会迁移至“应用级变量”，应用级变量与CS字段的使用方式无任何区别。
* CS11-20字段，会迁移至“[用户变量](../../shu-ju-shi-shi/shi-jian-ji-bian-liang/zi-ding-yi-bian-liang/ge-lei-xing-zi-ding-yi-bian-liang-jie-shao/yong-hu-bian-liang.md)”。两者的区别主要在于：用户变量支持自定义的归因方式。

#### 2.1 上传接口：

2.x 版本中的上传用户变量方法有较大改动，不再将 `'setCSn'` 这个字段作为参数，方法中只需写入用户变量的 key - value 对。

**Web 端：**

* 1.x 版本方法格式：

```text
_vds.push(['setCS1', 'CS1的key', 'CS1的value']);
_vds.push(['setCS2', 'CS2的key', 'CS2的value']);
_vds.push(['setCS3', 'CS3的key', 'CS3的value']);
...
_vds.push(['setCS10', 'CS10的key', 'CS10的value']);
```

* 2.x 版本方法格式：

对于 CS1 字段，也就是登陆用户ID，请使用以下方法：

```text
// 设置登录用户ID
gio('setUserId', userId); 

// 清除登录用户ID
gio('clearUserId');
```

对于应用级变量，也就是 1.x 版本中的 CS2 - CS10，请使用以下方法：

```text
gio(‘app.set’, key, value) // 单个变量
gio('app.set', appLevelVariables) // 多个变量，可组合为一个JSON对象appLevelVariables传入
```

对于用户变量，也就是 1.x 版本中的 CS11 - CS20，请使用以下方法：

```text
gio('people.set', key, value); // 单个变量
gio('people.set', peopleVariables); // 多个变量，可组合为一个JSON对象peopleVariables传入
```

**Android 端：**

* 1.x 版本方法格式：

```text
GrowingIO growingIO = GrowingIO.getInstance();
    growingIO.setCS1("user_id", "100324");
    growingIO.setCS2("company_id", "943123");
    growingIO.setCS3("user_name", "张溪梦");
```

* 2.x 版本方法格式：

对于 CS1 字段，也就是登陆用户ID，请使用以下方法：

```text
// 设置登录用户ID API
GrowingIO.getInstance().setUserId(String userId);

// 清除登录用户ID API
GrowingIO.getInstance().clearUserId();
```

对于应用级变量，也就是 1.x 版本中的 CS2 - CS10，请使用以下方法：

```text
GrowingIO.setAppVariable(JSONObject variables)
GrowingIO.setAppVariable(String key, Number variable)
GrowingIO.setAppVariable(String key, String variable)
GrowingIO.setAppVariable(String key, Boolean variable)
```

对于用户变量，也就是 1.x 版本中的 CS11 - CS20，请使用以下方法：

```text
GrowingIO gio = GrowingIO.getInstance();
gio.setPeopleVariable(String key, String value);
gio.setPeopleVariable(String key, Number value);
gio.setPeopleVariable(String key, Boolean value);
gio.setPeopleVariable(JSONObject peopleVariables);// 多个变量，可组合为一个JSON对象peopleVariables传入
```

**iOS 端：**

* 1.x 版本方法格式：

```text
[Growing setCS1Value:@"100324" forKey:@"user_id"];
[Growing setCS2Value:@"943123" forKey:@"company_id"];
[Growing setCS3Value:@"张溪梦" forKey:@"user_name"];
```

* 2.x 版本方法格式：

对于 CS1 字段，也就是登陆用户ID，请使用以下方法：

```text
// 设置登录用户ID API
+ (void)setUserId:(NSString *)userId;

// 清除登录用户ID API
+ (void)clearUserId;
```

对于应用级变量，也就是 1.x 版本中的 CS2 - CS10，请使用以下方法：

```text
[Growing setAppVariable:@{@"key1":@"value1", @"key2":@2}];
[Growing setAppVariableWithKey:@"key1" andStringValue:@"value1"];
[Growing setAppVariableWithKey:@"key2" andNumberValue:@2];
```

对于用户变量，也就是 1.x 版本中的 CS11 - CS20，请使用以下方法：

```text
+ (void)setPeopleVariableWithKey:(NSString *)key andStringValue:(NSString *)stringValue;
+ (void)setPeopleVariableWithKey:(NSString *)key andNumberValue:(NSNumber *)numberValue;
+ (void)setPeopleVariable:(NSDictionary<NSString *, NSObject *> *)variable; // 多个变量，可组合为一个对象传入
```

#### 2.2 GrowingIO 后台配置

在 GrowingIO 后台进行用户属性字段配置，是在 “项目配置” - “CS字段配置” 页面。升级至 2.x 版本后，取消了上述配置方式。您可以在 **“管理” - “自定义事件和变量” 页面中的 “应用级变量” 和 “用户变量” Tab 页**分别找到自动为您迁移过去的两种变量的配置。配置方式请参考[相关帮助文档](../sdk-1.x-wen-dang/zi-ding-yi-shu-ju-shang-chuan-pei-zhi-zhi-nan.md)。

#### 3. 迁移页面属性字段（PS字段）

如果您未做页面属性字段上传，请忽略此部分。

类似于用户属性字段，在 2.x 版本中，页面属性字段被迁移到了[“页面级变量”](../../shu-ju-shi-shi/shi-jian-ji-bian-liang/zi-ding-yi-bian-liang/ge-lei-xing-zi-ding-yi-bian-liang-jie-shao/ye-mian-ji-bian-liang.md)。与页面属性字段不同的是，**页面级变量相当于过去的 PS 字段，不再存在过去的 PG 字段**。

**3.1 上传接口**

**Web 端：**

* 1.x 版本方法格式：

```text
_vds.push([’setPageGroup‘, ‘PageGroup 的名称’]; 
_vds.push([‘setPS1’, ‘PS1 的值’]); 
_vds.push([‘setPS2’, ‘PS2 的值’]); 
_vds.push([‘setPS3’, ‘PS1 的值’]);
```

* 2.x 版本方法格式：

```text
gio('page.set', key, value);
gio('page.set', pageLevelVariables); //多个变量，可组合为一个对象传入
```

**Android 端：**

* 1.x 版本方法格式：

```text
GrowingIO.setPageGroup(Activity activity, String name); 
GrowingIO.setPS1(Activity activity, String property); 
GrowingIO.setPS2(Activity activity, String property);
```

* 2.x 版本方法格式：

```text
GrowingIO gio = GrowingIO.getInstance();
gio.setPageVariable(Activity activity, String key, String value);
gio.setPageVariable(Activity activity, String key, Number value);
gio.setPageVariable(Activity activity, String key, Boolean value);
gio.setPageVariable(Activity activity, JSONObject pageLevelVariables);

gio.setPageVariable(Fragment fragment, String key, String value);
gio.setPageVariable(Fragment fragment, String key, Number value);
gio.setPageVariable(Fragment fragment, String key, Boolean value);
gio.setPageVariable(Fragment fragment, JSONObject pageLevelVariables);
```

**iOS 端：**

* 1.x 版本方法格式：

```text
@property (nonatomic, copy) NSString* growingAttributesPageGroup; 
@property (nonatomic, copy) NSString* growingAttributesPS1; 
@property (nonatomic, copy) NSString* growingAttributesPS2; 
@property (nonatomic, copy) NSString* growingAttributesPS3;
```

* 2.x 版本方法格式：

```text
+ (void)setPageVariableWithKey:(NSString *)key andStringValue:(NSString *)stringValue toViewController:(UIViewController *)viewController;

+ (void)setPageVariableWithKey:(NSString *)key andNumberValue:(NSNumber *)numberValue toViewController:(UIViewController *)viewController;

+ (void)setPageVariable:(NSDictionary<NSString *, NSObject *> *)variable toViewController:(UIViewController *)viewController;
```

#### 2.2 GrowingIO 后台配置

您需要在 **“管理” - “自定义事件和变量” 页面中的 “页面级变量” Tab 页**进行配置。配置方式请参考[相关帮助文档](https://docs.growingio.com/sdk-20/zidingyi_config/zidingyi_config.html)

### 4. 迁移自定义事件（埋点事件）

如果您未做自定义事件的上传，请忽略此部分。

2.x 版本的自定义事件，在概念上与 1.x 版本无任何区别，但上传接口和配置方式上有以下变更。

**4.1 上传接口**

**Web 端：**

* 1.x 版本方法格式：

```text
window._vds.track(event_name, properties)
```

* 2.x 版本方法格式：

```text
gio('track', eventId);
gio('track', eventId, number);
gio('track', eventId, eventLevelVariables);
gio('track', eventId, number, eventLevelVariables);
```

**Android 端：**

* 1.x 版本方法格式：

```text
public class GrowingIO {
    public GrowingIO track(String eventName, JSONObject properties)
}
```

* 2.x 版本方法格式：

```text
GrowingIO gio = GrowingIO.getInstance();
gio.track(String eventId);
gio.track(String eventId, Number eventNumber);
gio.track(String eventId, Number eventNumber, JSONObject eventLevelVariables);
gio.track(String eventId, JSONObject eventLevelVariables);
```

**iOS 端：**

* 1.x 版本方法格式：

```text
@interface Growing: NSObject
+ (void)track: (NSString *) event properties: (nullable NSDictionary *) properties;
@end
```

* 2.x 版本方法格式：

```text
+ (void)track:(NSString *)eventId;
+ (void)track:(NSString *)eventId withNumber:(NSNumber *)number;
+ (void)track:(NSString *)eventId withNumber:(NSNumber *)number andVariable:(NSDictionary<NSString *, NSObject *> *)variable;
+ (void)track:(NSString *)eventId withVariable:(NSDictionary<NSString *, NSObject *> *)variable;
```

#### 4.2 GrowingIO 后台配置

自定义事件的配置，同 1.x 版本一样，也是在**“管理” - “自定义事件和变量” 页面中的 “自定义事件” Tab 页**。但您会发现，除了 “自定义事件” Tab 页外，现在还提供了 “事件级变量” Tab 页来专门管理事件级变量的配置。您只需在 “事件级变量” Tab 页完成事件级变量的配置，然后在新建自定义事件时，从已经建好的事件级变量中选择即可。

### 5. 数据校验

在完成了上述代码实施和配置后，我们当然需要对数据是否成功上传进行校验。校验工作分为两步完成。

#### 数据校验第一步：本地开发环境校验

GrowingIO 提供了 SDK debug 模式以及 debug 工具，来帮助您完成数据的校验。

1. Web 端

对 Web 端的开发者，GrowingIO 提供了 Chrome 浏览器插件形式的 debug 工具，请在[这里](../growingio-web-debugger/growingio-web-debugger-an-zhuang.md)下载安装。

debug 工具的工作界面如下图：

![](https://docs.growingio.com/assets/WebDebuggerInstall5.png)

**log 中自定义数据的关键字**

* 在 cstm 条目中，可以看到上传的 “自定义事件+事件级变量” 数据
* 在 pvar 条目中，可以看到上传的 “页面级变量” 数据
* 在 evar 条目中，可以看到上传的 “转换变量” 数据
* 在各条目中，都可以找到 “用户变量” 对应的数据
* 移动端

对移动端的开发者，GrowingIO 的 SDK 提供了 debug 模式，在 SDK 初始化代码中可以找到。如下图：

Android： 

![](../../.gitbook/assets/12%20%281%29.jpeg)

iOS： 

![](../../.gitbook/assets/13%20%282%29.jpeg)

开启 debug 模式后，您需要在app上触发一下打点事件，在打出的log里搜索上述关键字就能找到对应自定义事件&变量上传的数据。

#### 数据校验第二步：GrowingIO 后台图表验证

在 GrowingIO 分析后台，找到 “单图” - “新建事件分析”，然后在图表中选择您设计好的 “指标+维度”，查看是否有数据。当然，您需要首先确保您的自定义事件或变量确实有被触发。

