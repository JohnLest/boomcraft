from pydantic import BaseModel


class ResourceModel(BaseModel):
    id_res: int
    type: str
    resource: str
    quantity: int

