# -*- coding: utf-8 -*-
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx_helpers import set_cell_background, set_cell_margins
from make_english_book import add_heading_1, add_heading_2, add_callout

def build_en_chapter_4(doc):
    add_heading_1(doc, "Chapter 4: Crushing the 'Stale Skills' Bias — A 72-Hour Modern AI & Digital Toolchain Sprint")
    
    add_heading_2(doc, "1. The Problem: The 'Outdated Veteran' Stereotype")
    doc.add_paragraph(
        "Even when returners bypass the ATS and secure a live phone screen, they encounter an unspoken, pervasive hiring prejudice: "
        "the interviewer (often a millennial or Gen Z team lead 5 to 10 years younger than the candidate) harbors a subtle bias: "
        "'This person has been out of the workforce since 2022. Workplaces have completely transformed with generative AI, modern collaboration "
        "tools, and automated pipelines. They are probably stuck in the legacy past, slow to adapt, and will require hand-holding.'"
    )

    add_heading_2(doc, "2. Why It Happens: The Velocity Illusion of Corporate Toolchains")
    doc.add_paragraph(
        "Between 2023 and 2026, enterprise software underwent a rapid paradigm shift. Tools like Slack, Notion, Airtable, Linear, "
        "and generative AI platforms (ChatGPT Enterprise, Claude, Copilot) became standard corporate infrastructure. "
        "Current employees who use these platforms daily develop an inflated sense of technological exclusivity, believing that these workflows "
        "can only be acquired through continuous corporate immersion."
    )
    doc.add_paragraph(
        "Candidates stumble into this bias because they believe catching up requires months of technical retraining or a costly certificate. "
        "In reality, **modern AI and digital tools are designed for natural-language, no-code interaction**. A seasoned professional with 10+ years "
        "of foundational business judgment can master high-impact AI workflows in 72 hours—and articulate them with far more commercial maturity "
        "than a junior employee using AI for basic email drafts."
    )

    add_heading_2(doc, "3. Common Mistakes: Museum-Piece Phrasing vs. Vague AI Hype")
    doc.add_paragraph("Returners typically signal technical obsolescence through two verbal mistakes:")
    doc.add_paragraph("• Relic Phrasing: Listing 'Proficient in Microsoft Word, Excel, PowerPoint, Outlook, and Internet Research' under skills. In modern hiring, advertising basic word processing is like a driver bragging that they know how to turn on windshield wipers—it immediately flags you as technologically dated.")
    doc.add_paragraph("• Unsubstantiated AI Buzzwords: Claiming 'Expert Prompt Engineer' or 'AI Enthusiast.' When a technical interviewer asks, 'Which model parameters or structured prompting frameworks do you leverage for document analysis?', the candidate stammers, proving their expertise is merely superficial.")

    add_heading_2(doc, "4. The Correct Approach: Tool-to-Workflow Binding")
    doc.add_paragraph(
        "To dismantle the 'stale skills' bias, apply the rule of **TOOL-TO-WORKFLOW BINDING**.\n"
        "Never mention a tool in isolation. Always pair the tool with a concrete business workflow and an efficiency outcome:\n"
        "[Tool Name] + [Specific Domain Task] + [Measurable Business Impact].\n"
        "You do not need to be a Python developer; you only need to show that you orchestrate modern digital tools to solve domain problems faster."
    )

    add_callout(
        doc,
        "THE BIAS REVERSAL LAW:\n"
        "Hiring managers fear that you will be a slow, high-maintenance hire.\n"
        "When you casually drop a phrase like: 'I regularly use Claude to run semantic diff comparisons across 60-page vendor contracts, "
        "which cuts our preliminary legal review cycle by 50%,' you instantly flip their perception. "
        "You cease to be an 'outdated returner' and emerge as a forward-leaning, high-leverage operator.",
        title="EXECUTIVE PERCEPTION PRINCIPLE"
    )

    add_heading_2(doc, "5. Step-by-Step Implementation: The 72-Hour Digital Re-tooling Sprint")
    doc.add_paragraph("Execute this disciplined three-day sprint to update your modern toolchain competency:")

    doc.add_paragraph("Day 1: Master Modern Collaborative Workspaces (Notion / Airtable)\n"
                  "Move past static spreadsheets. Open a free personal account on Notion or Airtable. Build a functional relational database (e.g., a candidate pipeline, vendor tracker, or project backlog). "
                  "Learn to create single-select tags, link records between tables, and configure one automated notification trigger (e.g., send a notification when status changes to 'Approved'). Time required: 3 hours.")

    doc.add_paragraph("Day 2: Build a Domain-Specific GenAI Workstream\n"
                  "Take a complex document from your past career (a financial audit, an operational SOP, a marketing brief). Open an advanced LLM (ChatGPT Plus, Claude 3.5 Sonnet). "
                  "Practice structured prompting using the 4-part framework: Role + Context + Task Constraints + Output Schema. "
                  "Prompt: 'Act as a Senior Compliance Officer. Review this 10-page policy document against current industry standards. Identify 3 ambiguous clauses, and output a 4-column Markdown table summarizing: Clause, Risk, Recommended Edit, and Justification.' Time required: 3 hours.")

    doc.add_paragraph("Day 3: Codify Your Modernized Value Narrative\n"
                  "Translate your weekend experiments into crisp bullet points for your resume and interview script. Store a clean PDF export of your database and AI audit on your laptop as a portfolio artifact ready for presentation.")

    add_heading_2(doc, "6. Concrete Example: Modernizing Four Functional Skillsets")
    
    # Skill Matrix Table
    table = doc.add_table(rows=5, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["Functional Track", "Outdated Legacy Phrasing (Rejected)", "Modernized High-Impact Phrasing (Selected)"]
    col_widths = [1.2, 2.3, 2.7]
    
    for i, title in enumerate(headers):
        cell = table.cell(0, i)
        cell.width = Inches(col_widths[i])
        set_cell_background(cell, "EDF2F7")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(title)
        run.font.bold = True
        run.font.size = Pt(9.5)
        run.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
        
    matrix_data = [
        ("Finance & Accounting", 
         "\"Proficient in Excel pivot tables, VLOOKUPs, and drafting monthly financial reports.\"", 
         "\"Build automated financial tracking models in modern relational databases; utilize structured LLM workflows for automated variance analysis and anomaly detection in raw ledger data.\""),
         
        ("HR & Talent Acquisition", 
         "\"Handled onboarding paperwork, organized employee files, and conducted phone screens.\"", 
         "\"Architected full-lifecycle onboarding workflows in Notion; leveraged AI-assisted role profiling to draft structured interview rubrics and eliminate candidate sourcing bottlenecks.\""),
         
        ("Marketing & Content", 
         "\"Wrote press releases, managed company blog, and posted on social media channels.\"", 
         "\"Orchestrate multi-channel content pipelines leveraging generative AI for rapid copy variation, SEO keyword clustering, and automated analytics dashboarding in Airtable.\""),
         
        ("Project Management / PM", 
         "\"Held weekly status meetings, updated Microsoft Project plans, and sent email updates.\"", 
         "\"Steer agile project cadences using Jira and digital Kanban boards; deploy automated webhook notifications and AI summary digests to identify critical-path dependencies.\"")
    ]
    
    for row_idx, data in enumerate(matrix_data, start=1):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, 80, 80, 100, 100)
            set_cell_background(cell, "FFFFFF" if row_idx % 2 == 1 else "F7FAFC")
            p = cell.paragraphs[0]
            run = p.add_run(text)
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0x2B, 0x6C, 0xB0) if col_idx == 2 else RGBColor(0x2D, 0x37, 0x48)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_heading_2(doc, "7. Practical Checklist: The Toolchain Modernity Audit")
    doc.add_paragraph("Before walking into an interview, verify:")
    doc.add_paragraph("[1] Stripped all references to 'Microsoft Office / Word / Basic Internet' from my resume.")
    doc.add_paragraph("[2] Comfortably understand the architecture of at least one modern workspace (Notion, Airtable, or modern Jira/Slack).")
    doc.add_paragraph("[3] Can articulate the 4 components of structured prompting (Role, Context, Constraints, Schema).")
    doc.add_paragraph("[4] Possess at least one tangible, de-identified artifact (a dashboard or analysis output) created with modern tools.")
    doc.add_paragraph("[5] Frame AI strictly as a productivity force-multiplier under human executive control, never as an unverified black box.")

    add_heading_2(doc, "8. Immediate Actionable Step")
    doc.add_paragraph(
        "IMMEDIATE ACTION TODAY: Log into Claude or ChatGPT. Paste in a challenging problem from your past career and run a structured prompt "
        "demanding a 3-part strategic breakdown. Spend 30 minutes studying how the AI handles the synthesis. "
        "You have officially crossed the digital divide."
    )
    
    doc.add_page_break()

print("EN Chapter 4 ready.")
