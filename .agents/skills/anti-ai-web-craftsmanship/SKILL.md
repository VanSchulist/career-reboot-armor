---
name: anti-ai-web-craftsmanship
description: Principles, design tokens, and frontend architecture for creating human-engineered developer tools and dashboards without stereotypical "AI-generated" aesthetics (neon gradients, generic buzzwords, washed-out glassmorphism, or empty cards).
---

# Anti-AI Web Craftsmanship & Human-Engineered Interface Guidelines

Use this skill when designing, building, or refactoring landing pages, developer portals, and telemetry dashboards. It enforces the design principles of premier developer tools (Linear, Vercel, Fly.io, Astral/uv, GitHub, Stripe, Supabase).

---

## 1. Eradicate "AI-Generated" Clichés

| ❌ AI Cliché / Trope | Why It Feels "AI-Generated" | ✅ Human-Engineered Standard |
| :--- | :--- | :--- |
| **Saturated Neon Gradients** (`from-purple-600 via-pink-600 to-amber-500` text) | Overused by generative models to mimic "futuristic AI". | **Crisp White Headings** (`text-zinc-100` / `#ffffff`) with subtle, muted secondary text (`text-zinc-400`). Single purposeful accent (emerald, sky, amber) used only on interactive elements or status badges. |
| **Washed-out Glassmorphism & Blurry Glows** (`backdrop-blur-md bg-white/5 shadow-[0_0_50px_rgba(...)]`) | Makes text hard to read and looks like an unstyled crypto template. | **Solid, Grounded Surfaces**: Dark zinc/slate surfaces (`#09090b` canvas, `#121316` cards, `#181a1f` hover) with crisp `1px` borders (`#27272a` or `rgba(255,255,255,0.08)`). |
| **Robotic Buzzword Headlines** ("Engineering the Agentic Substrate", "Empowering holistic multi-agent synergy") | Hollow marketing jargon that conveys zero actual functionality. | **Pragmatic, Direct Developer Copy**: "Cut Turn-0 Prompt Bloat by 90%." "Stop loading 50+ tool schemas into your agent prompt before the user types a word." |
| **Pinging Colored Dots & Toy Gimmicks** (`animate-ping bg-amber-400`) | Distracting visual noise masquerading as "liveliness". | **Clean Status Badges**: `● LIVE` pill with subtle opacity, or small mono indicators (`CONNECTED: 127.0.0.1:8765`). |
| **Floating Emojis in Headers** (`🕸️ Topology`, `📡 Servers`, `⚡ Waterfall`) | Low-effort visual placeholder typical of rapid prototype prompts. | **Subtle Geometric SVG Icons** or clean, well-spaced typography (`Topology Map`, `Upstream Sources`, `Invocation Stream`). |
| **Unformatted Jumping Numbers** | Numbers that wobble when updated because of proportional font widths. | **Tabular Monospace Numerics**: `font-variant-numeric: tabular-nums; font-family: ui-monospace, SFMono-Regular, monospace`. |

---

## 2. Core Visual Foundations

### Palette
* **Canvas**: `#09090b` (Neutral rich black)
* **Surface / Panels**: `#111215` (Deep charcoal zinc)
* **Raised / Cards**: `#16181d` (Subtle lift)
* **Borders**: `#22242a` (Crisp 1px boundary)
* **Dividers**: `rgba(255, 255, 255, 0.06)`
* **Text Primary**: `#f4f4f5` (Zinc 100)
* **Text Secondary**: `#a1a1aa` (Zinc 400)
* **Text Muted**: `#71717a` (Zinc 500)
* **Accents (Functional Only)**:
  * Healthy / Saved / Online: Emerald `#10b981` / `rgba(16, 185, 129, 0.15)`
  * Cache Hit / Info: Sky `#0ea5e9` / `rgba(14, 165, 233, 0.15)`
  * Warning / Processing: Amber `#f59e0b` / `rgba(245, 158, 11, 0.15)`
  * Error / Tripped: Rose `#f43f5e` / `rgba(244, 63, 94, 0.15)`

### Typography & Spacing
* **Sans Font**: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif`
* **Mono Font**: `ui-monospace, "SF Mono", "Cascadia Code", "JetBrains Mono", Consolas, monospace`
* **Header Hierarchy**:
  * Display: `text-3xl` or `text-4xl`, `font-bold tracking-tight`
  * Section: `text-lg` or `text-xl`, `font-semibold text-zinc-100`
  * Meta/Label: `text-xs font-mono uppercase tracking-wider text-zinc-400`
  * Body: `text-sm text-zinc-300 leading-relaxed`

---

## 3. Mandatory Interactive Details

1. **One-Click Terminal Snippets**: Every CLI or install instruction must feature a prominent copy button with instant visual feedback ("Copied!").
2. **Tabbed Client Switcher**: Let developers switch tabs between **Claude Desktop**, **Cursor**, and **Antigravity** to see actual JSON config snippets.
3. **Inspectable Event Ledger**: In observability dashboards, clicking any row in the invocation stream must reveal an inspection drawer or modal detailing the JSON-RPC request and response payloads.
4. **Active Controls**: Include live pause/play toggles, rate selectors, search filters, and manual traffic trigger buttons.
