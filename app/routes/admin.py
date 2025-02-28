from fastapi import APIRouter, Request

from ..bootstrap import templates
from ..models.input_model import Login as Login_Model
from ..models.models import Convesoes as Conversoes_Model
from ..services.auth import Auth as Auth_Service

auth_svc = Auth_Service()

router = APIRouter(
    prefix="/admin"
)


@router.get("")
@router.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse(
        "pages/login.html",
        {
            "request": request,
        }
    )

@router.post("/login")
async def post_login(request: Request, login: Login_Model):
    return await auth_svc.login(login.usuario, login.senha)

@router.get("/conversoes")
@auth_svc.is_auth()
async def get_conversoes(request: Request):
    conversoes = await Conversoes_Model.all().order_by("created_at", "ip")
    print(conversoes)
    return templates.TemplateResponse(
        "pages/conversoes.html",
        {
            "request": request,
            "conversoes": conversoes
        }
    )