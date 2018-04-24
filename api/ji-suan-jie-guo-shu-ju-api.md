# 计算结果数据 API

## 看板数据API 定义

注意：

1. 本页API中的project\_id、dashboard\_id、chart\_id字段，均可在项目页面url中找到，如："[https://www.growingio.com/admin/projects/nxog09md/dashboard/YoX28w7R](https://www.growingio.com/admin/projects/nxog09md/dashboard/YoX28w7R)" 中的"nxog09md"和"YoX28w7R"分别是project\_id和dashboard\_id。
2. 在进行导出之前，请务必参考[“GrowingIO接口认证”文档](https://docs.growingio.com/growingio_api_auth.html)，完成接口认证获取token。

### Resource

GET [https://www.growingio.com/projects/:project\_id/dashboards/:dashboard\_id.json](https://www.growingio.com/projects/:project_id/dashboards/:dashboard_id.json)

### Authorization

在 Header 里面添加两个属性：

| 名字 | 类型 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| X-Client-Id | String | GrowingIO 分配的公钥，请在GrowingIO后台“项目配置”页面获取 | X-Client-Id: 123abc |
| Authorization | String | 认证后获取到的 Token | Authorization: Token xxxxxx |

### Response

Status Code: 200 OK

```text
{
  id: "Dashboard Uid",
  name: "Dashboard Name",
  charts: [
    {
      id: "Chart Uid",
      name: "Chart Name",
      createor: "Chart Creator",
      createdAt: "Created Time"
    },
    {
      id: "Chart Uid",
      name: "Chart Name",
      createor: "Chart Creator",
      createdAt: "Created Time"
    }
  ]
}
```

## 单图数据API 定义

**单图下载每秒限速2次**

### Resource

GET [https://www.growingio.com/projects/:project\_id/charts/:chart\_id.json](https://www.growingio.com/projects/:project_id/charts/:chart_id.json)

注意：**跳出率、平均访问时长、每次访问页面浏览量、访问用户人均访问次数**以及基于以上指标的其他指标，在以**小时**为 interval 的请求中，返回值都为0。

### Authorization

在 Header 里面添加两个属性：

| 名字 | 类型 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| X-Client-Id | String | GrowingIO 分配的公钥，请在GrowingIO后台“项目配置”页面获取 | X-Client-Id: 123abc |
| Authorization | String | 认证后获取到的 Token | Authorization: Token xxxxxx |

### Query Parameter

| 名字 | 类型 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| startTime | integer | 数据起始时间 | 1462118400000 |
| endTime | integer | 数据结束时间 | 1462118400000 |
| interval | integer | 数据间隔 | 86400000 |

### Responses

Status Code: 200 OK

```text
{
  id: "Chart Uid",
  name: "Chart Name",
  startTime: 1462118400000,
  endTime: 1462118400000,
  interval: 86400000,
  meta: [
    { name: '城市', dimension: true },
    { name: '浏览器', dimension: true },
    { name: 'Metric 1', metric: true },
    { name: 'Metric 2', metric: true }
  ],
  data: [
    // 线图
    [timestamp, metric1, metric2],
    [timestamp, metric1, metric2]

    // 横向柱图
    [dimension_v1, metric1],
    [dimension_v2, metric1]

    // 纵向柱图
    [timestamp, metric1, metrics2],
    [timestamp, metric1, metrics2]

    // 表格
    [dimension1_v1, dimension2_v1, metric1, metric2],
    [dimension1_v2, dimension2_v1, metric1, metric2]

    // 聚合数字
    [metric1]

    // 气泡图
    [dimension_v1, metric1, metric2, metric3, metric4],
    [dimension_v2, metric1, metric2, metric3, metric4]

    // 双向柱图
    [dimension_v1, metric1],
    [dimension_v2, metric1]
  ]
}
```

## 分群 API 定义

### Resource

GET [https://www.growingio.com/projects/:project\_id/segmentations.json](https://www.growingio.com/projects/:project_id/segmentations.json)

### Authorization

在 Header 里面添加两个属性：

| 名字 | 类型 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| X-Client-Id | String | GrowingIO 分配的公钥，请在GrowingIO后台“项目配置”页面获取 | X-Client-Id: 123abc |
| Authorization | String | 认证后获取到的 Token | Authorization: Token xxxxxx |

### Query Parameter

无

### Responses

Status Code: 200 OK

```text
[
  {
    id: "Segmentation Uid",
    name: "Segmentation Name",
    userType: 'u',
    userNum: 1230,
    updatedAt: "2016-08-03"
  },
  {
    id: "Segmentation Uid",
    name: "Segmentation Name",
    userType: 'cs1',
    userNum: 1230,
    updatedAt: "2016-08-03"
  },
  ...
]
```

### Resource

GET [https://www.growingio.com/projects/:project\_id/segmentations/:segmentation\_id/users.csv](https://www.growingio.com/projects/:project_id/segmentations/:segmentation_id/users.csv)

### Authorization

在 Header 里面添加两个属性：

| 名字 | 类型 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| X-Client-Id | String | GrowingIO 分配的公钥，请在GrowingIO后台“项目配置”页面获取 | X-Client-Id: 123abc |
| Authorization | String | 认证后获取到的 Token | Authorization: Token xxxxxx |

### Query Parameter

无

### Responses

Status Code: 200 OK  
CSV 文件以 Tab 分隔，内容是上传的 CS 属性字段

```text
cs1_name    cs2_name    
12249    GrowingIO
```

## 规则逻辑 API 接口

### Resource

GET [https://www.growingio.com/projects/:project\_id/rules.csv](https://www.growingio.com/projects/:project_id/rules.csv)

### Authorization

在 Header 里面添加两个属性：

| 名字 | 类型 | 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| X-Client-Id | String | GrowingIO 分配的公钥，请在GrowingIO后台“项目配置”页面获取 | X-Client-Id: 123abc |
| Authorization | String | 认证后获取到的 Token | Authorization: Token xxxxxx |

### Query Parameter

无

### Responses

Status Code: 200 OK  
CSV 文件内容以 Tab 分隔

```text
ruleId,eventName,eventType
f2503720,元素_注册按钮,clck
```

Status Code: 401 Unauthorized

```text
{
  "message": "Unauthorized",
  "errors": []
}
```

Status Code: 500 Server Error

```text
{
  "message": "Request timeout",
  "errors": [
    {
      "code": "request_timeout",
      "message": "Request timeout in 5000 milliseconds"
    }
  ]
}
```

