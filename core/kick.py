from json import dumps
import sys
sys.path.append("../")
import base
import asyncio
import websocket
# {'cmd':'login','addr':addr,'name':name}
class Kick(base.CommandBase):
	def __init__(self,websocket,users,data):
		base.CommandBase.__init__(self,
			websocket=websocket,
			users=users,
			data=data)

	def execute(self):
		'''
		for user in self.users.userset:
			if user.websocket == self.websocket:

				if user.level==100:
					return
		'''

		for user in self.users.userset:
			# print(user.nick)
			if user.nick==self.data['name']:
				print(user.nick+' kicked')
				user.channel='kicked'
