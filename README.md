# Nomid Chat
基于`Python server from hack.chat`改编，
新增了addserver命令，权限100及以上

使用`/addserver [remote websocket] name`连接其他服务器，
如：`/addserver wss://hack.chat/chat-ws`，
连接仅会影响一个频道

## 安装方式
使用`python main.py`运行，注意修改`main.py:75`的`websocket`端口，
`client/client.js:306`也要一起改，
建议打开反向代理。

## 使用方式
在主页后追加`?{channelname}`进入特定频道
|命令|说明|
|-|-|
|/w nick 内容|发送私信|
|/color #颜色|设置颜色|
|/addserver ws name|添加服务器，ws:ws://服务器地址|
|/kick nick|踢人|
### config
所有配置在`config.py`中，必须修改
```
servername='test' # 服务器名字
serveraddr='ws://test.example/awa'
mods=['NGY5Zj'] # 管理识别码
salt='just for test' # 识别码计算用salt
```

### 识别码
加入时昵称后加`#密码`即可出现识别码

## 技术原理
说白了不算去中心化，就是多个服务器相连接

## LICENSE
使用GPL，防止有人改服务器
client文件夹下的代码遵循MIT许可证
