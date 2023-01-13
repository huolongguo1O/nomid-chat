from json import dumps, loads
import random
import sys
import time
sys.path.append("../")
import base
import asyncio
import websocket
import _thread

class DelServer(base.CommandBase):
	def __init__(self,websocket,users,data):
		base.CommandBase.__init__(self,
			websocket=websocket,
			users=users,
			data=data)

	def execute(self):


			base.serverwss[base.servernames.index(self.data["name"])].close()
			

