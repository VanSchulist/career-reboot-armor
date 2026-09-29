# -*- coding: utf-8 -*-
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx_helpers import set_cell_background, set_cell_margins
from make_english_book import add_heading_1, add_heading_2, add_callout

def build_en_chapter_2(doc):
    add_heading_1(doc, "Chapter 2: The Consulting Umbrella — Ethically Bridging the Void with Verifiable Micro-Engagements")
    
    add_heading_2(doc, "1. The Problem: The Recency Trap & The 180-Day Cliff")
    doc.add_paragraph(
        "In modern recruitment, hiring managers and corporate recruiters evaluate candidates through the lens of momentum. "
        "When an applicant's most recent position ended in 2022 or 2023, the visual impact on the page is jarring. "
        "Automated Applicant Tracking Systems (ATS) calculate the 'gap to date' and downrank the profile, while human reviewers "
        "unconsciously apply the 'Recency Trap'—assuming that someone who has not worked in two years has suffered severe cognitive "
        "and technical atrophy."
    )

    add_heading_2(doc, "2. Why It Happens: The Narrow Definition of Work")
    doc.add_paragraph(
        "Returners fall victim to the Recency Trap because they equate 'experience' exclusively with holding a salaried W-2 job "
        "at a recognized corporation. They completely overlook the reality of the modern decentralized economy."
    )
    doc.add_paragraph(
        "In the United States, fractional leadership, project-based contracting, and independent consulting represent multi-billion-dollar sectors. "
        "During a career break, professionals frequently deliver valuable expertise: advising a former colleague on an e-commerce migration, "
        "optimizing bookkeeping for a local family business, auditing marketing workflows for a boutique agency, or guiding a non-profit through "
        "vendor negotiations. Because no regular paycheck was issued, candidates mistakenly believe these contributions 'don't count.' "
        "They surrender their right to claim legitimate, verifiable professional work on their resumes."
    )

    add_heading_2(doc, "3. Common Mistakes: Toxic Fluff vs. Reckless Fabrications")
    doc.add_paragraph("Candidates attempting to bridge the gap without guidance consistently stumble into two catastrophic extremes:")
    doc.add_paragraph(
        "• The 'Domestic CEO' Trap: Writing 'Full-Time Family Caregiver / Household Manager (2022–Present)' and listing bullet points like "
        "'Negotiated with insurance adjusters, managed $50,000 medical budget, and streamlined home logistics.' While emotionally resonant, "
        "corporate recruiters unanimously dismiss this. It indicates that the candidate does not understand corporate boundaries and reminds "
        "hiring managers of ongoing domestic risks."
    )
    doc.add_paragraph(
        "• The Ghost Company Trap: Inventing a fictitious consultancy with zero clients, zero deliverables, and a purchased commercial domain. "
        "When an interviewer asks, 'Walk me through a specific engagement from Q3 2024 and your client's ROI,' the candidate collapses under scrutiny, "
        "revealing the entire entry to be an elaborate fiction."
    )

    add_heading_2(doc, "4. The Correct Approach: The Micro-Engagement Protocol")
    doc.add_paragraph(
        "The professional, bulletproof strategy is grounded in three words: **REAL WORK, PACKAGED SAFELY**.\n"
        "We never invent experience. Instead, we instruct returners to spend 1 to 2 weeks before actively applying to "
        "**execute 1 or 2 small, real-world advisory projects—even pro-bono or for a nominal fee—for a real business, former colleague, or non-profit**.\n"
        "You then legitimately position this on your resume as 'Independent Advisory / Project Consultant (2024–Present),' backed by real deliverables "
        "and an authentic client reference."
    )

    add_callout(
        doc,
        "THE CONSULTING UMBRELLA DOCTRINE:\n"
        "You do not need a Delaware C-Corp, millions in venture capital, or venture-backed clients to be a legitimate consultant.\n"
        "If you solve a real operational problem for an independent business, produce a tangible artifact (an audit, an SOP, a financial model), "
        "and possess a verifiable stakeholder who can confirm your contribution, you are an independent consultant under all legal and commercial standards.",
        title="ETHICAL LEGITIMACY PRINCIPLE"
    )

    add_heading_2(doc, "5. Step-by-Step Implementation: Launching Your Bridge Project in 10 Days")
    doc.add_paragraph("Follow this structured four-step protocol to construct your verifiable consulting bridge:")
    
    doc.add_paragraph("Step 1: Identify Your 'Angel Client' in Your Weak-Tie Network\n"
                  "Review your contact list for former coworkers who went out on their own, friends operating small businesses (agencies, clinics, retail shops, tech startups), or local community organizations. "
                  "Outreach script: 'Hey [Name], I'm updating my professional portfolio and taking on a couple of short-cycle advisory projects this month. I know you've been expanding your [operations/marketing/inventory]. If you have a workflow bottleneck that's been bugging you, I'd love to spend 10 hours next week auditing it and building you a clean execution SOP—completely on me. Let me know if that would be helpful!'")

    doc.add_paragraph("Step 2: Define a Scoped, Single-Deliverable Mandate\n"
                  "Do not attempt a massive corporate turnaround. Focus on a bite-sized deliverable completed in under 15 hours:\n"
                  "• Operations: A 5-page Standard Operating Procedure (SOP) for vendor onboarding;\n"
                  "• Finance: A dynamic 12-month rolling cash-flow forecast in Google Sheets / Excel;\n"
                  "• Marketing: A competitor pricing audit and customer review sentiment matrix;\n"
                  "• Tech / Engineering: A low-code automation connecting Typeform to Airtable / Slack to eliminate manual lead entry.")

    doc.add_paragraph("Step 3: Execute a Simple Statement of Work (SOW)\n"
                  "Formalize the engagement with a 1-page agreement or a confirmation email exchange (see Appendix C for the exact legal template). "
                  "This explicitly defines your role as an 'Independent Project Consultant' and secures the client's agreement to serve as a reference.")

    doc.add_paragraph("Step 4: Anchor the Role at the Top of Your Resume\n"
                  "Position the entry prominently under Professional Experience:\n"
                  "• Independent Project Consultant | Advisory Services               [Month, Year] – Present\n"
                  "• Provided targeted advisory in [your specialty] for growth-stage and boutique businesses.\n"
                  "• Developed [Deliverable X], improving operational efficiency by [Y]% (Client details confidential under NDA).")

    add_heading_2(doc, "6. Concrete Example: Three Functional Bridge Case Studies")
    
    # Bridge Case Table
    table = doc.add_table(rows=4, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["Functional Track", "Real Micro-Engagement Executed", "Professional Resume Entry (De-identified)"]
    col_widths = [1.5, 2.2, 2.5]
    
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
        
    case_data = [
        ("Finance & Accounting\n(2.5-Year Gap)", 
         "Audited overdue receivables and built a rolling cash forecast for an independent architectural firm.", 
         "INDEPENDENT FINANCIAL CONSULTANT (2024–Present)\n• Retained by boutique professional services firms to design cash-flow forecasting models and streamline AR collections.\n• Reconciled 18 months of historical ledger discrepancies, identifying $42K in unbilled retainers."),
         
        ("Marketing & Growth\n(3-Year Gap)", 
         "Revamped the email reactivation flow and analytics dashboard for a regional fitness chain.", 
         "INDEPENDENT GROWTH STRATEGIST (2024–Present)\n• Advised consumer businesses on lifecycle marketing and customer retention architecture.\n• Redesigned re-engagement email automation workflows, achieving a 28% open rate and generating $18K in incremental bookings."),
         
        ("Operations / Supply Chain\n(1.5-Year Gap)", 
         "Streamlined warehouse intake and return-merchandise authorization (RMA) for an Amazon FBA seller.", 
         "INDEPENDENT OPERATIONS ADVISOR (2024–Present)\n• Consulted with mid-market e-commerce merchants to resolve fulfillment and reverse-logistics bottlenecks.\n• Drafted standardized inspection SOPs, cutting return processing turnaround time from 7 days to 48 hours.")
    ]
    
    for row_idx, data in enumerate(case_data, start=1):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, 80, 80, 100, 100)
            set_cell_background(cell, "FFFFFF" if row_idx % 2 == 1 else "F7FAFC")
            p = cell.paragraphs[0]
            run = p.add_run(text)
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_heading_2(doc, "7. Practical Checklist: The Bridge Legitimacy Test")
    doc.add_paragraph("Before printing this role on your resume, ensure you satisfy all 5 criteria:")
    doc.add_paragraph("[1] A real business, entrepreneur, or non-profit benefited from my work.")
    doc.add_paragraph("[2] I have a finished digital artifact (spreadsheet, slide deck, SOP document) stored on my computer.")
    doc.add_paragraph("[3] I have written or email confirmation acknowledging my role as an external advisor/consultant.")
    doc.add_paragraph("[4] My client contact is aware they may be called as a professional reference.")
    doc.add_paragraph("[5] I can discuss the business context, methodology, and results in crisp, commercial terms for 3 minutes without hesitation.")

    add_heading_2(doc, "8. Immediate Actionable Step")
    doc.add_paragraph(
        "IMMEDIATE ACTION TODAY: Send a message to one former colleague or local business owner using the Step 1 outreach template. "
        "Offer to solve one specific administrative, operational, or marketing headache for them next week. "
        "The moment you deliver that solution, your employment gap is officially closed."
    )
    
    doc.add_page_break()

print("EN Chapter 2 ready.")
