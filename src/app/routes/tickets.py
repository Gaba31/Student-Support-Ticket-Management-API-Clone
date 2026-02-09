from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.schemas.ticket import TicketCreation,TicketUpdate
from app.utils.jwt_handler import decode_data
from app.utils.logger import logger

router = APIRouter()
security = HTTPBearer()

# Temporary in-memory storage
TICKETS = []
ticket_counter = 1

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = decode_data(token)
    return payload


@router.post("/create")
def create_ticket(ticket: TicketCreation,
    user=Depends(get_current_user),
):
    global ticket_counter
    global TICKETS
    new_ticket = {
        "id": ticket_counter,
        "title": ticket.title,
        "description": ticket.description,
        "priority":"medium",
        "status": "open",
        "created_by": user["user_id"]
    }

    TICKETS.append(new_ticket)
    logger.info(f"Ticket created | ticket_id={ticket_counter}")
    ticket_counter += 1

    return {
        "success": True,
        "data": new_ticket,
        "message": "Ticket created successfully",
    }


@router.get("/all")
def get_all_ticket(user = Depends(get_current_user)):
    global TICKETS
    role = user['role']
    ticket_list = []

    if role == "student":
        for t in TICKETS:
            if t['created_by'] == user['user_id']:
                ticket_list.append(t)

    if role == "admin":
        ticket_list = TICKETS

    return ticket_list


@router.get("/{ticket_id}")
def get_ticket_by_id(ticket_id:int,user=Depends(get_current_user)):
    global TICKETS
    role = user['role']

    if role == "student":
        for t in TICKETS:
            if t["id"] == ticket_id and t['created_by'] == user['user_id']:
                return t

    if role == 'admin':
        for t in TICKETS:
            if t["id"] == ticket_id:
                return t

    return {
        "Success":False,
        "message":"Ticket not found!"
    }


def fetch_ticket_by_id(ticket_id):
    global TICKETS
    for ticket in TICKETS:
        if ticket["id"] == ticket_id:
            return ticket


@router.post("/update/{ticket_id}")
def update_ticket_by_admin(*,ticket_id : int, user = Depends(get_current_user),data:TicketUpdate):
    role = user['role']
    if role == 'admin':
        ticket = fetch_ticket_by_id(ticket_id)
        ticket["priority"] = data.priority
        ticket["status"] = data.priority


        return ticket

