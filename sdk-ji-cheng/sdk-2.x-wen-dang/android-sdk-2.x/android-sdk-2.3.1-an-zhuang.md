# Android SDK 2.3.1 安装

Android SDK 2.3.1安装

## 1.导入SDK

Gradle编译环境（AndroidStudio）

### \(1\)在project级别的build.gradle文件中添加`vds-gradle-plugin`依赖

```java
buildscript {
    repositories {
        jcenter()
        google()
    }
    dependencies {
        //gradle建议版本
        classpath 'com.android.tools.build:gradle:3.0.1'
        classpath 'com.growingio.android:vds-gradle-plugin:2.3.1'
    }
}

allprojects {
    repositories {
        jcenter()
    }
}
```

### \(2\)在module级别的build.gradle文件中添加`com.growingio.android`插件、`vds-android-agent`依赖和对应的资源；

URL Scheme的格式是growing.xxxxxxxxxxxxxxxx，它的获取方式有两种：

* 新产品的 URL Scheme ：登录官网 -&gt;点击项目选择框 -&gt; 点击“项目管理” -&gt; 点击“应用管理” -&gt; 点击“新建应用”-&gt; 选择添加Android应用 -&gt; 第二段中"此应用的 URL Scheme 为:growing.xxxxxxxxxxxxxxxx”中标黄字体。
* 现有产品的 URL Scheme ：登录官网 -&gt;点击项目选择框 -&gt; 点击“项目管理” -&gt; 点击“应用管理” -&gt; 找到对应产品的URL Scheme。

![&#x9879;&#x76EE;&#x7BA1;&#x7406;](../../../.gitbook/assets/image%20%281%29.png)

```java
apply plugin: 'com.android.application'
//添加插件
apply plugin: 'com.growingio.android'

android {
    defaultConfig {
        resValue("string", "growingio_project_id", "您的项目ID")
        resValue("string", "growingio_url_scheme", "您的URL Scheme")
    }
}
dependencies {
        compile 'com.growingio.android:vds-android-agent:2.3.1@aar'
}
```

## 2.添加URLScheme和网络权限

把URL Scheme添加到您的项目，以便我们唤醒您的程序，进行圈选。将该产品的URLScheme添加到你的AndroidManifest.xml中的LAUNCHER Activity下。例如：

```java
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.growingio.testdemo">

    <!--请注意添加网络权限-->
    <uses-permission android:name="android.permission.INTERNET" />
    <!--非危险权限，不需要运行时请求，Manifest文件中添加即可-->
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW"/>

    <!--请注意<application/>标签中的name属性值（这里为android:name=".MyApplication"）必须为您的Application类-->
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:name=".MyApplication"
        android:theme="@style/AppTheme">
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <!--请添加这里的整个 intent-filter 区块，并确保其中只有一个 data 字段-->
            <intent-filter>
                <data android:scheme="growing.您的URL Scheme" />
                <action android:name="android.intent.action.VIEW" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
            </intent-filter>
            <!--请添加这里的整个 intent-filter 区块，并确保其中只有一个 data 字段-->
        </activity>
    </application>

</manifest>
```

## 3. 初始化SDK

请将以下 GrowingIO.startWithConfiguration加在您的Application 的 onCreate 方法中

```java
public class MyApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        GrowingIO.startWithConfiguration(this, new Configuration()
        .useID()
        .trackAllFragments()
        .setChannel("XXX应用商店"))
        .setDebugMode(true); //打开调试Log
    }
}
```

（1）请确保将代码添加在`Application`的`onCreate`方法中，添加到其他方法中可能导致数据不准确。

（2）其中`GrowingIO.startWithConfiguration`第一个参数为`Application`对象。

（3）使用`useID`方法，能够更准确地统计界面元素，一般建议添加。

（4）`trackAllFragments`方法用于把`Fragment`自动识别为页面，但一个界面中只能同时显示一个`Fragment`。

（5）`setChannel`方法的参数定义了“自定义App渠道”这个维度的值。

添加代码之后，**请先 Clean 项目**，然后再进行编译。

## 4. 代码混淆

如果你启用了混淆，请在你的proguard-rules.pro中加入如下代码：

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

## 5.重要配置选项

### \(1\) 采集H5页面数据

如果您在App内嵌入了WebView（包括X5内核），请确保您已经调用过下面的方法，来采集H5页面的数据：

```java
WebView.setWebChromeClient(WebChromeClient client);
```

**请在第一次调用 WebView.loadUrl\(\) **之前调用以上方法。

### \(2\) 采集Banner数据

很多应用的界面上方都有横向滚动的 Banner 广告。

对于此类广告，如果您的应用通过 ViewPager、AdapterView 或者 RecyclerView 实现，请在 Banner创建时（包括动态创建）调用下面的接口来采集数据。

```text
GrowingIO.getInstance().trackBanner(banner, bannerDescriptions)
```

其中 bannerDescriptions 是 List&lt;String&gt;类型，包含所有广告图对应的广告内容描述，内容描述需要跟广告的顺序相同。

例如，当您有 5 张广告图时，只需创建一个 String 类型的 List，然后按 5 个广告出现的顺序给 List 的元素设置对应的广告描述，同样设置 5 个元素即可。

### \(3\) 采集GPS数据

如果您需要采集用户的GPS数据，请在获取坐标后，调用如下接口进行设置

```text
GrowingIO.getInstance().setGeoLocation(latitude, longitude);
```

其中，`latitude`是纬度，`longitude`是经度。

当用户下一次切换页面，或者发生点击行为时，GPS数据会被发送回GrowingIO。

如果您需要清除用户的GPS信息，请调用如下接口

```text
GrowingIO.getInstance().clearGeoLocation();
```

### \(4\) 采集输入框数据

如果您需要采集应用内某个输入框内的文字（例如搜索框），请调用如下接口进行设置

```text
GrowingIO.getInstance().trackEditText(EditText);
```

其中，`EditText`代表要被采集的输入框。

当这个输入框失去焦点（包括应用退到后台），且输入框内容跟获取焦点前相比发生变化时，输入框内文字会被发送回GrowingIO。

请注意：对于密码输入框，即便标记为需要采集，SDK也会忽略，不采集它的数据。

### \(5\) 启用Hashtag识别

在 SDK 初始化方法中设置

```text
    GrowingIO.startWithConfiguration(this, new Configuration().setHashTagEnable(true)）
```

