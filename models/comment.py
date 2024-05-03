from __future__ import annotations
from .db import db, BaseModel


class Comment(BaseModel):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"))

    def json(self):
        return {
            "id": self.id,
            "content": self.content,
            "recipe_id": self.recipe_id
        }

    @classmethod
    def get_by_id(cls, id: int) -> Comment:
        return cls.query.get(id)
    
    @classmethod
    def get_by_recipe_id(cls, recipe_id: int) -> list[Comment]:
        return cls.query.filter_by(recipe_id=recipe_id)
