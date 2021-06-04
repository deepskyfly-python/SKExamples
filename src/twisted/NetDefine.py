from enum import Enum,auto

class NetKeyName:
    ACTION = 'action'
    ACTOR_TYPE = 'actor'
    UUID = 'uuid'
    TIME = 'time'

class NetActionType(Enum):
    None_ = 0
    Login = auto()
    LoginSuccess = auto()
    SyncPlayerInfo = auto()
    JoinWorld = auto()
    JoinWorldSuccess = auto()
    BeListenServer = auto()
    LeaveWorld = auto()
    PlayerLeaveWorld = auto()
    ObjectUpdate = auto()
    ObjectDestroy = auto()




