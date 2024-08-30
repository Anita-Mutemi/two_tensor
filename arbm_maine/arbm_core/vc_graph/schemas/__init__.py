import abc

from bson import ObjectId  # type: ignore
from pydantic import BaseModel  # type: ignore


class PyMongoBase(BaseModel, abc.ABC):
    class Config:
        # The ObjectIdField creates an bson ObjectId value, so its necessary to setup the json encoding
        json_encoders = {ObjectId: str}
