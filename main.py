from agents import Agent , Runner, run 
from config import config


agent = Agent(
    name = 'Helpful Assistant',
    instructions='You are a Helpful Assistant.'
)
 
 
result = Runner.run_sync(
    agent,
    input = 'Hi, How are you ?',
    run_config=config
)    

print(result.final_output)