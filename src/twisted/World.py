from Player import Player
from NetDefine import NetKeyName,NetActionType

class World(object):
    def __init__(self,playerMaster):
        self.playerMaster = playerMaster
        self.playerList = set()
        self.playerList.add(playerMaster)
        
    def checkCanJoinWorld(self,player):
        return len(self.playerList) < 8

    def addPlayer(self,player):    
        if(player not in self.playerList):
            self.playerList.add(player)
            player.joinWorld(self)

    def removePlayer(self,player):
        self.playerList.remove(player)
        player.leaveWorld()

        data = {}
        data[NetKeyName.ACTION] = NetActionType.PlayerLeaveWorld.value
        data[NetKeyName.UUID] = player.uuid
        self.receiveMsg(player,data)        

    def receiveMsg(self,player,obj):
        for p in self.playerList:
            if(p != player):
                p.receiveMsg(obj)

