# Nomid Chat
基于`Python server from hack.chat`改编
新增了addserver命令，权限100及以上

使用`/addserver [remote websocket] name`连接其他服务器
如：`/addserver wss://hack.chat/chat-ws`
连接仅会影响一个频道

使用`python main.py`运行，注意修改main.py:75的websocket端口
client/client.js也有一块要改