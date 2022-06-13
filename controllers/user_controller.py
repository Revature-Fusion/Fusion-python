from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.user_model import User
from repositories.user_repo_impl import UserRepoImpl
from services.user_service import UserService


ur = UserRepoImpl()
us = UserService(ur)


def route(app):

    @app.route("/login", methods=["POST"])
    def user_login():
        try:
            login = User.json_parse(request.json)
            u_login = us.login(login)
            return jsonify(u_login), 200
        except TypeError:
            return "credentials are incorrect, please try again", 404

    @app.route("/users", methods=["POST"])
    def register_user():
        body = request.json

        user = User(email=body["email"], first_name=body["firstName"], last_name=body["lastName"], username=body["username"], password=body["password"], role=body["role"])
        user = us.create_user(user)
        return user.json(), 200

    @app.route("/users/guest", methods=["POST"])
    def register_guest():
        body = request.json

        user = User(email=body["email"], first_name=body["firstName"], last_name=body["lastName"])
        user = us.create_guest(user)
        return user.json(), 200

    @app.route("/users/<u_id>", methods=["GET"])
    def get_user(u_id):
        try:
            return us.get_user(int(u_id)).json(), 200
        except ValueError as e:
            return "Not a Valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/users", methods=["GET"])
    def get_all_users():
        return jsonify([users.json() for users in us.get_all_users()]), 200

    @app.route("/users/<u_id>", methods=["PUT"])
    def update_user(u_id):
        body = request.json
        user = User(u_id=int(u_id), email=body["email"], first_name=body["firstName"], last_name=body["lastName"],
                    username=body["username"], password=body["password"], role=body["role"])
        user = us.update_user(user)

        if isinstance(user, str):
            return user, 404
        else:
            return user.json()

    @app.route("/users/<u_id>", methods=["DELETE"])
    def delete_user(u_id):
        us.delete_user(u_id)
        return '', 204
