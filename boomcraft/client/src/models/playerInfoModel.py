from typing import List
from pydantic import BaseModel
from src.models.userModel import UserModel
from src.models.resourcesModel import ResourceModel


class PlayerInfoModel(BaseModel):
    user: UserModel
    own_resources: List[ResourceModel]
    game_resources: List[ResourceModel]

