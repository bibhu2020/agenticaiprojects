from agents import Agent, RunContextWrapper, Runner, function_tool, ModelSettings, InputGuardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
from contexts.user_context import UserContext
from tools.weather import get_weather_forecast
from aagents.flight_agent import flight_agent
from aagents.hotel_agent import hotel_agent
from aagents.conversational_agent import conversational_agent
from aagents.budget_guardrail_agent import budget_guardrail
from output_types.travel_plan import TravelPlan

travel_agent = Agent[UserContext](
    name="Travel Planner",
    instructions="""
    You are a travel planning assistant who helps users plan their trips.
    
    You can provide personalized travel recommendations based on the user's destination, duration, budget, and preferences.
    
    The user's preferences are available in the context, which you can use to tailor your recommendations.
    
    You can:
    1. Get weather forecasts for destinations
    2. Hand off to specialized agents for flight and hotel recommendations
    3. Create comprehensive travel plans with activities and notes
    
    Always be helpful, informative, and enthusiastic about travel.
    """,
    model="gpt-4o-mini",
    tools=[get_weather_forecast],
    handoffs=[flight_agent, hotel_agent, conversational_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=budget_guardrail),
    ],
    output_type=TravelPlan
)