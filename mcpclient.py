from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    # Check if weather server is available
    weather_available = False
    try:
        import httpx
        async with httpx.AsyncClient() as client:
            # Try a simple GET request to check if server is running
            response = await client.get("http://localhost:8000/mcp", timeout=2.0)
            # If we get any response (even an error), the server is running
            weather_available = True
            print("✅ Weather server is available and will be used")
    except Exception as e:
        print("⚠️  Weather server is not available (not running or unreachable)")
    
    # Create client with available servers
    if weather_available:
        client = MultiServerMCPClient({
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        })
    else:
        client = MultiServerMCPClient({
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            }
        })

    import os
    groq_api_key = os.getenv("GROQ_API_KEY")
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key

    tools=await client.get_tools()
    model=ChatGroq(model="qwen/qwen3-32b", temperature=0)
    agent=create_react_agent(
        model,tools
    )

    # Test with a simple expression
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "evaluate this math experssion for me (2+4*5+2)/(3-1/2) ?"}]}
    )
    print("Math response:", math_response['messages'][-1].content)
    
    # Test with weather if available
    if weather_available:
        weather_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
        )
        print("Weather response:", weather_response['messages'][-1].content)
    else:
        print("Weather server not available - skipping weather test")

asyncio.run(main())
