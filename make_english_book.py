# -*- coding: utf-8 -*-
"""
The Career Reboot Armor: A Tactical Field Manual for Returning to the US Job Market
After Caregiving, Illness, or Extended Leave
Complete Production Generator (US Edition)
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_callout(doc, text, title="CORE PRINCIPLE"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.2)
    set_cell_background(cell, "F7FAFC")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="2B6CB0"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_title = p.add_run(f"[{title}]\n")
    run_title.font.bold = True
    run_title.font.size = Pt(10)
    run_title.font.color.rgb = RGBColor(0x2B, 0x6C, 0xB0)
    
    run_text = p.add_run(text)
    run_text.font.size = Pt(9.5)
    run_text.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_heading_1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(22)
    h.paragraph_format.space_after = Pt(10)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.bold = True
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
    return h

def add_heading_2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.bold = True
    run.font.size = Pt(12)
    run.font.color.rgb = RGBColor(0x2B, 0x6C, 0xB0)
    return h

def create_english_document():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Calibri'
    style_normal.font.size = Pt(10.5)
    style_normal.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
    style_normal.paragraph_format.line_spacing = 1.35
    style_normal.paragraph_format.space_after = Pt(6)
    
    # Title Page
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(36)
    p_title.paragraph_format.space_after = Pt(12)
    run_title = p_title.add_run("THE CAREER REBOOT ARMOR\nA Tactical Field Manual for Returning to the US Job Market\nAfter Caregiving, Illness, or Extended Leave")
    run_title.font.bold = True
    run_title.font.size = Pt(20)
    run_title.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(28)
    run_sub = p_sub.add_run("Bridging the Resume Gap, Passing Background Checks, and Bypassing the Algorithmic Meat Grinder")
    run_sub.font.size = Pt(11)
    run_sub.font.color.rgb = RGBColor(0x71, 0x80, 0x96)
    
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_after = Pt(40)
    run_meta = p_meta.add_run("Target Audience: Mid-to-senior US professionals re-entering the workforce after a 1–4 year career break.\nCore Standard: Strict adherence to US employment verification practices (FCRA, The Work Number) and ATS mechanics.\nZero Fluff. Zero Toxic Inspiration. Pure Tactical Execution.")
    run_meta.font.size = Pt(9.5)
    run_meta.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)

    doc.add_page_break()
    return doc

print("English Doc Generator Framework Ready.")
