from sqlite3 import Connection
from typing import Dict, List, Tuple

class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def registry_participant(self, participant_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO participants
                    (id, trip_id, emails_to_invite_id, name)
                VALUES 
                    (?, ?, ?, ?)
            ''', (
                participant_infos["id"],
                participant_infos["trip_id"],
                participant_infos["emails_to_invite_id"],
                participant_infos["name"],
            )
        )
        self.__conn.commit()
        
    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            #Seleciona o ID , nome e is_confirmed da tabela de participantes e o email da tabela emails, porém, vai selecionar apenas os participantes onde o ID do email (na tabela Email) for igual ao ID do email_to_invite_id (que está presente na tabela Participants) , tudo isso de uma determinada Viagem (WHERE p.trip_id )
            '''
                SELECT p.id, p.name, p.is_confirmed, e.email
                from participants as p
                JOIN emails as e ON e.id = p.email_to_invite_id
                WHERE p.trip_id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        return participants
    
    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE participants
                    SET is_confirmed = 1
                WHERE 
                    id = ?
            ''', (participant_id,)
        )
        self.__conn.commit()