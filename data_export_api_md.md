# 数据导出API

### ChangeLog

#### 2016-07-30 在action级别数据中增加字段index，info。
1. index用于标记列表中的第几项项目，为bigint类型
2. info用于用户自定义添加的标识信息，string类型，对应数据采集时growingAttributesInfo定义的属性
3. 此次修改仅在action级别增加字段信息，visit与page不受影响


#### 2016-06-05

1. 认证的时候需要传入 tm 参数，tm 是当前时间戳（**毫秒**)
2. insights API 支持传入 expire 参数，来控制链接过期时间，默认 5 分钟。
3. insights API 可以请求小时数据，比如 2016060510，表示获取6月5号10点到11点的数据。