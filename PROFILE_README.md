# Van Schulist

> **Building low-latency agent infrastructure, Model Context Protocol gateways, and zero-dependency developer tools. Founder of [Existential Cloud](https://www.existentialcloud.ccwu.cc).**

[![Official Portal](https://img.shields.io/badge/Portal-existentialcloud.ccwu.cc-10b981?style=flat-square)](https://www.existentialcloud.ccwu.cc)
[![Live Simulator](https://img.shields.io/badge/Simulator-GitHub%20Pages-10b981?style=flat-square)](https://vanschulist.github.io/existentialcloud-portal/)
[![Flagship: mcp-mesh](https://img.shields.io/badge/Flagship-mcp--mesh%20v1.3.0-0ea5e9?style=flat-square)](https://github.com/VanSchulist/mcp-mesh)
[![Architecture: Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-zinc?style=flat-square)](https://github.com/VanSchulist/mcp-mesh#architecture)
[![Test Suite: 100% Pass](https://img.shields.io/badge/Tests-161%2F161%20Passed-10b981?style=flat-square)](https://github.com/VanSchulist/mcp-mesh/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](https://opensource.org/licenses/MIT)

---

## 💡 About Me & Existential Cloud

I'm an American undergraduate computer science student and indie builder. I build pragmatic open-source software designed to eliminate algorithmic friction, prompt bloat, and bureaucratic gatekeeping.

Modern coding agents are bottlenecked by context bloat: connecting 10 Model Context Protocol (MCP) servers statically dumps 30,000+ tokens of heavy JSON schemas into every prompt before you type a word. At **Existential Cloud**, I engineer zero-dependency developer tools that treat LLM attention windows and local machine resources with absolute discipline.

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      Heterogeneous AI Clients / IDEs                    │
 │               Claude Desktop  │  Cursor  │  Google Antigravity         │
 └───────────────────────────────────┬────────────────────────────────────┘
                                     │ stdio (JSON-RPC 2.0)
                                     │ Only 4 Meta-Tools Exposed (527 tokens, 94.6% reduction)
                                     ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │                   mcp-mesh v1.3.0 Federation Gateway                   │
 │  ┌──────────────────────────────────────────────────────────────────┐  │
 │  │        Federation Manager (Auto-discovery, Loop Prevention)       │  │
 │  ├──────────────────────────────────────────────────────────────────┤  │
 │  │      Tool Indexer, BM25 Scoring & Predictive Pre-Warmer          │  │
 │  ├──────────────────────────────────────────────────────────────────┤  │
 │  │  Circuit Breakers, Telemetry Ledger & Transparent Process Router │  │
 │  └──────────────────────────────────────────────────────────────────┘  │
 └───────────────────────────────────┬────────────────────────────────────┘
                                     │ Concurrently supervised upstream stdio pipes
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
 ┌───────────────────────┐   ┌───────────────────────┐   ┌───────────────────────┐
 │ ghost-job-hunter MCP  │   │ Postgres MCP          │   │ Filesystem / Git MCP  │
 │ (Antigravity Config)  │   │ (Claude Config)       │   │ (Cursor Config)       │
 └───────────────────────┘   └───────────────────────┘   └───────────────────────┘
```

---

## ⚡ 1-Minute Developer Quickstart

Federate all your local MCP servers across Claude Desktop, Cursor, and Google Antigravity into a single master connection with zero installation:

```bash
# Start universal heterogeneous federation gateway
uvx mcp-mesh run --federate

# Test natural language tool search across all workstation servers
uvx mcp-mesh search "ghost job audit" --federate

# View persistent SQLite token economy ledger
uvx mcp-mesh stats --db
```

---

## 📦 Open Source Portfolio (1 + 3 + N Architecture)

| Project | Role | Description | Stack & Status |
| :--- | :--- | :--- | :--- |
| [**`mcp-mesh`**](https://github.com/VanSchulist/mcp-mesh) | **FLAGSHIP** | Universal Heterogeneous MCP Reverse Proxy & Federation Gateway. Slashes Turn-0 prompt bloat by 85–95%, auto-discovers client configs, pre-warms target processes, and persists SQLite telemetry. | `Python 3.10+ Stdlib` • **v1.3.0** |
| [**`mcp-mesh-ui`**](https://github.com/VanSchulist/mcp-mesh-ui) | **OBSERVABILITY** | Real-time topology visualizer & telemetry dashboard for `mcp-mesh`. Features dark-mode local Web SPA (port 8765, SSE live stream), ANSI terminal TUI, and JSON-RPC inspection drawer. | `Vanilla JS / Web SPA` • **v1.3.0** |
| [**`mcp-registry-cli`**](https://github.com/VanSchulist/mcp-registry-cli) | **PACKAGE MGR** | Zero-config community package manager & synchronizer for MCP servers across Google Antigravity, Claude Desktop, and Cursor. | `Python CLI` • **v1.1.0** |
| [**`mcp-mesh-eval`**](https://github.com/VanSchulist/mcp-mesh-eval) | **BENCHMARK** | Frontier benchmark harness evaluating tool selection accuracy, TTFT latency, and Turn-0 token savings across 60 enterprise tools. | `Python Benchmark` • **v1.0.0** |
| [**`ghost-job-hunter`**](https://github.com/VanSchulist/ghost-job-hunter) | **TACTICAL AGENT** | Autonomous anti-ghost job hunting agent. Features 5 heuristic scoring engines, multi-source live scraping (Hacker News, RemoteOK, WWR), SQLite application ledger, and 1-click email outreach. | `Python / SQLite / MCP` • **v2.1.0** |
| [**`career-reboot-armor`**](https://github.com/VanSchulist/career-reboot-armor) | **TACTICAL MANUAL** | Publication-grade field manual and portfolio strategy guide for engineers re-entering the tech workforce after caregiving or medical gaps. | `Markdown / Generators` • **Phase 3** |
| [**`github-ai-studio`**](https://github.com/VanSchulist/github-ai-studio) | **GOVERNANCE** | Central engineering lab, Architectural Decision Records (ADRs), research tracker, and multi-agent ecosystem governance. | `Architecture Hub` • **Active** |

---

## 🛠️ Engineering Standards

* 🚀 **Zero External Dependencies**: All core libraries and CLI tools are engineered strictly with the Python standard library (`concurrent.futures`, `json`, `sqlite3`, `http.server`, `urllib`, `re`). Runs anywhere without `pip install` friction.
* 🧠 **Context-Window Economics**: AI agents should never be forced to parse 50 static schemas at Turn 0. Compact signatures and lazy on-demand resolution save dollars and eliminate tool hallucinations.
* 🛡️ **Defensive Reliability**: Automated circuit breakers, threaded watchdog timeouts, non-blocking JSON-RPC notification semantics, and 100% passing test suites across ecosystem (159/159 tests passing).

---

## 🌐 Links & Contact

* **Official Portal**: [www.existentialcloud.ccwu.cc](https://www.existentialcloud.ccwu.cc)
* **GitHub Organizations & Repos**: [@VanSchulist](https://github.com/VanSchulist)
* **License**: All public software released under the [MIT License](https://opensource.org/licenses/MIT).

---
*Crafted with 🖤 by Van Schulist | Existential Cloud AI Studio*
