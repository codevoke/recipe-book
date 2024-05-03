from __future__ import annotations

from .db import db, BaseModel
from .comment import Comment


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
            "comments": [comment.json() for comment in self.get_comments()]
        }
    
    @classmethod
    def get_by_id(cls, id: int) -> Recipe:
        return cls.query.get(id)
    
    @classmethod
    def get_all(cls) -> list[Recipe]:
        return cls.query.all()
    
    def get_comments(self) -> list[Comment]:
        return Comment.get_by_recipe_id(self.id)
