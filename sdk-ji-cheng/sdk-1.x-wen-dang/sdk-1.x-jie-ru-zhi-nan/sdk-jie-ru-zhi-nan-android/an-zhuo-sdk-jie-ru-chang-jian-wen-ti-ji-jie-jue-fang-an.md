# 安卓 SDK 接入常见问题及解决方案

**1.报错提示Error:Could not download vds-class-rewriter.jar \(com.growingio.android:vds-class-rewriter:0.9.99\): No cached version available for offline mode**

解决方案：是由于开启了"Android Studio"中 "Preferences"中"Build，Execution，DeployMent"中 gradle 选项卡中的 Offline Work模式，导致只使用本地 gradle 仓库，不会从线上下载 jar 包，按以上路径操作关闭该模式即可。

**2.在Android Studio下导入的eclipse项目，只有帮助文档中的module级别的build.gradle文件，没有project级别的build.gradle文件**

解决方案：建议在Android Studio中新建项目，并按目录级别替换eclipse开发的相应代码。

**3.严重异常FATAL EXCEPTION: main java.lang.IllegalStateException**

解决方案：gradel 版本至少1.5以上，即显示“classpath 'com.android.tools.build:gradle:1.5.0”； 并且 gradle 版本只能写一次，否则无法成功集成SDK。

**4.Error:Execution failed for task ':ziroom-main:vdsInstrumentTask' com.sun.tools.attach.AgentLoadException: Agent JAR not found or no Agent-Class attribute**

解决方案：请查看 gradle 缓存的 jar 目录，路径中间不可以出现空格或中文字符。

**5.plugin id 'com.growingio.android' not found**

解决方案：（1）检查集成第一步，buildscript &gt; dependencies &gt; classpath "com.growingio.android:vds-gradle-plugin:x.x.x" ；（2）没有加 jcenter 。

**6.Failed to resolve: com.growingio.android:vds-android:latest.release**

解决方案：是由于您开了代理引起的，关掉即可。

**7.Error:Execution failed for task ':app:transformClassesWithDexForDevelopDebug' ,&gt;com.android.ide.common.process.ProcessException: org.gradle.process.internal.ExecException: Process 'command 'C:\Program Files\Java\jdk1.8.0\_66\bin\java.exe'' finished with non-zero exit value 1**

解决方案：方法总数过多导致报错，如果目前的方法总数超过 60000，建议分包。

**8.Could not find class ‘com.tencent.smtt.sdk.WebView'**

解决方案：这个错误提示，是因为 App 中没有使用 X5 内核的 WebView，不会影响 App的集成。

**9.报错：org.json.JSONException: No Value for tags**

解决方案：这是您刚集成SDK没有圈选任何指标，服务器返回的错误。

**10.集成Android SDK，应用启动时正确在logcat中输出GrowingIO Android SDK的版本号和欢迎词，但是SDK并没有正常工作**

解决方案：将GrowingIO.startWithConfiguration中第一个参数改为在AndroidManifest.xml中注册的application的实例。

