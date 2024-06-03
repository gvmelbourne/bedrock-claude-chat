# app/routes/integrations.py

from fastapi import APIRouter, Request
from backend.app.usecases.bot import handle_bot_request

router = APIRouter()

@router.post("/jira")
async def jira_endpoint(request: Request):
    data = await request.json()
    return handle_bot_request('jira', data)

@router.post("/confluence")
async def confluence_endpoint(request: Request):
    data = await request.json()
    return handle_bot_request('confluence', data)

@router.post("/warehouse")
async def warehouse_endpoint(request: Request):
    data = await request.json()
    return handle_bot_request('warehouse', data)
