from tortoise.models import Model
from tortoise import fields

class User(Model):
    """Modelo para armazenar informações sobre usuários."""
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=255)
    name = fields.CharField(max_length=100)
    document = fields.CharField(max_length=20, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"