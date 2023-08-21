from uuid import uuid4
from sqlalchemy import UUID, func, true
from app.extensions import db, bcrypt
from app.base_model import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    age = db.Column(db.Integer)
    active = db.Column(db.Boolean, server_default=true())
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.utc_timestamp())
    bio = db.Column(db.Text)

    _hidden_fields = [
        "password",
    ]
    
    _default_fields = [
        "firstname",
        "lastname",
        "email",
        "age",
        "bio"
    ]
    
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return f'<User {self.id} {self.firstname} {self.lastname}>'
    
    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password)