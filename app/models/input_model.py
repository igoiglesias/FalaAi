

from typing import Annotated
from pydantic import BaseModel, Field


class Texto(BaseModel):
    
    texto: Annotated[str, Field(max_length=1000)]