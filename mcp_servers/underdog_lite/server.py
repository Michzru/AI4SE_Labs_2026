"""Minimal local MCP server inspired by the UNDERDOG kayak coach connector.

Exposes a single tool that turns a K1 500 m race time into pace metrics.
Runs over stdio; registered for Claude Code in the repo-root .mcp.json.
"""

from mcp.server.mcpserver import MCPServer

RACE_DISTANCE_M = 500

mcp = MCPServer(
    "underdog-lite",
    instructions="Kayak K1 500 m helper. Use k1_500_pace to compute pace from a race time.",
)


def _parse_time(time: str) -> float:
    """Parse 'M:SS.s' or 'SS.s' into seconds."""
    if ":" in time:
        minutes, seconds = time.split(":", 1)
        return int(minutes) * 60 + float(seconds)
    return float(time)


@mcp.tool()
def k1_500_pace(time: str) -> dict:
    """Compute pace metrics for a K1 500 m time.

    Args:
        time: Race time as 'M:SS.s' (e.g. '1:52.4') or seconds (e.g. '112.4').
    """
    total_s = _parse_time(time)
    if total_s <= 0:
        raise ValueError("time must be positive")
    return {
        "time_s": round(total_s, 2),
        "avg_speed_kmh": round(RACE_DISTANCE_M / total_s * 3.6, 2),
        "avg_speed_ms": round(RACE_DISTANCE_M / total_s, 2),
        "split_per_100m_s": round(total_s / 5, 2),
        "split_per_250m_s": round(total_s / 2, 2),
    }


if __name__ == "__main__":
    mcp.run()
