import sys
sys.path.append("../")
import base


class RemoveServer(base.CommandBase):
	def __init__(self,websocket,users,data):
		base.CommandBase.__init__(self,
			websocket=websocket,
			users=users,
			data=data)

	def execute(self):
		if "color" in self.data:
			for user in self.users.userset:
				if user.websocket == self.websocket:
					user.color = self.data["color"]