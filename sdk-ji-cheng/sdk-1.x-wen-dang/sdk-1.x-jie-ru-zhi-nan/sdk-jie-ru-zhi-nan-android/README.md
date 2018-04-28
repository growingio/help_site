# SDK接入指南（Android）

从0.9.85版（2016年7月20日发布）起，SDK的集成方式发生变化，下方文档已经更新。

新版SDK不支持Eclipse开发环境，如果需要请参考旧版集成文档，请点击[这里](https://github.com/growingio/help_site/tree/f4b4103b288205f6a9b13e0c4692f4d65a2ab386/SDK/Android_oldversion.html)

注意：目前 Android SDK **不支持 Instant Run**，原因是 SDK 采用的 Hook 方案是字节码植入方案，植入是在编译时期，但是因为 Instant Run 是不完全编译所以会造成新更改的元素无法正常 Hook。如果您想要测试效果或者发版，采用一次全新编译即可。

## 1. 导入SDK

**Gradle 编译环境（Android Studio）**

一、在project级别的build.gradle文件中添加`vds-gradle-plugin`依赖：

```groovy
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:3.0.1'
        classpath 'com.growingio.android:vds-gradle-plugin:1.1.9'
    }
}

allprojects {
    repositories {
        jcenter()
    }
}
```

二、在module级别的build.gradle文件中添加`com.growingio.android`插件、`vds-android-agent`依赖和对应的资源：

### URL Scheme获取方式有两种

1. 添加新产品：登录官网 -&gt; 点击项目选择框 -&gt; 点击“项目管理” -&gt; 点击“应用管理” -&gt; 点击“新建应用”-&gt;选择添加Android应用 -&gt;填写“应用名称“，点击下一步-&gt;在第二段中标黄字体。   
2. 现有产品：登录官网 -&gt; 点击项目选择框 -&gt; 点击“项目管理” -&gt; 点击“应用管理” -&gt; 找到对应产品的URL Scheme。

![&#x9879;&#x76EE;&#x7BA1;&#x7406;](../../../../.gitbook/assets/image%20%282%29.png)

### URL Scheme的格式是growing.xxxxxxxxxxxxxxxx

```groovy
apply plugin: 'com.android.application'
apply plugin: 'com.growingio.android'
android {
    defaultConfig {
        resValue("string", "growingio_project_id", "您的项目ID")
        resValue("string", "growingio_url_scheme", "您的URL Scheme")
    }
} 
dependencies {
        compile 'com.growingio.android:vds-android-agent:1.1.9@aar'
}
```

## 2. 添加URL Scheme

将下面的启动圈选接口添加到您的`AndroidManifest.xml`中的LAUNCHER `Activity`下以便我们唤醒您的程序，进行圈选。

```markup
<activity
    android:name=".MainActivity"
    android:label="@string/app_name"
    android:theme="@style/AppTheme.NoActionBar">
    <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
    </intent-filter>
    <!-- GrowingIO 启动圈选接口 -->
    <intent-filter>
        <data android:scheme="@string/growingio_url_scheme"/>
        <action android:name="android.intent.action.VIEW"/>

        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
    </intent-filter>
    <!-- GrowingIO 启动圈选接口 -->
</activity>
```

请添加一整个intent-filter区块,并确保其中只有一个data字段

## 3. 初始化SDK

请将以下 `GrowingIO.startWithConfiguration`加在您的`Application` 的 `onCreate` 方法中

```java
public class MyApp extends Application {
    @Override
    public void onCreate() {
        super.onCreate();
        GrowingIO.startWithConfiguration(this, new Configuration()
                .useID()
                .trackAllFragments()
                .setChannel("XXX应用商店")
                .setDebugMode(true); //打开调试Log
    }
}
```

1. 请确保将代码添加在\`Application\` 的 \`onCreate\` 方法中，添加到其他方法中可能导致数据不准确。
2. 其中`GrowingIO.startWithConfiguration`第一个参数为 `Application` 对象。
3. 使用`useID`方法，能够更准确地统计界面元素，一般建议添加。
4. 对于已经集成过旧版SDK并圈选过的应用，调用`useID`会导致新圈选的指标数值从零开始计算，类似初次集成SDK后发版的效果，但不影响之前圈选的指标数据。如果不希望出现这种情况，请去掉这个方法的调用。
5. `trackAllFragments`方法用于把`Fragment`自动识别为页面，但一个界面中只能同时显示一个`Fragment`。
6. `setChannel`方法的参数是渠道的名称。

添加代码之后，请先Clean项目，然后再进行编译。

## 4. 代码混淆

1. 如果您启用了代码混淆，请在您的 proguard-rules.pro 中添加以下代码

```text
-keep class com.growingio.android.sdk.** {
 *;
}
-dontwarn com.growingio.android.sdk.**
-keepnames class * extends android.view.View

-keep class * extends android.app.Fragment {
 public void setUserVisibleHint(boolean);
 public void onHiddenChanged(boolean);
 public void onResume();
 public void onPause();
}
-keep class android.support.v4.app.Fragment {
 public void setUserVisibleHint(boolean);
 public void onHiddenChanged(boolean);
 public void onResume();
 public void onPause();
}
-keep class * extends android.support.v4.app.Fragment {
 public void setUserVisibleHint(boolean);
 public void onHiddenChanged(boolean);
 public void onResume();
 public void onPause();
}
-keep class com.growingio.android.sdk.collection.GrowingIOInstrumentation {
    public *;
    static <fields>;
}
```

1. 如果您使用了AndResGuard,请在白名单里添加GrowingIO,如下：

```text
R.string.growingio*
```

### 下方各个配置项将影响统计的准确性，请务必仔细阅读，判断是否需要

## 5. 重要配置项

#### 采集H5页面数据

如果您在App内嵌入了WebView（包括X5内核），请确保您已经调用过下面的方法，来采集H5页面的数据：

```java
WebView.setWebChromeClient(WebChromeClient client);
```

请在第一次调用`WebView.loadUrl()`之前调用以上方法。

#### 采集广告Banner数据

很多应用的界面上方都有横向滚动的Banner广告。

对于此类广告，如果您的应用通过ViewPager、AdapterView或者RecyclerView实现，请在Banner创建时（包括动态创建）调用下面的接口来采集数据。

```java
GrowingIO.getInstance().trackBanner(banner, bannerDescriptions)
```

其中`bannerDescriptions`是`List<String>`类型，包含所有广告图对应的广告内容描述，内容描述需要跟广告的顺序相同。

例如，当您有5张广告图时，只需创建一个`String`类型的`List`，然后按5个广告出现的顺序给List的元素设置对应的广告描述，同样设置5个元素即可。

### 页面别名

对于安卓应用，页面指的是`Activity`或者`Fragment`。

有些时候，对于完成某个功能的页面，统计时可能需要进一步细分。 比如，对于展示商品列表的页面，需要区分衣物类商品，以及食品类商品的两种列表的访问量。

为处理这种场景，我们提供了取别名的方法来区分这两种情况下的页面，方法如下：

```text
GrowingIO.setPageName(Activity activity, String name)
```

如果您设置的的对象是`Fragment`，将上方的`Activity`替换为`Fragment`即可。

**我们用**`Activity`**来举例，具体说明它的用法。**

1. 某个应用的商品列表页是用`FeedActivity`实现的，所以默认的页面名称都是`FeedActivity`。
2. 现在我们想区分衣物类商品列表和食品类商品列表，分别看它们的浏览量，可以在`onCreate`方法中添加如下代码：

   ```java
   public class FeedActivity extends Activity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            GrowingIO.getInstance().setPageName(this, "Clothing");
        }
   }
   ```

请注意

1. 必须在该`Activity`的`onCreate`方法中完成该属性的赋值操作。
2. 页面别名只能设置为字母、数字和下划线的组合。
3. 为查看数据方便，请尽量对iOS和安卓的同功能页面取不同的名称。

至此集成完毕。您需要在【添加新产品】页面进行检测并安装。安装成功后您可以在您的App中激活SDK，进行数据定义。具体的激活和圈选教程请看 [移动端直接圈选](https://docs.growingio.com/Features/circle/appcirclingapp_new.html)

### 采集Fragment数据

当一个`Activity`下同时在屏幕中显示多个`Fragment`时，我们无法判断将哪个作为页面统计。

如果您的应用中有这种情况，请在初始化时删除对于`Configuration.trackAllFragments`的调用，这样就不会默认采集任何`Fragment`的数据。

然后使用下面的接口，在`Activity`中指定某一个`Fragment`作为页面进行数据采集：

```text
GrowingIO.trackFragment(Activity activity, Fragment fragment)
```

请在`Fragment`添加到`Activity`之前调用此接口，每个`Fragment`对象调用一次即可。

### 采集GPS\(地理位置信息\)数据

注：Android SDK暂时没办法自动获取GPS数据，如果您要采集GPS数据，需要在您的App每次获取完GPS数据之后，通过以下Api告知SDK。  
在您的App获取GPS坐标后，调用如下接口进行设置

```text
GrowingIO.getInstance().setGeoLocation(latitude, longitude);
```

其中，`latitude`是纬度，`longitude`是经度。

当用户下一次切换页面，或者发生点击行为时，GPS数据会被发送回GrowingIO。

如果您需要清除用户的GPS信息，请调用如下接口

```text
GrowingIO.getInstance().clearGeoLocation();
```

### 采集输入框数据

如果您需要采集应用内某个输入框内的文字（例如搜索框），请调用如下接口进行设置

```text
GrowingIO.getInstance().trackEditText(EditText);
```

其中，`EditText`代表要被采集的输入框。

当这个输入框失去焦点（包括应用退到后台），且输入框内容跟获取焦点前相比发生变化时，输入框内文字会被发送回GrowingIO。

请注意：对于密码输入框，即便标记为需要采集，SDK也会忽略，不采集它的数据。

### 渠道设置

为方便用户生成不同渠道的安装包，我们除了允许在Configuration的setChannel方法中设置渠道以外还允许在AndroidManifest.xml中通过MetaData设置安装包渠道：

```text
  <meta-data android:name="com.growingio.android.GConfig.Channel" android:value="Your ChannelID"/>
```

### 启用Hashtag识别

对于 1.1.4 及以上 SDK 版本，在 SDK 初始化方法中设置

```text
    GrowingIO.startWithConfiguration(this, new Configuration().setHashTagEnable(true)）
```

## 6. 其他配置项

### 自定义维度

GrowingIO的数据分析工具提供了例如“应用版本”，“渠道”，“城市”，“设备型号”等等这些通用维度。但在使用过程中，有时无法满足用户对特定数据维度的分析要求。

为了能够让数据分析变得更加的灵活，我们提供了自定义维度的接口，使用者可以对各种对象设置属性。

**这些属性在作图时，将表现为维度。**

#### 用户属性

用户属性只能用来表示登录用户本身的属性，至少包括用户ID。

根据需求，可以用来指定用户的各种属性

1. 自然属性，比如性别、出生年月等。
2. 账户属性，比如等级、类型标签等。
3. 行为特征，比如是否有过购买记录之类。

用户属性被称为CS字段，最多支持十个，从CS1到CS10，接口如下：

```java
GrowingIO growingIO = GrowingIO.getInstance();
growingIO.setCS1("CS1的key", "CS1的value");
growingIO.setCS2("CS2的key", "CS2的value");
...
growingIO.setCS10("CS10的key", "CS10的value");
```

在下面的例子中，总计上传5个用户属性，分别是：

CS1: user\_id:100324  
CS2: company\_id:943123  
CS3: user\_name:张溪梦  
CS4: company\_name:GrowingIO  
CS5: sales\_name:销售员小王

```java
private void setGrowingIOCS() {
    GrowingIO growingIO = GrowingIO.getInstance();
    growingIO.setCS1("user_id", "100324");
    growingIO.setCS2("company_id", "943123");
    growingIO.setCS3("user_name", "张溪梦");
    growingIO.setCS4("company_name", "GrowingIO");
    growingIO.setCS5("sales_name", "销售员小王");
}
```

**CS字段设置条件和限制**

1. CS 字段不能是和用户没有直接关系的属性，比如不能是订单 ID，商品 ID 等。
2. CS1 字段：在 GrowingIO 系统中用于识别注册用户的身份，因此 CS1 的 value 必须填写用户的唯一身份标示 ID。
3. CS2 字段：在 GrowingIO 系统中用于识别 SaaS 客户的租户，因此所有的 SaaS 用户必须填写租户的唯一身份标示 ID，非 SaaS 用户不做限定。
4. 对于未登录用户，不要设置任何CS字段。
5. 如果没有用到所有的CS字段，剩下的可以不设置。
6. 同一个CS字段，必须保持在各个平台意义相同。

**CS1字段设置时机**

基本原则：当App使用者的登录状态改变时设置CS1字段的值

用户手动登录 1. 如果有多个登录入口，在每一个入口登录成功后，都需要调用`GrowingIO.setCS1`来设置用户的唯一标识 2. 如果有第三方登录，成功登录后需要调用`GrowingIO.setCS1`方法

自动登录：App启动时，自动登录或者用户默认是登录状态，也需要调用`GrowingIO.setCS1`方法

注册：有的App注册成功后，默认登录，这种情况下也需要调用`GrowingIO.setCS1`方法

退出：退出登录后，请勿继续上传CS字段，即使是空值也请勿上传。

**其他CS字段遵循相似的设置时机**

**在上传成功两小时后，您需要在「项目管理-项目配置-CS 配置中」进行字段配置和激活，配置成功后便可开始使用 CS 字段进行分析。配置过程请参考 **[**属性数据\(CS\)上传配置文档**](https://docs.growingio.com/attribution-data.html)**。**

### 设置界面元素内容

SDK默认不会采集ImageView的内容，如果您需要区分不同的ImageView，可以使用contentDescription来标记，也可以调用下方的方法来设置：

```java
GrowingIO.setViewContent(View view, String content);
```

### 设置界面元素ID

调用了`useID`方法后，SDK将会使用Layout文件中的ID来识别一个元素。

如果部分元素在Layout文件中没有ID，建议在Layout文件中添加。

对于动态生成的元素，可以使用如下方法对它设置唯一的ID：

1. 调用GrowingIO.setViewID\(View view, String viewID\)。第一个参数是要设置的View，第二个是给这个View的ID。
2. 如果在ViewGroup上设置ID的话，SDK会忽略他所有子元素的默认ID（就是写在xml文件里的）只会使用GrowingIO.setViewID设置的ID。
3. ID只能设置为字母、数字和下划线的组合。

### 忽略元素

如果您需要忽略某些特殊内容，比如倒计时元素或涉及隐私的内容，可以使用该功能。

```java
GrowingIO.ignoreView(View view)
```

### 设置元素对象

如果元素自身的内容并不能代表具体的意义，可以使用元素对象来标识。

例如“加入购物车”按钮，可以设置成加入购物车的具体商品名称或ID。

```text
GrowingIO.setViewInfo(View view, String info);
```

### 动态添加View

如果您有某些View动态添加到ViewTree中并且在父容器中的位置不固定（例如常见的多Fragment实现的Tab切换），请给每个View设置ID来辅助统计

```java
View content = getLayoutInflater().inflate(R.layout.content_view, container, false);

GrowingIO.setTabName(content, "MyContent");
```

### 自定义点击事件

如果您有自定义的控件重写了`View`的`onTouchEvent`方法来判断和处理点击事件，那么必须调用它的`PerformClick`，并且设置相应的`onClickListener`。

至此，您的SDK安装就成功了。您登录 GrowingIO 进入产品安装页面执行“数据检测”几分钟后就可以看到数据了。

