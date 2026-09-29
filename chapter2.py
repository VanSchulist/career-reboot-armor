# -*- coding: utf-8 -*-
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx_helpers import set_cell_background, set_cell_margins, add_callout
from chapter1 import add_heading_1, add_heading_2

def build_chapter_2(doc):
    add_heading_1(doc, "第二章：履历过桥——合规构建“项目制顾问/独立咨询”真实外壳")
    
    add_heading_2(doc, "1. 问题：时间断崖与系统拒信")
    doc.add_paragraph(
        "现代企业的招聘系统（ATS）和初筛 HR，每天要浏览成百上千份简历。当一名求职者的最新一份经历停留在 2022 年或 2023 年时，"
        "简历在视觉上呈现出明显的“时间断崖”。在 ATS 自动化解析中，计算出的“当前失业月数”若超过阈值，简历将直接被系统降权排在最后；"
        "而在人工 HR 眼中，一个完全没有近期职场痕迹的候选人，会本能地被贴上“技能生疏、与业界脱节、缺乏战斗力”的负面标签。"
    )

    add_heading_2(doc, "2. 为什么发生：狭隘雇佣观遮蔽了自发专业价值")
    doc.add_paragraph(
        "求职者之所以任由断崖赤裸裸地暴露在简历顶端，核心症结在于将“工作经历”狭隘地等同于“在一家公司打卡领全职薪水并缴纳社保”。"
        "事实上，在现代商业社会中，“项目制交付（Project-based / Fractional Delivery）”、“独立咨询（Independent Advisory）”"
        "以及“自由顾问（Freelance Consultant）”早已是极为普遍且广受尊重的专业执业形态。"
    )
    doc.add_paragraph(
        "许多专业人士在照护家庭或休假期间，其实并未完全与社会断绝联系——他们曾给前同事的工作出谋划策、曾帮亲友的小微店铺诊断运营数据、"
        "曾在行业社群里撰写专业洞察、或无偿参与过某些非营利开源项目。只因这些事情没有按月发工资，求职者就自卑地认为它们“不算工作”，"
        "主动放弃了将这些宝贵的专业输出转化为合法履历的权利。"
    )

    add_heading_2(doc, "3. 常见错误：伪情怀毒药与粗糙伪造")
    doc.add_paragraph(
        "在处理最新经历空白时，求职者极易走向两个极端："
    )
    doc.add_paragraph(
        "【极端一：把家务写成管理岗位（伪情怀）】\n"
        "受网上某些鸡汤影响，在简历顶部写：“2022.09 - 至今：家庭全职照料者，负责全家预算管理、日常医疗排期调度与紧急事态协调”。"
        "一线 HR 和猎头对此极其反感。在商业雇佣语境下，招聘方付费购买的是商业业务问题的解决能力，而不是家务技能。"
        "此类写法不仅无法获得同情，反而直白地向雇主宣告：你的全部精力目前深陷于复杂的家庭羁绊中，难以全身心投入高强度工作。"
    )
    doc.add_paragraph(
        "【极端二：无中生有编造全职公司（实质造假）】\n"
        "找朋友的公司盖假公章、开具虚假在职证明，宣称自己在某公司全职任职 2 年。在现代背景调查中，只要背调机构要求提供个税申报记录、"
        "发薪银行流水（对公账户回执）或社保缴纳清单，这一谎言会在 10 秒内被击溃，彻底终结求职者的职业声誉。"
    )

    add_heading_2(doc, "4. 正确方法：微型项目真实交付，咨询架构合规过桥")
    doc.add_paragraph(
        "合规过桥的唯一正确法则可总结为八个字：**【微型交付，真实不虚】**。\n"
        "我们绝不伪造经历，而是指导求职者在正式投递简历前的 2 至 4 周内，**主动、真实地完成 1 至 2 次小规模的专业交付（哪怕是无偿或象征性收费的）**，"
        "然后以“独立咨询顾问（Independent Consultant / Fractional Specialist）”的身份，堂堂正正地将该项目作为当前的最新履历置于简历顶端。"
    )

    add_callout(
        doc,
        "商业真理：独立咨询与项目顾问不需要注册资金数千万的公司，也不需要按月发放全职工资。\n"
        "只要你针对真实的业务主体（即便是一家街边咖啡店、前同事的 3 人独立工作室、或亲友的电商店铺），"
        "实际产出了一份专业的分析报告、优化了某个业务环节，并有真实的业务对接人愿意为你背书，"
        "这段经历在法律、事实和商业逻辑上就是 100% 真实有效、无懈可击的专业实践！",
        title="过桥架构合法性原则"
    )

    add_heading_2(doc, "5. 具体步骤：四步完成你的第一个过桥项目")
    doc.add_paragraph("按照以下极简四步，花 1～2 周时间落地你的合法过桥项目：")
    
    doc.add_paragraph("第一步：圈定服务对象（寻找你的“天使客户”）\n"
                  "从你的弱关系网络中寻找正在创业、做个体生意、或者在中小团队任职的熟人：\n"
                  "- 正在做电商或自媒体的前同事；\n"
                  "- 经营实体诊所、餐厅、咨询工作室的亲友；\n"
                  "- 当地需要数字化梳理的非营利组织或行业社群。\n"
                  "主动沟通口径：“我最近在更新行业方法论，准备做几个微型咨询案例。你手头有没有什么头疼的运营/财务/行政流程琐事？我花一周时间免费帮你出个完整的梳理方案和执行规范。”绝大多数中小业务方会非常感激并欣然接受。")
    
    doc.add_paragraph("第二步：锁定单点交付物（必须落实在物理文件上）\n"
                  "切忌做宏大叙事，聚焦于解决一个具体的业务小痛点。必须有一份白纸黑字（或飞书/Notion文档）的实体成果：\n"
                  "- 运营方向：设计一套《私域用户转介绍与社群促活 SOP》；\n"
                  "- 人事方向：帮对方重新梳理一份《全职与兼职人员绩效提成与考核核算模型》；\n"
                  "- 财务方向：清洗对方过去半年的混乱账目，输出一份《现金流预测与供应链应付账款排期表》；\n"
                  "- 技术/IT方向：用无代码工具或现代开源框架帮对方搭建一套《自动化线索收集与通知机器人》。")
    
    doc.add_paragraph("第三步：签署极简备忘录或确认函（锁定合法证明人）\n"
                  "即便不收报酬，也请用邮件或纸质形式与对方签署一份《项目咨询服务备忘录（SOW）》或保留一封双方确认的往来邮件，明确：\n"
                  "- 项目名称（例如：某某零售品牌私域流程数字化优化项目）；\n"
                  "- 你的职责：独立项目顾问；\n"
                  "- 对方授权你可在脱敏后用于个人履历展示，并同意在未来求职时作为业务证明人（Reference）接受简短电话核实。")
    
    doc.add_paragraph("第四步：标准化命名并植入简历顶端\n"
                  "在简历顶部以专业标准格式排布（详见第三章）：\n"
                  "• 2024.11 – 至今：独立商业咨询 / 项目顾问（Independent Advisory）\n"
                  "• 聚焦方向：企业数字化提效与核心业务流程梳理\n"
                  "• 核心成果：（用量化指标真实描述你在上述项目中带来的具体优化）。")

    add_heading_2(doc, "6. 示例：三类职业的真实过桥范例展示")
    
    # 示例表格
    table = doc.add_table(rows=4, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    headers = ["职业方向", "服务对象与微型任务", "简历上的专业转化表述（脱敏）"]
    col_widths = [1.2, 2.2, 2.8]
    
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
        ("财务 / 审计主管\n（断层2年）", "为前同事新开办的文创设计工作室梳理混乱账目，搭建多项目成本核算模板。", "【独立财务咨询顾问】（2024.10 - 至今）\n• 为中小创意企业重构跨项目成本分摊与毛利测算模型，协助识别3处隐性损耗，改善现金流周转周期。\n• 搭建轻量化应收账款预警机制，梳理近百笔往来款项账目。"),
        ("电商 / 用户运营\n（断层3年）", "为亲戚经营的线下实体烘焙工坊搭建社群私域运营体系与积分兑换规则。", "【独立用户增长与私域顾问】（2024.08 - 至今）\n• 主导本地消费品牌私域社群SOP冷启动，规划新客裂变及会员积分机制，累计沉淀高净值客户1200+人。\n• 利用自动化工具重构日常促活内容流转流程，周均复购率提升18%。"),
        ("软件工程师 / IT\n（断层1.5年）", "利用开源大模型为一家本地物流中介开发飞书运单自动识别录入机器人。", "【独立技术顾问 / 自由开发】（2024.09 - 至今）\n• 基于OCR与LLM API构建轻量化货运单据结构化解析工具，实现多格式运单免人工核对直接入库。\n• 独立负责从架构设计、接口鉴权到端侧部署全流程，日均处理单据800+条。")
    ]
    
    for row_idx, data in enumerate(case_data, start=1):
        for col_idx, text in enumerate(data):
            cell = table.cell(row_idx, col_idx)
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, 80, 80, 100, 100)
            if row_idx % 2 == 1:
                set_cell_background(cell, "FFFFFF")
            else:
                set_cell_background(cell, "F7FAFC")
            p = cell.paragraphs[0]
            run = p.add_run(text)
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_heading_2(doc, "7. 检查清单：过桥项目合规与安全性 5 条铁律")
    doc.add_paragraph("在将过桥项目写进简历之前，请逐项自我核对：")
    doc.add_paragraph("【1】真实存在：有真实的受众或业务方，我真真切切花时间输出了文档、方案、代码或分析表格。")
    doc.add_paragraph("【2】证据确凿：我的电脑里有一份完整的、可随时脱敏展示给面试官看的交付成果物（PPT/文档/表格）。")
    doc.add_paragraph("【3】证明人就位：对方负责人知道我以此名义求职，并答应在背调或背调电话核实时代为证明业务真实性。")
    doc.add_paragraph("【4】不虚构大厂：我绝未在过桥项目中冒充世界500强或著名上市公司（写小微企业或客户名称脱敏是通行的安全惯例）。")
    doc.add_paragraph("【5】商业逻辑自洽：我能用一分钟流利解释该项目的商业背景、痛点、我的切入点以及最终带来的改善。")

    add_heading_2(doc, "8. 读者可以立即执行的行动")
    doc.add_paragraph(
        "【立即行动】：不要等待外部机会降临。今天打开微信或手机通讯录，找到一个正在创业、带团队或自己做生意的朋友，"
        "给他打个电话或发条消息，主动承担一个耗时不超过 3 天的微型方案梳理。只要这第一份成果出炉，你的职业空白期在事实上就已经彻底终结。"
    )
    
    doc.add_page_break()

print("Chapter 2 module ready.")
