import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from .link_to_invite_repository import LinkToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco")
def teste_registry_link():
    conn = db_connection_handler.get_connection()
    link_to_invite_repository = LinkToInviteRepository(conn)
    
    link_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "https://www.youtube.com/",
        "title": "Compre o ingresso pro circo"
    }
    
    link_to_invite_repository.registry_link(link_infos)
    
@pytest.mark.skip(reason="Interação com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_to_invite_repository = LinkToInviteRepository(conn)
    
    links = link_to_invite_repository.find_links_from_trip(trip_id)
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
    print()
    print(links)