from tortoise.models import Model
from tortoise import fields

class Convesoes(Model):
    """Modelo para armazenar informações sobre conversoes."""
    id = fields.IntField(pk=True)
    texto = fields.CharField(max_length=1000)
    audio = fields.CharField(max_length=60)
    ip = fields.CharField(max_length=50)
    deteletado = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "conversoes"

class Usuarios(Model):
    """Modelo para armazenar informações sobre usuários."""
    id = fields.IntField(pk=True)
    nome = fields.CharField(max_length=200)
    usuario = fields.CharField(max_length=60, unique=True)
    senha = fields.CharField(max_length=60)
    deteletado = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "usuarios"