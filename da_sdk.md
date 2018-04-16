# GrowingIO数据平台API SDK


**目前仅提供Java版本的GrowingIO数据平台API SDK**

#### 使用方式

在maven中添加依赖


```
    <repositories>
        <repository>
            <id>growingio</id>
            <url>https://oss.sonatype.org/service/local/staging/deploy/maven2</url>
        </repository>
    </repositories>

    <dependencies>
        <dependency>
            <groupId>com.growingio.growingapi</groupId>
            <artifactId>growing-api-java</artifactId>
            <version>0.0.1</version>
        </dependency>
    </dependencies>
```


或者将assembly包添加到classpath的lib路径中。`git clone`代码之后运行`mvn clean package｀获取assembly包。

然后添加配置文件(可以在resources目录下直接添加),若是使用GrowingDownloadApi,则添加growingApi.conf。也可以自己实现对应的DownloadApi,override其中的store方法即可。


#### AppDemo.java

growingApi.conf配置

```
app {
  # configure ai value, 在项目管理页面内（管理员权限）
  # ai: "abc12345678caf"

  # configure project Id, for example 'nxoa08md', 项目管理中的管理员有权限获取
  # projectId: "nxoa08md"

  # 秘钥,在项目管理页面内（管理员权限）
  # secretKey: "xxx"

  # 公钥,在项目管理页面内（管理员权限）
  # publicKey: "xxx"


  # 下面两个配置项为GrowingDownloadApi内配置项

  # 存储文件的绝对路径地址,可以override store()方法,控制数据存储
  # store: "/tmp"

  # 选择是否解压存储在目录下
  # uncompress: true
}

```

调用方式

```
    GrowingDownloadApi api = new GrowingDownloadApi();
    api.download("2016071221");
```