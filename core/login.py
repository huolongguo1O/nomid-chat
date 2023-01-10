from json import dumps
import sys
sys.path.append("../")
import base
import asyncio
import websocket
# {'cmd':'login','addr':addr,'name':name}
class Login(base.CommandBase):
	def __init__(self,websocket,users,data):
		base.CommandBase.__init__(self,
			websocket=websocket,
			users=users,
			data=data)

	def execute(self):
		print('somebody loged in')
		base.serveraddrs.append({'ws':self.websocket,'channel':self.data['channel']})

			