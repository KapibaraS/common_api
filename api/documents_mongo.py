from datetime import datetime
from typing import Dict, Any
from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorDatabase


class Car:

    def __init__(
            self,
            collection: AsyncIOMotorDatabase,
            manufacturer: str = None,
            model: str = None,
            year_production: str = None,
            color: str = None,
            vin_code: str = None,
            _id: str = None,
            created_at: datetime = None,
            updated_at: datetime = None,

    ) -> None:
        self.__collection = collection
        self.manufacturer = manufacturer
        self.model = model
        self.year_production = year_production
        self.color = color
        self.vin_code = vin_code
        self._id = _id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    async def load(
            cls,
            db: AsyncIOMotorDatabase,
            _id: str = None,
            manufacturer: str = None,
            model: str = None,
            year_production: str = None,
            color: str = None,
            vin_code: str = None,
            fields: Dict = None,
    ):
        filters = {}

        doc = await db.cars.find_one(filters, fields)
        if not doc:
            return
        return cls(collection=db, **doc)

    async def create(self) -> None:
        self._id = self._id or uuid4().hex
        now = datetime.utcnow()
        self.created_at = now
        self.updated_at = now
        await self.__collection.insert_one(self.to_dict())

    def to_dict(self) -> Dict[str, Any]:
        return {
            '_id': self._id,
            'manufacturer': self.manufacturer,
            'model': self.model,
            'year_production': self.year_production,
            'color': self.color,
            'vin_code': self.vin_code,
        }
