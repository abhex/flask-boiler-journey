from flask import jsonify, request
from flask_jwt_extended import create_access_token, current_user, jwt_required
from app.attribute_dict_helper import AttributeDict
from app.users import bp
from app.extensions import jwt
from app.users.service import UsersService

@bp.route('/')
def index():
  return "This is the users Blueprint"

@bp.route('/login', methods=['POST'])
def login():
  user = UsersService.find_by_email(request.json.get('email'))
  if not user or not user.check_password(request.json.get('password')):
    return jsonify({"error": "Wrong username or password", "status": 401}), 401
  access_token = create_access_token(identity=AttributeDict(user.to_dict()))
  return jsonify({"access_token": access_token})

@bp.route('/all')
def get_users():
  users = UsersService.get_users()
  return jsonify(users)

@bp.route('/register', methods=['POST'])
def insert():
  try:
    response = UsersService.register(request.json)
    return jsonify({"status": 200, "user": response})
  except Exception as e:
    return jsonify(error=e.__dict__), 500


@bp.route("/who-am-i", methods=["GET"])
@jwt_required()
def protected():
    return jsonify(
        id=current_user.id,
        firstname=current_user.firstname,
        lastname=current_user.lastname,
        email=current_user.email,
    )


@jwt.user_identity_loader
def user_identity_lookup(user):
    print("USER_IDENTITY_")
    print(user)
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UsersService.find_one_by_identity(identity)