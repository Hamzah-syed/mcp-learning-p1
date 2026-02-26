from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="hello-server",
    stateless_http=True,
)

# Fix for HF Spaces — disable host header validation
mcp.settings.host = "0.0.0.0"

# Patch the allowed hosts directly on the settings
if hasattr(mcp.settings, 'allowed_hosts'):
    mcp.settings.allowed_hosts = ["*"]

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

mcp_app = mcp.streamable_http_app()