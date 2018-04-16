1. 报错：
```
Error:Could not download vds-class-rewriter.jar         (com.growingio.android:vds-class-rewriter:0.9.99): No cached     version available for offline mode
```
因为开启了Android studio的Preferences中Build，Execution，DeployMent选项的Gradle选项卡中的Offline Work模式，导致只使用本地gradle仓库，不会从线上下载jar包，关闭即可。 

2. 报错：`FATAL EXCEPTION: main java.lang.IllegalStateException`
解决：保证gradel版本至少1.5以上。

3. 报错： `Could not find class 'com.tencent.smtt.sdk.WebView’`
原因为 app 中没有使用 X5内核的WebView，不会影响 app使用。

4. 报错：`org.json.JSONException: No Value for tags `
此为刚集成没有圈选任何指标，服务器返回的错误。

5. 报错：
```
Error:Execution failed for task ':app:transformClassesWithDexForDevelopDebug'.
>com.android.ide.common.process.ProcessException: org.gradle.process.internal.ExecException: Process 'command 'C:\Program Files\Java\jdk1.8.0_66\bin\java.exe'' finished with non-zero exit value 1
```
因为方法总数过多，超过了65536个，建议用分包的方式解决。

6. 报错：`Your agent and class rewriter versions do not match: agent = 0.9.93 class rewriter = 0.9.100. You probably need to update one of these components. If you're using gradle and just updated, run gradle -stop to restart the daemon.`
原因为android studio默认开启了 gradle 的 daemon 进程，会缓存我们的 sdk。可关闭 daemon 进程并允许 gradle clean命令。

7. 集成时报错 `OutofMemoryError`。
原因为编译的时候内存不够了，可以把 gradle.properties 中 `org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8`
这个注释去掉（此注释是给编译时分配更多内存，不会拖慢编译速度；SDK 编译时消耗的内存取决于您代码的复杂程度）。
