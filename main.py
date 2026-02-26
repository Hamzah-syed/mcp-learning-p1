from mcp.server.fastmcp import FastMCP
from starlette.middleware.trustedhost import TrustedHostMiddleware

mcp = FastMCP(name="hello-server", stateless_http=True)

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

mcp_app = mcp.streamable_http_app()

# Remove host restriction — allow all hosts (needed for HF Spaces)
mcp_app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)