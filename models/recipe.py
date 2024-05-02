from __future__ import annotations

from .db import db, BaseModel


class Recipe(BaseModel):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String, nullable=True)

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image": self.image,
        }
    
    @classmethod
    def get_by_id(cls, id: int) -> Recipe:
        return cls.query.get(id)
    
    @classmethod
    def get_all(cls) -> list[Recipe]:
        return cls.query.all()
