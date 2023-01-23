from json import dumps, loads
import random
import sys
import time
sys.path.append("../")
import base
import asyncio
import websocket
import _thread
def handler(ws,users,userobj,sn):

	while 1:
		data=loads(ws.recv())
		if data["cmd"]=="info":
			if "type" in data:
				if data["type"]=="whisper":
					data["text"]=data["text"].replace(data["from"],data["from"]+'-'+sn,1)
					t=data["text"].split(' ',4)
					for i in users.userset:

						if t[2] == i.nick and i.channel==userobj.channel:
							users.sendto(data,i)





		if data['cmd']=='chat':
			if '-' not in data['nick']:
				data['nick']+='-'+sn
			

				users.broadcasttextfromserver(userobj.channel,dumps(data))
				print('Turning a packet from another server')
		'''
		if data['cmd']=='onlineAdd':
			data['nick']+='-'+sn

			users.broadcasttextfromserver(userobj.channel,dumps(data))
		if data['cmd']=='onlineRemove':
			data['nick']+='-'+sn

			users.broadcasttextfromserver(userobj.channel,dumps(data))
		'''
		'''if data['cmd']=='onlineSet':
			if 'servername' in data:
				sn=data['servername']
		'''
		if True:
			pass
			'''
			for i in range(len(data['nicks'])):
				

				data['nicks'][i]+='-'+sn
				broadcastdata = {
					"cmd":"onlineAdd",
					"nick":data['nicks'][i],
					"uType":"user",
					"hash":'Another server',
					"level":100,
					"userid":random.randint(0,1145141919810),
					"isbot":'True',
					"channel":userobj.channel,
					"time":round(time.time())
					}
				users.broadcasttextfromserver(userobj.channel,dumps(broadcastdata))
			'''

class AddServer(base.CommandBase):
	def __init__(self,websocket,users,data):
		base.CommandBase.__init__(self,
			websocket=websocket,
			users=users,
			data=data)

	def execute(self):

		if "servername" in self.data:
			for user in self.users.userset:
				if user.websocket == self.websocket:

					userobject = user 
					break
			print('Starting '+self.data['servername'])
	
			websocket1=websocket.create_connection(self.data['servername'])
			print('Connecting')	

			websocket1.send(dumps({"cmd":"join","nick":"server_"+base.servername,"channel":userobject.channel}))
			print('Joining')
			sn=self.data["sn"]

			base.serverwss.append(websocket1)

			base.servernames.append(sn)
			print('Add server done')
			_thread.start_new_thread( handler, (websocket1,self.users,userobject,sn,) )


