from agents import function_tool, RunContextWrapper
from contexts.user_context import UserContext
import json

@function_tool
async def search_flights(wrapper: RunContextWrapper[UserContext], origin: str, destination: str, date: str) -> str:
    """Search for flights between two cities on a specific date, taking user preferences into account."""
    # In a real implementation, this would call a flight search API
    flight_options = [
        {
            "airline": "SkyWays",
            "departure_time": "08:00",
            "arrival_time": "10:30",
            "price": 350.00,
            "direct": True
        },
        {
            "airline": "OceanAir",
            "departure_time": "12:45",
            "arrival_time": "15:15",
            "price": 275.50,
            "direct": True
        },
        {
            "airline": "MountainJet",
            "departure_time": "16:30",
            "arrival_time": "21:45",
            "price": 225.75,
            "direct": False
        }
    ]
    
    # Apply user preferences if available
    if wrapper and wrapper.context:
        preferred_airlines = wrapper.context.preferred_airlines
        if preferred_airlines:
            # Move preferred airlines to the top of the list
            flight_options.sort(key=lambda x: x["airline"] not in preferred_airlines)
            
            # Add a note about preference matching
            for flight in flight_options:
                if flight["airline"] in preferred_airlines:
                    flight["preferred"] = True                      
    
    return json.dumps(flight_options)