from http import HTTPStatus

from flask import request
from flask_restful import Resource

from models import Recipe as RecipeModel
from models import Comment as CommentModel


class Comment(Resource):
    path = "/comment"

    @classmethod
    def post(cls):
        content = request.json["content"]
        recipe_id = request.json["recipe_id"]

        recipe = RecipeModel.get_by_id(recipe_id)
        if not recipe:
            return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND
        
        comment = CommentModel(content=content, recipe_id=recipe_id)
        comment.save()

        return comment.json(), HTTPStatus.CREATED
