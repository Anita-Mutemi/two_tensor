from pydantic import BaseModel  # type: ignore


class BooleanModel(BaseModel):
    enable_echo: bool
