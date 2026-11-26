# Task 7 – Lokálny MCP server

**Výsledok:** lokálny MCP server `underdog-lite` (Python, `mcp` SDK 2.3, stdio) s jedným nástrojom `k1_500_pace`. Je to zjednodušená obdoba môjho konektora UNDERDOG (tréner pre K1 500 m): z času na 500 m vypočíta rýchlosť a medzičasy.

## Súbory

| Súbor | Účel |
|---|---|
| [`mcp_servers/underdog_lite/server.py`](../../../mcp_servers/underdog_lite/server.py) | MCP server s nástrojom `k1_500_pace(time)` |
| [`mcp_servers/underdog_lite/requirements.txt`](../../../mcp_servers/underdog_lite/requirements.txt) | závislosť `mcp>=2.3,<3` |
| [`.mcp.json`](../../../.mcp.json) | registrácia servera pre Claude Code (projektový scope) |

Inštalácia (`.venv` je v gite ignorovaný):

```bash
cd mcp_servers/underdog_lite && uv venv .venv && uv pip install -p .venv/bin/python -r requirements.txt
```

## Overenie

Test cez MCP klienta (stdio, `initialize`, `list_tools`, `call_tool`):

```
tools: ['k1_500_pace']
call k1_500_pace(time="1:52.4") →
{"time_s": 112.4, "avg_speed_kmh": 16.01, "avg_speed_ms": 4.45,
 "split_per_100m_s": 22.48, "split_per_250m_s": 56.2}
```

Použitie v Claude Code:

- [mcp_connected.png](mcp_connected.png): `/mcp` ukazuje `underdog-lite` ako ✔ connected, 1 tool (Project MCPs z `.mcp.json`).
- [mcp_tool_call.png](mcp_tool_call.png): na otázku „Aké mám tempo, ak som šiel K1 500 m za 1:52,4?“ Claude zavolal `underdog-lite` a vrátil hodnoty z nástroja: 16,01 km/h, 22,48 s na 100 m, 56,2 s na 250 m.
- Pri prvom pokuse model nástroj nezavolal a tempo si vypočítal sám. Úloha bola na neho príliš jednoduchá. Nástroj zavolal až po opätovnom pripojení servera (Reconnected to underdog-lite).

Postup: projektový `.mcp.json` sa načíta pri štarte session a server treba raz schváliť. Potom stačí napr. prompt „Aké mám tempo, ak som šiel K1 500 m za 1:52,4?“. Claude zavolá `mcp__underdog-lite__k1_500_pace`.

## Poznámky

- V `mcp` 2.x bol `FastMCP` premenovaný na `MCPServer` (`mcp.server.mcpserver`). Kód písaný pre v1 bez úpravy padne.
- Server má len 1 nástroj, takže do kontextu pridáva minimum tokenov. To je v súlade s upozornením v zadaní, že príliš veľa nástrojov zhoršuje výkon.
