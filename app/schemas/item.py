from pydantic import BaseModel

# Schema for incoming data to update or create an item
class ItemCreate(BaseModel):
    name: str
    quantity: int

# Schema for the response when an item is queried
class ItemResponse(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:        
        # allows you to work with SQLAlchemy models directly.
        orm_mode = True