import uuid
import pytest
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.activities_repository import ActivitiesRepository
from datetime import datetime, timedelta

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interação com o banco")
def teste_registry_activity():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    
    activity_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Visita ao Castelo de Osaka",
        "occurs_at": datetime.strptime("02-01-2024", "%d-%m-%Y"),
    }
    
    activities_repository.registry_activity(activity_infos)

@pytest.mark.skip(reason="Interação com o banco")
def  find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    
    activities = activities_repository.find_activities_from_trip(trip_id)
    print()
    print(activities)