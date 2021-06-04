from NetDefine import NetKeyName,NetActionType
import json

class Player(object):
    def __init__(self,uuid,protl):
        self.uuid = uuid
        self.name = 'Player_'+str(uuid)
        self.level = 1
        self.serverProtl = protl
        self.world = None

    def isInWorld(self):
        return self.world != None

    def controlWorld(self,world):
        self.world = world
        self.sendAction(NetActionType.BeListenServer)

    def joinWorld(self,world):
        self.world = world
        self.sendAction(NetActionType.JoinWorldSuccess)

    def leaveWorld(self):
        self.world = None
        self.sendAction(NetActionType.LeaveWorld)
        
    def postLogin(self):
        self.sendAction(NetActionType.LoginSuccess)

    def receiveMsg(self,obj):
        print("send to client : <{}>".format(self.serverProtl.transport.getPeer()))
        print(obj)
        self.serverProtl.sendString(bytes(json.dumps(obj),'utf-8'))
        
    def sendAction(self,actionType):
        data = {}
        data[NetKeyName.ACTION] = actionType.value
        data[NetKeyName.UUID] = self.uuid
        print(json.dumps(data))
        self.serverProtl.sendString(bytes(json.dumps(data),'utf-8'))


