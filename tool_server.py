# tool_server.py
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI(title="Mock Ticket Tool", version="0.1")

class TicketReq(BaseModel):
    title: str
    category: str
    description: str
    contact: str

class TicketResp(BaseModel):
    ticket_id: str
    next_steps: str
    echo: TicketReq

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/create_ticket", response_model=TicketResp)
def create_ticket(req: TicketReq):
    tid = "T-" + uuid.uuid4().hex[:8].upper()
    return TicketResp(
        ticket_id=tid,
        next_steps=f"已创建工单 {tid}，IT 将在 2 个工作日内联系 {req.contact}。",
        echo=req
    )