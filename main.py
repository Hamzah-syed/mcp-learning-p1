from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.settings import TransportSecuritySettings # Add this import

mcp = FastMCP(
    name="hello-server",
    stateless_http=True,
)

# Fix: Explicitly disable DNS rebinding protection for proxy environments
mcp.settings.transport_security = TransportSecuritySettings(
    enable_dns_rebinding_protection=False
)

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

mcp_app = mcp.streamable_http_app()
