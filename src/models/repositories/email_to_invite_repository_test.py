import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .email_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco")
def teste_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    emails_trips_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "olamundo@gmail.com"
    }
    
    emails_to_invite_repository.registry_email(emails_trips_infos)

@pytest.mark.skip(reason="Interação com o banco")
def test_find_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)
    
    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)