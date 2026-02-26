from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="hello-server",
    stateless_http=True,
)

# If the module isn't found, use this direct attribute override 
# which works on older FastMCP versions to bypass host checks
try:
    from mcp.server.fastmcp.settings import TransportSecuritySettings
    mcp.settings.transport_security = TransportSecuritySettings(
        enable_dns_rebinding_protection=False
    )
except ImportError:
    # Fallback for older SDK versions
    if hasattr(mcp, "settings"):
        mcp.settings.host = "0.0.0.0"
