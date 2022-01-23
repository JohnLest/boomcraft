from typing import List
from pydantic import BaseModel
from models.userModel import UserModel
from models.resourcesModel import ResourceModel


class PlayerInfoModel(BaseModel):
    user: UserModel
    own_resources: List[ResourceModel]
    game_resources: List[ResourceModel]
    key_socket: object
