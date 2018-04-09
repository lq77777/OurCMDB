# 资产管理系统CMDB
## 功能介绍
* 基于python3
* Django 1.8.2
* SB-admin模板

### 2018-03-27 更新日志
*  新建CMDB项目
*  数据建模
*  setting设置，app、数据库、时间、static、media文件
*  选择模板SB-admin v2.0，放置静态文件、修改静态文件路径、汉化
*  用户添加（CMDB很少提供用户注册，大部分支持用户添加）
    *  register 模态框
    *  form表单，定义表单项，表单校验（前端校验，手机号、密码验证）

### 2018-03-28 更新日志
*  form表单，submit提交会刷新页面，使用ajax动态局部提交
*  数据建模