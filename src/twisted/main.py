from twisted.internet import endpoints, reactor, protocol
from twisted.protocols import basic
from NetDefine import NetActionType,NetKeyName
from Player import Player
from World import World
import json

class STServer(object):
    def __init__(self):
        self.playerServerID = 10000
        self.playerMap = {}        
        self.clients = set()

    def clientConnected(self, client):
        print("client connected: <{}>".format(client.transport.getPeer()))
        self.clients.add(client)

    def clientDisconnected(self, client, reason):
        print("client disconnected: <{}>, reason: <{}>".format(client.transport.getPeer(), reason))
        self.clients.remove(client)
        #移除 playerMap
        if(client.player != None):
            if(client.player.isInWorld()):
                client.player.world.removePlayer(client.player)
            del self.playerMap[client.player.uuid]
        
    def clientObjectReceived(self, client,obj):
        actionType = obj[NetKeyName.ACTION]
        player = client.player
        #Login
        if(actionType == NetActionType.Login.value):
            self.clientLogin(client,obj)
            return

        #Action
        if(player == None):
            print("client : <{}>, player is none".format(client.transport.getPeer())) 
            return

        if(actionType == NetActionType.JoinWorld.value):
            world = self.searchServerPlayer(player,obj)
            if(world != None):
                world.addPlayer(player)                
        elif(actionType >= NetActionType.ObjectUpdate.value):
            player.world.receiveMsg(player,obj)


    def clientLogin(self,client,obj):
        print(obj)
        self.playerServerID +=1
        player = Player(self.playerServerID,client)
        client.player = player
        self.playerMap[self.playerServerID] = player
        player.postLogin()

    def searchServerPlayer(self,player,obj):
        #单人的 其他玩家
        for v in self.playerMap.values():
            if(v != player):
                if(v.isInWorld() == False):
                    world = World(v)
                    v.controlWorld(world)
                    return world
                elif(v.world.checkCanJoinWorld(player)):
                    return v.world

        return None



class STServerProtocol(basic.Int32StringReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.buffer = ''
        self.player = None

    def connectionMade(self):
        GServer.clientConnected(self)        

    def connectionLost(self, reason):
        GServer.clientDisconnected(self, reason)

    def stringReceived(self, string):
        o = None
        try:
            o = json.loads(string)
        except:
            print('json parse error')
        if o != None:
            print('get data from ===={}'.format(self.transport.getPeer()))
            GServer.clientObjectReceived(self,o)
        

class STServerFactory(protocol.Factory):
    def __init__(self):
        pass

    def buildProtocol(self, addr):
        return STServerProtocol(self)

GServer = STServer()
endpoints.serverFromString(reactor, "tcp:11025").listen(STServerFactory())

print("server start")
reactor.run()

