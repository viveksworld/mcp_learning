from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel
import json


mcp = FastMCP("Joke-Generator-MCP",  host="0.0.0.0", port=8081)

class JokeCategory(BaseModel):
    category: str

@mcp.tool()
async def get_joke(category: str, ctx: Context):
    """
    This function returns a joke from a given category.
    """
    if category == "dad":
        return json.dumps({"joke": "Why don't scientists trust atoms? Because they make up everything!"})
    elif category == "tech":
        return json.dumps({"joke": "Why did the computer go to the doctor? Because it had a virus!"})
    else:
        print("Checkpoint - Categroy not found")
        result = await ctx.elicit(
            "I don't have jokes for that category. Please choose 'dad' or 'tech'.",
            JokeCategory,
        )
        if result.action == "accept" and result.data:
            # We recursively call get_joke with the new category from the user
            return await get_joke(result.data.category, ctx)
        else:
            # The user declined or cancelled the elicitation
            return json.dumps({"joke": "Okay, no joke for you then."})


def main():
    print("Starting MCP server with elicitation...")
    mcp.run(transport="sse")


if __name__ == "__main__":
    main()
