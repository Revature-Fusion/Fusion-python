from flask import request, jsonify

from exceptions.resource_not_found import ResourceNotFound
from models.users_model import Users
from models.login_model import Login
from repositories.users_repo_impl import UsersRepoImpl
from repositories.login_repo_impl import LoginRepoImpl
from services.users_service import UsersService
from services.login_service import LoginService

ur = UsersRepoImpl()
us = UsersService(ur)

lr = LoginRepoImpl()
ls = LoginService(lr)


def route(app):

    @app.route("/login", methods=["POST"])
    def user_login():
        try:
            login = Login.json_parse(request.json)
            u_login = ls.login(login)
            return jsonify(u_login), 200
        except TypeError:
            return "credentials are incorrect, please try again", 404

    @app.route("/users", methods=["POST"])
    def register_user():
        body = request.json

        user = Users(email=body["email"], first_name=body["firstName"], last_name=body["lastName"], role=body["role"])
        user = us.create_user(user)
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
        user = Users(u_id=int(u_id), email=body["email"], first_name=body["firstName"], last_name=body["lastName"],
                     role=body["role"])
        user = us.update_user(user)

        if isinstance(user, str):
            return user, 404
        else:
            return user.json()

    @app.route("/users/<u_id>", methods=["DELETE"])
    def delete_user(u_id):
        us.delete_user(u_id)
        return '', 204
