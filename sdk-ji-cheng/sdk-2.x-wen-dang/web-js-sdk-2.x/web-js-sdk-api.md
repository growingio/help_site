# Web JS SDK API

## API简介：

```text
// 初始化参数
gio('init', projectId, options); 

// 修改系统变量API
gio('config', options);

// 发送事件API
gio('track', eventId);
gio('track', eventId, number);
gio('track', eventId, eventLevelVariables);
gio('track', eventId, number, eventLevelVariables);

// 发送页面级变量API
gio('page.set', key, value);
gio('page.set', pageLevelVariables);

// 发送转化变量API
gio('evar.set', key, value);
gio('evar.set', conversionVariables);

// 发送用户变量API
gio('people.set', key, value);
gio('people.set', customerVariables);

// 设置登录用户ID
gio('setUserId', userId); 

// 清除登录用户ID
gio('clearUserId');
```

### init

初始化参数，设置项目ID和一些常用的配置项。

参数：

| 参数名称 | 参数类型 | 是否必须 | 说明 |
| :--- | :--- | :--- | :--- |
| projectId | String | 是 | 项目ID |
| options | JSON Object | 否 | 系统变量配置 |

```text
//init API原型
gio('init', projectId, options);
```

```text
//init API调用示例
//配置imp类型的数据关闭发送
gio('init', '1234567890', {'imp':false});
```

### track

发送一个事件。在添加所需要发送的事件代码之前，需要在打点管理用户界面配置事件以及事件级变量。

参数：

| 参数名称 | 参数类型 | 是否必须 | 说明 |
| :--- | :--- | :--- | :--- |
| eventId | String | 是 | 事件标识符 |
| number | Number | 否 | 事件的数值，没有number参数时，事件默认加1；当出现number参数时，事件自增number的数值。 |
| eventLevelVariables | JSON Object | 否 | 包含事件级变量的JSON对象，暨事件发生时所伴随的维度信息。 |

```text
// track API原型
gio('track', eventId, eventLevelVariables);
gio('track', eventId, number, eventLevelVariables);
```

```text
// track API调用示例一
gio('track', 'registerSuccess');
```

```text
// track API调用示例二
gio('track', 'registerSuccess', {'gender':'male', 'age':21});
```

```text
// track API调用示例三
gio('track', 'loanAmount', 800000, {'loanType':'houseMortgage','province':'Zhejiang'});
```

### page.set

发送页面级别的维度信息，在添加代码之前必须在打点管理界面上声明页面级变量。

参数：

| 参数名称 | 参数类型 | 是否必须 | 说明 |
| :--- | :--- | :--- | :--- |
| key | String | 否 | 页面级变量的标识符 |
| value | String | 否 | 页面级变量的值 |
| pageLevelVariables | JSON Object | 否 | 包含页面级变量的JSON对象，暨页面级别的信息 |

```text
// page.set API原型
gio('page.set', key, value);
gio('page.set', pageLevelVariables);
```

```text
// page.set API调用示例一
gio('page.set', {'pageName': 'Home Page', 'author': 'Zhang San'});
```

```text
// page.set API调用示例二
gio('page.set', 'author', 'Zhang San');
```

### evar.set

发送一个转化信息用于高级归因分析，在添加代码之前必须在打点管理界面上声明转化变量。

参数

| 参数名称 | 参数类型 | 是否必须 | 说明 |
| :--- | :--- | :--- | :--- |
| key | String | 否 | 转化变量的标识符 |
| Value | String | 否 | 转化变量的值 |
| conversionVariables | JSON Object | 否 | 包含转化变量的JSON对象 |

```text
// evar.set API原型
gio('evar.set', key, value);
gio('evar.set', conversionVariables);
```

```text
// evar.set API调用示例一
gio('evar.set', 'campaignId'，'1234567890');
```

```text
// evar.set API调用示例二
gio('evar.set', {'campaignId': '1234567890', 'campaignOwner':'lisi'});
```

### people.set

发送用户信息用于用户信息相关分析，在添加代码之前必须在打点管理界面上声明转化变量。

参数：

| 参数名称 | 参数类型 | 是否必须 | 说明 |
| :--- | :--- | :--- | :--- |
| key | String | 否 | 用户变量的标识符 |
| value | String | 否 | 用户变量的值 |
| customerVariables | JSON Object | 否 | 包含用户变量的JSON对象 |

```text
// people.set API原型
gio('people.set', key, value);
gio('people.set', customerVariables);
```

```text
// people.set API调用示例一
gio('people.set', 'gender', 'male');
```

```text
//people.set API调用示例二
gio('people.set', {'gender':'male', 'age':'25'});
```

### setUserId

当用户登录之后调用setUserId API，设置登录用户ID。

参数：

| 参数名称 | 参数类型 | 是否必须 | 说明 |
| :--- | :--- | :--- | :--- |
| userId | String | 是 | 用户的登录用户ID |

```text
//setUserId API原型
gio('setUserId', userId);
```

```text
//setuserId API调用示例
gio('setUserId', '1234567890');
```

### clearUserId

当用户登出之后调用clearUserId，清除已经设置的登录用户ID。

```text
//clearUserId API原型和调用示例
gio('clearUserId');
```

### sendPage

在默认情况下，由于用户浏览网站的交互行为导致当前页面的URL产生变化时，GrowingIO的Web JS SDK会发送一个page类型的请求。在一些特殊的情况下，例如用户在访问单页应用（Single Page Application）类型的网站时，用户的操作会导致业务上面理解的页面产生了变化，但是当前的URL可能并没有改变。

这时，可以调用GrowingIO提供的sendPage接口手动发送页面浏览事件。这个接口的调用将会发送出一条‘page’类型的数据，GIO服务器在收到page类型的数据之后，页面浏览量这个预定义指标会加1。

```text
//sendPage API原型和调用示例
gio('sendPage');
```

