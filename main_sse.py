from mcp.server.fastmcp import FastMCP
import json


mcp = FastMCP("Joke-Generator-MCP")

@mcp.tool()
def get_joke(category: str):
    """
    This function returns a joke from a given category.
    """
    if category == "dad":
        return json.dumps({"joke": "Why don't scientists trust atoms? Because they make up everything!"})
    elif category == "tech":
        return json.dumps({"joke": "Why did the computer go to the doctor? Because it had a virus!"})
    else:
        return json.dumps({"joke": "I don't have any jokes for that category."})


def main():
    print("Starting MCP server...")
    mcp.run(transport="sse")


if __name__ == "__main__":
    main()
