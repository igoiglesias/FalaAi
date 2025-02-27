import os
from tortoise import Tortoise, run_async
from ..config.settings import settings

async def init_db():
    """
    Inicializa o banco de dados, configurando o Tortoise-ORM com os modelos definidos.
    """
    models_dir = "app/models"
    modules = [
        f"app.models.{filename[:-3]}"  # Remove a extensão ".py"
        for filename in os.listdir(models_dir)
        if filename.endswith(".py") and filename != "__init__.py"
    ]
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": modules},
        _create_db=True,
    )
    await Tortoise.generate_schemas()
    print("Database initialized.")

async def close_db():
    """
    Encerra todas as conexões do banco de dados.
    """
    await Tortoise.close_connections()
    print("Database connections closed.")


if __name__ == "__main__":
    async def run():
        await init_db()
        print("Database is ready.")
        await close_db()

    run_async(run())
