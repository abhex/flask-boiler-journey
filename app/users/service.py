from typing import Dict
from app.users.model import User
from app.extensions import db


class UsersService:
  
  def register(usersInput: Dict[str, str]) -> Dict[str, str]:
    first_name = usersInput.get('firstName')
    last_name = usersInput.get('lastName')
    email = usersInput.get('email')
    password = usersInput.get('password')

    me = User(firstname=first_name, lastname=last_name, email=email, password=password)
    db.session.add(me)
    db.session.commit()
    return User.query.get(me.id).to_dict()
  
  
  def get_users():
    return [[user.to_dict() for user in User.query.all()]]


  def find_by_email(email: str):
    return User.query.filter_by(email=email).one_or_none()
  
  def find_one_by_identity(identity):
    return User.query.filter_by(id=identity).one_or_none()
 