# from mcp.server.fastmcp import FastMCP

# mcp = FastMCP('Weather')

# @mcp.tool(name = 'get_weather', description='Gets weather information for a Location')
# async def get_weather(location:str)->str:
#     """
#     Gets weather information for a given location

#     Args:
#         location (str): Location to get weather information

#     Returns:
#         str: Weather information for location
#     """
#     return f"Weather in {location} is always Rainy!!"
from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str)->str:
    """Get the weather location."""
    return "It's always raining in California"

if __name__=="__main__":
    mcp.run(transport="streamable-http")
