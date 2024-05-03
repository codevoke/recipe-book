import os
import base64
from http import HTTPStatus
from flask import request
from flask_restful import Resource

from models import Recipe as RecipeModel


class Recipe(Resource):
    path = "/recipe"

    @classmethod
    def get(cls) -> tuple[dict[str, str], HTTPStatus]:
        _id = request.args.get("id")

        if _id is None:
            return {"message": "id is required"}, HTTPStatus.BAD_REQUEST
        else:
            recipe = RecipeModel.get_by_id(_id)
            if recipe is None:
                return {"message": "recipe not found"}, HTTPStatus.NOT_FOUND

            return recipe.json(), HTTPStatus.OK

    @classmethod
    def post(cls):
        title = request.json["title"]
        description = request.json["description"]
        image = request.json["image"]

        recipe = RecipeModel(title=title, description=description)
        recipe.save()

        if image is not None:
            base64_image = base64.b64decode(image)

            filename = f"{recipe.id}.jpg"
            file = open("static/images/" + filename, "w")
            file.write(" ")
            file.close()

            with open(f"static/images/{recipe.id}.jpg", "wb") as f:
                f.write(base64_image)
            recipe.image = f"static/images/{recipe.id}.jpg"

            recipe.save()

        return recipe.json(), HTTPStatus.CREATED


class RecipeList(Resource):
    path = "/recipe/list"

    @classmethod
    def get(cls):
        recipes = RecipeModel.get_all()
        return [recipe.json() for recipe in recipes]
