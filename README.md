# Nomid Chat
基于`Python server from hack.chat`改编，
新增了addserver命令，权限100及以上

使用`/addserver [remote websocket] name`连接其他服务器，
如：`/addserver wss://hack.chat/chat-ws`，
连接仅会影响一个频道

## 使用方式
使用`python main.py`运行，注意修改`main.py:75`的`websocket`端口，
`client/client.js:306`也要一起改

## 技术原理
说白了不算去中心化，就是多个服务器相连接

## LICENSE
使用GPL，防止有人改服务器
