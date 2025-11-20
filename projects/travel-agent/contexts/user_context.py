from datetime import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class UserContext:  
    user_id: str
    preferred_airlines: List[str] = None
    hotel_amenities: List[str] = None
    budget_level: str = None
    session_start: datetime = None
    
    def __post_init__(self):
        if self.preferred_airlines is None:
            self.preferred_airlines = []
        if self.hotel_amenities is None:
            self.hotel_amenities = []
        if self.session_start is None:
            self.session_start = datetime.now()