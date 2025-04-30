from ..database import SessionLocal
from .. import crud

class MCPServer:
    def __init__(self):
        self.db = SessionLocal()
    
    def get_recommended_itineraries(self, duration_nights: int):
        """Return recommended itineraries for a given duration."""
        return crud.get_recommended_itineraries(self.db, duration_nights)
    
    def __del__(self):
        self.db.close()


mcp_server = MCPServer()