# GrowingIO数据平台API

### ChangeLog

2017-02-21 增加打点原始数据导出
1. visit数据增加新字段lat, lng, 为mobile平台采集的gps信息
2. 增加打点数据的导出，具体格式参考custom_attr表字段说明

#### 2016-09-08 增加访问级别的query与ps页面信息字段
1. 在visit级别增加新字段query，用于提取用户访问时的utm字段信息
2. 在page级别增加新字段pagegroup, ps1~ps10，对应sdk采集时设置的页面信息字段



#### 2016-08-09 导出数据增加action_tag与rules两张数据表
1. 导出数据中增加action_tag数据，用于关联action级别数据中的action_id与rule_id字段
2. rules表用于关联rule_id与rule名称，便于进一步分析GrowingIO平台圈选的标签数据
3. action_tag与之前的导出数据接口一致，在获取的下载链接中多出action_tag一项，而rules需要通过额外接口获取


#### 2016-07-30 在action级别数据中增加字段index，info。
1. index用于标记列表中的第几项项目，为bigint类型
2. info用于用户自定义添加的标识信息，string类型，对应数据采集时growingAttributesInfo定义的属性
3. 此次修改仅在action级别增加字段信息，visit与page不受影响


#### 2016-06-05

1. 认证的时候需要传入 tm 参数，tm 是当前时间戳（**毫秒**)
2. insights API 支持传入 expire 参数，来控制链接过期时间，默认 5 分钟。
3. insights API 可以请求小时数据，比如 2016060510，表示获取6月5号10点到11点的数据。