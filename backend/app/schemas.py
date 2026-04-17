from app import ma
from app.models import User, Task

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password_hash",)

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_fk = True
        load_instance = True

# THESE are the variables tasks.py is trying to import!
user_schema = UserSchema()
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)