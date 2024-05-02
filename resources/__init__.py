from flask_restful import Api

from .recipe import Recipe, RecipeList


api = Api(prefix="/api")

api.add_resource(Recipe, Recipe.path)
api.add_resource(RecipeList, RecipeList.path)


def init_app(app):
    api.init_app(app)
