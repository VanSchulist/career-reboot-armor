# -*- coding: utf-8 -*-
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx_helpers import set_cell_background, set_cell_margins
from make_english_book import add_heading_1, add_heading_2, add_callout

def build_en_chapter_1(doc):
    add_heading_1(doc, "Chapter 1: The Reality Check — Demystifying Background Checks & Dismantling Gap Paranoia")
    
    add_heading_2(doc, "1. The Problem: The Phantom Investigator & Self-Sabotage")
    doc.add_paragraph(
        "For professionals returning to the United States job market after a prolonged break—whether 12 months or 4 years "
        "spent caring for a parent with Alzheimer's, managing an acute family health crisis, or recovering from a serious medical condition—the "
        "greatest barrier to re-entry is rarely external. It is an internal, paralyzing dread: 'If a prospective employer runs a background check, "
        "they will discover I haven't held a W-2 job in three years. They will flag me, think I'm unemployable, and pull my offer.'"
    )
    doc.add_paragraph(
        "This phantom anxiety leads candidates into catastrophic behaviors: they either self-select out of senior roles they are fully qualified for, "
        "or they commit fatal resume fraud—extending employment dates by a few years in a desperate attempt to erase the gap. Both reactions stem "
        "from a fundamental misunderstanding of how employment screening operates under federal US law."
    )

    add_heading_2(doc, "2. Why It Happens: Conflating Criminal Investigations with Commercial Screening")
    doc.add_paragraph(
        "Job seekers mistakenly imagine background check companies (such as HireRight, Sterling, First Advantage, or Equifax's The Work Number) "
        "as forensic detective agencies with boundless access to IRS tax filings, bank statements, and personal diaries. The reality is radically different."
    )
    doc.add_paragraph(
        "Under the Fair Credit Reporting Act (FCRA), Consumer Reporting Agencies (CRAs) are strictly regulated commercial entities hired to perform "
        "low-cost, automated database comparisons. They are paid to answer one narrow question: 'Did this candidate work at the specific companies "
        "listed on their signed Background Check Authorization Form during the exact dates specified?'"
    )
    doc.add_paragraph(
        "They do NOT proactively scour the internet to uncover what you did during periods you left blank. In the eyes of US employment law, "
        "an employment gap is not a crime, a violation, or a discrepancy. It is simply a period of non-employment. Fraud occurs only when a candidate "
        "claims to have been on an employer's payroll when they were not."
    )

    add_heading_2(doc, "3. Common Mistakes: Manufacturing Real Fraud to Hide a Legal Break")
    doc.add_paragraph("When confronted by an employment gap, returners frequently make one of three fatal errors:")
    
    # Error comparison table
    table = doc.add_table(rows=4, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["The Fatal Mistake", "The Candidate's False Assumption", "The Inevitable Industry Outcome"]
    col_widths = [1.8, 2.0, 2.4]
    
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
        
    error_data = [
        ("Pushing Out the End Date\n(e.g., Left real job in Dec 2022; listed as Dec 2024)", 
         "\"HR won't notice a few months, and my old manager will cover for me.\"", 
         "[OFFER RESCINDED] CRA calls corporate HR or checks The Work Number payroll records. A 60-day date discrepancy triggers an automated 'Major Discrepancy' flag. Candidate is disqualified for resume fraud."),
         
        ("Buying a Shell Company Reference\n(Using paid reference services or fake LLCs)", 
         "\"As long as someone picks up the phone with a script, I'm covered.\"", 
         "[BLACKLISTED] Modern CRAs run Secretary of State corporate registry checks and cross-reference EINs. Shell entities without legitimate tax or payroll history trigger immediate fraud alerts across enterprise ATS databases."),
         
        ("Treating Caregiving as a Corporate Job\n(Listing 'Full-time Family CEO' on resume)", 
         "\"It shows I managed budgets, crisis scheduling, and advocacy.\"", 
         "[INSTANT REJECTION] Hiring managers and recruiters view this as unprofessional fluff that screams 'high absenteeism risk' and reveals deep domestic entanglements that may compete with intense work demands.")
    ]
    
    for row_idx, data in enumerate(error_data, start=1):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, 80, 80, 100, 100)
            set_cell_background(cell, "FFFFFF" if row_idx % 2 == 1 else "F7FAFC")
            p = cell.paragraphs[0]
            run = p.add_run(text)
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0xC5, 0x30, 0x30) if col_idx == 2 else RGBColor(0x2D, 0x37, 0x48)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_heading_2(doc, "4. The Correct Approach: The Dual-Track Reporting Rule")
    doc.add_paragraph(
        "To navigate US hiring safely, you must maintain a strict mental separation between two distinct documents:\n"
        "1. The Legal Background Check Authorization Form: A legal affidavit. Every single date, job title, and company name must be 100% accurate down to the month, matching W-2s and official separation notices. Gaps are designated honestly as 'Career Break' or left unlisted as periods of unemployment.\n"
        "2. The Commercial Marketing Resume: A persuasive professional document designed to pass ATS keyword parsing and human review by bridging the timeline with legitimate advisory, project, or consulting work (detailed in Chapter 2)."
    )

    add_callout(
        doc,
        "THE DUAL-TRACK IMMUNITY PRINCIPLE:\n"
        "Your resume is marketing material; your background check form is a legal attestation.\n"
        "As long as every past employer on your background check form matches payroll records to the exact month, "
        "an intervening gap will be classified by HireRight/Sterling as 'Normal Non-Employment.' "
        "It will NEVER fail a background check or rescind an offer on legal compliance grounds.",
        title="FCRA COMPLIANCE IRON RULE"
    )

    add_heading_2(doc, "5. Step-by-Step Implementation: Auditing Your Payroll Record")
    doc.add_paragraph("Before sending out a single resume, execute this four-step audit to eliminate surprises:")
    doc.add_paragraph("Step 1: Pull Your Free Employment Data Report (EDR)\nUnder FCRA regulations, you are entitled to a free copy of your employment history file. Visit The Work Number website (theworknumber.com) and request your personal Employment Data Report. This reveals precisely what previous employers reported to Equifax regarding your hire dates, termination dates, and payroll titles.")
    doc.add_paragraph("Step 2: Collect Your Documentary Proof\nLocate your W-2 forms for the last 5 years, your final paystubs from your last full-time employer, and your signed Separation Agreement. If a past employer went out of business or merged, these documents serve as definitive proof of employment during manual verification.")
    doc.add_paragraph("Step 3: Lock Down Your Hard Baseline Dates\nRecord the exact month and year of your official termination date (e.g., October 2022). This date is an immovable anchor; you will never alter it on any background screening portal.")
    doc.add_paragraph("Step 4: Re-establish Warm Contact with References\nReach out to your previous direct supervisor or a trusted senior colleague. Confirm their current email and cell phone number, and verify they are willing to serve as a professional reference who can speak to your past achievements.")

    add_heading_2(doc, "6. Concrete Example: How a Clean Background Check Report Looks")
    doc.add_paragraph(
        "Case Study: Sarah M., Former Director of Operations. Resigned in September 2022 to provide hospice care for her father until early 2024. Started independent advisory projects in mid-2024. Received an offer from a mid-sized SaaS company in March 2025."
    )
    doc.add_paragraph(
        "What Sarah submitted on her HireRight screening portal:\n"
        "• Employer 1 (2016.04 – 2022.09): Global Logistics Corp | Director of Operations\n"
        "• Gap Period (2022.10 – 2024.05): Listed as 'Career Break / Family Health Matter' (No verification required)\n"
        "• Independent Consulting (2024.06 – Present): Provided client reference and copy of SOW\n\n"
        "The HireRight Screening Report delivered to the hiring company:\n"
        "• Global Logistics Corp: Dates Verified (Clear). Title Verified (Clear).\n"
        "• Criminal / Sanctions / Identity: Clear.\n"
        "• Overall Adjudication: MEETS COMPANY STANDARDS (Green Checkmark)."
    )

    add_heading_2(doc, "7. Practical Checklist: The Pre-Submission Background Audit")
    doc.add_paragraph("Before submitting any official background check portal form, verify:")
    doc.add_paragraph("[1] Every start and end date matches my W-2 or separation letter within 30 days.")
    doc.add_paragraph("[2] Job titles reflect official HR payroll titles (or use 'Functional Title / Payroll Title' formatting).")
    doc.add_paragraph("[3] I have not listed any shell company, phantom employer, or unverified payroll entity.")
    doc.add_paragraph("[4] My designated supervisor reference is aware of my job search and has my updated resume.")
    doc.add_paragraph("[5] I understand that an employment gap is a neutral timeline fact, not an ethics violation.")

    add_heading_2(doc, "8. Immediate Actionable Step")
    doc.add_paragraph(
        "IMMEDIATE ACTION TODAY: Log into your personal tax portal (or your files), locate the W-2 from your last year of full-time employment, "
        "and note the exact corporate name and termination month. Create a dedicated folder on your computer named 'Verification_Vault' "
        "containing your last paystub and W-2. Your factual foundation is now locked down."
    )
    
    doc.add_page_break()

print("EN Chapter 1 ready.")
