from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with enhanced metadata for 2025-06-18 spec
mcp = FastMCP(
    name="hello-server",
    stateless_http=True # When true we don't need handshake or initialize things.
)

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

mcp_app = mcp.streamable_http_app()