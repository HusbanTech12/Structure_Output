from agents import Agent , Runner, function_tool;
from config import config;
from pydantic import BaseModel;


class WeatherStructure(BaseModel):
    Location : str
    Weather : str
    Temperature : float 



@function_tool
def fetch_weather(location : str) -> str:
    """
      Fetch Weather the given location.  
    """
    return 'The Weather in {location} is Sunny with a temperature at 25°C'   
    
    
    
agent = Agent(
    name = 'Helpful Assistant',
    instructions='You are a Helpful Assistant.',
    tools = [fetch_weather],
    output_type= WeatherStructure
)
 
 
result = Runner.run_sync(
    agent,
    input = 'What is the weather in karachi ?',
    run_config=config
)    
# print(agent.as_tool)
print(result.final_output)  