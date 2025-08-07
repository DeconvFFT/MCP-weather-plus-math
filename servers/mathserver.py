from mcp.server.fastmcp import FastMCP
from typing_extensions import Union

mcp = FastMCP('Math')

@mcp.tool(name='add', description='Add two numbers')
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers

    Args:
        a (int/float): number 1
        b (int/float): number 2

    Returns:
        int/float: Addition of two numbers
    """
    return a+b

@mcp.tool(name='subtract', description='Subtract two numbers')
def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts two numbers

    Args:
        a (int/float): number 1
        b (int/float): number 2

    Returns:
        int/float: Subtraction of two numbers
    """
    return a-b

@mcp.tool(name='multiply', description='Multiply two numbers')
def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers

    Args:
        a (int/float): number 1
        b (int/float): number 2

    Returns:
        int/float: Multiplication of two numbers
    """
    return a*b

@mcp.tool(name='divide', description='Divide two numbers')
def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Divides two numbers

    Args:
        a (int/float): number 1
        b (int/float): number 2
    """
    return a/b if b!=0 else 0.0

    
# if __name__ == '__main__':
#     mcp.run(transport='stdio') # when transport = stdio: Accepts input from stdin (results in terminal)
   
# from mcp.server.fastmcp import FastMCP

# mcp=FastMCP("Math")

# @mcp.tool()
# def add(a:int,b:int)->int:
#     """_summary_
#     Add to numbers
#     """
#     return a+b

# @mcp.tool()
# def multiple(a:int,b:int)-> int:
#     """Multiply two numbers"""
#     return a*b

#The transport="stdio" argument tells the server to:

#Use standard input/output (stdin and stdout) to receive and respond to tool function calls.

if __name__=="__main__":
    mcp.run(transport="stdio") 