from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="hello-server",
    stateless_http=True,
    allowed_hosts=["hamzah-syed-mcp-learning-p1.hf.space", "localhost", "0.0.0.0"],
)

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

mcp_app = mcp.streamable_http_app()