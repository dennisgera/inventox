from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()


# Route to update inventory
@router.post("/update_inventory/", response_model=schemas.ItemResponse)
def update_inventory(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    # Check if item already exists
    existing_item = db.query(models.Item).filter(models.Item.name == item.name).first()

    if existing_item:
        existing_item.quantity = item.quantity
    else:
        # Create new item
        new_item = models.Item(name=item.name, quantity=item.quantity)
        db.add(new_item)

    db.commit()
    db.refresh(existing_item or new_item)

    return existing_item or new_item


# Route to query current inventory
@router.get("/inventory/", response_model=list[schemas.ItemResponse])
def get_inventory(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items
