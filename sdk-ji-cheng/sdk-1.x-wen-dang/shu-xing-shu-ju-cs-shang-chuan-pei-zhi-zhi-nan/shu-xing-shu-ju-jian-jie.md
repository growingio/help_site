# 属性数据简介

## 什么是用户属性字段?

用户属性数据，用来存储和上传您数据库里的用户属性，如用户 ID，性别，年龄等。GrowingIO 通过您上传的 UserID 将您的用户信息和 GrowingIO 获取的用户行为数据进行匹配，方便您对自己的用户做更深入的分析。

## 为什么要上传用户属性字段?

当您想要分析自己的用户信息如性别，年龄时，您可以将您数据库里关于用户的信息，通过 GrowingIO 的接口，上传到 GrowingIO 的服务器中。上传成功后，您便可以在作图中将这些信息作为维度进行分析，如分析不同年龄层的用户使用您产品的差异情况等。

## 怎么上传用户属性字段?

GrowingIO 支持您通过 SDK 上传和 API 上传用户属性数据，字段总数不超过20个。CS1 -CS10 字段必须使用 SDK 上传。如果 10 个字段不能满足您的需求，再通过 API 上传其他字段。操作过程请参考 SDK 上传说明文档 和 API 上传说明文档。

在上传成功两小时后，您需要在「项目管理-项目配置-用户属性配置中」进行字段配置和激活，配置成功后便可开始使用用户属性字段进行分析。操作过程请参考用户属性数据上传配置文档。

注：用户属性数据当前只适用于上传用户的属性，不能用于其他类型数据的上传。例如：订单 ID，商品ID等。

## 上传什么样的属性数据？

**SaaS行业建议上传以下内容**

| 用户属性字段 | 上传内容 | 类型 | 定义 |
| --- | --- | --- | --- |
| CS1 | 用户ID （User ID） | String | 唯一标示一个注册用户的ID |
| CS2 | 公司ID （Tenant ID） | String | 客户公司的唯一ID |
| CS3 | 用户名称 （User Name） | String | 用户的名字 |
| CS4 | 公司名称 （Tenant Name） | String | 客户公司名称 |
| CS5 | 客户级别（Account Level Name） | String | 比如 战略客户，重点客户，一般客户，免费客户等 |
| CS6 | 客户付费状态（Tenant\_is\_Paid） | String | 如： 付费，免费 |
| CS7 | 客户行业（Industry） | String | 如： 电商行业，SaaS行业，在线教育行业，互联网金融行业，社交行业，硬件行业 等行业类型 |
| CS8 | 客户成功名称 （Customer Success Name） | String | 公司内客户成功人员的名称 |
| CS9 | 销售名称（Sales Name ） | String | 公司内销售名称 |
| CS10 | 用户所在部门 （Department） | String | 市场部，产品部，运营部门 |
| CS11 | 购买帐号数 | Double | 客户购买的账户数量 |
| CS12 | 已经激活帐号数 | Double | 客户激活的账户数量 |
| CS13 | 合同签订日（Contract Date） | Double | 如：20160920，合同签订日： Contract Date     前端显示：已签约天数：   N天   N＝@today- Contract Date |
| CS14 | 合同到期日（Expire Date ） | Double | 合同到期日： Expire Date         前端显示： 距到期期：       M天  M＝ Expire Date－@today |

