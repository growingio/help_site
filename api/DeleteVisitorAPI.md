1. 调用DeleteVisitor API之前先准备好哪些访问用户ID的数据需要删除
2. 基于准备好需要删除的访问用户ID，调用DeleteVisitor API 
    - **服务器请求接口**
      1. 服务器请求URL：https://data.growingio.com/{projectId}/deleteVisitor?auth={auth_token}
      2. 服务器请求header：
          - Access-Token = publicKey
          - Content-Type = application/json
      3.  服务器请求body：
{  
    "visitUserId":["abcdef","bcdefg",...]
}
    - **示例说明**：
      1. visitUserId是GrowingIO生成的ID，用以代表匿名的访问用户
      2. deleteVisitor API，单个请求上传的数据包总大小不超过2MB，内含u的个数不超过100个
    - **{auth_token}由如下三个参数计算生成**
      1. projectId: 由GrowingIO分配给您的项目ID
      2. secretKey：由GrowingIO分配给您的私钥
      3. keyArray：对于一次上传多条记录时，取多条数据中的每个对象的主键的值
    - **计算公式**
      1. 以secretKey为key
      2. 使用SHA256算法计算字符串"projectId=${projectId}&visitUserId=${keyArray}"的hash值
