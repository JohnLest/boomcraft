from typing import List
from pydantic import BaseModel
from src.models.userModel import UserModel


class ResourceModel(BaseModel):
    id_res: int
    type: str
    resource: str
    quantity: int
