from random import choice
from typing import Annotated
from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse

from ..bootstrap import templates
from ..services.home import Home as Home_Service
from ..config.settings import settings
from ..models.input_model import Texto as Texto_Model


router = APIRouter()

home_svc = Home_Service()

@router.get("/")
async def index(request: Request):
    """Index."""
    return templates.TemplateResponse(
        "pages/home.html",
        {
            "request": request,
            "slogan": choice(settings.SLOGANS),
            "audio": None
        }
    )

@router.post("/")
async def post_text(request: Request, body: Texto_Model):
    """Post Texto."""
    file_name = await home_svc.text_to_audio(body.texto)
    return {"file_name": file_name }
    
