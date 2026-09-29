# -*- coding: utf-8 -*-
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx_helpers import set_cell_background, set_cell_margins, add_callout
from chapter1 import add_heading_1, add_heading_2

def build_chapter_3(doc):
    add_heading_1(doc, "第三章：格式突围——穿透 ATS 算法的“混合型（Hybrid）”简历工程")
    
    add_heading_2(doc, "1. 问题：网申投递的“数字黑洞”")
    doc.add_paragraph(
        "大量休假归来的求职者在网申（各大招聘网站、企业内推通道、猎头邮箱）时遭遇极其残酷的现实：投递出几百封简历，"
        "绝大多数显示“未读”或在几分钟后收到冰冷的自动拒信模板。求职者往往归咎于“大环境太差”或“自身资历不够”，"
        "却完全没有意识到：**在90%的大中型企业和知名招聘平台上，你的简历根本没有机会被任何人类HR看上一眼，"
        "它在进入数据库的第 3 秒，就已经被 ATS（Applicant Tracking System，求职者追踪系统）的算法在后台静默淘汰并自动归档了。**"
    )

    add_heading_2(doc, "2. 为什么发生：ATS 机器人的解析偏执与传统版式破绽")
    doc.add_paragraph(
        "主流招聘系统（如外企使用的 Workday、Taleo、Greenhouse、iCIMS，以及国内主流招聘大厂的简历中台）本质上是一台笨拙的“文本正则表达式提取机”。"
        "算法在扫描一份简历时，会执行两项致命的自动化计算："
    )
    doc.add_paragraph(
        "第一项是【职位状态计算（Current Employment Calculation）】：算法会抓取简历中最顶端一段经历的结束时间（End Date）。"
        "如果该时间不是“至今/Present”，系统会自动计算 `当前日期 - 最新经历结束日期`。当这个差值超过 180 天（半年）时，"
        "在招聘系统的后台候选人看板上，算法会自动给该候选人打上“长期非在职（Unemployed Gap）”的过滤标签，或直接在排序权重中下调 40%～60%。"
    )
    doc.add_paragraph(
        "第二项是【文本层级坍塌（Text Hierarchy Collapse）】：现代求职者为了追求视觉美观，喜欢使用 Canva 等设计软件制作双栏简历、"
        "把文字塞在装饰性文本框里、或者用表格来对齐日期。当 ATS 机器人提取这些非标准文档时，文本流会发生严重错位——"
        "左栏的公司名和右栏的毕业院校混在一起，系统判定为乱码或信息缺失，直接触发自动丢弃。"
    )

    add_heading_2(doc, "3. 常见错误：掩耳盗铃的花哨设计")
    doc.add_paragraph("面对格式排版，求职者极易踩中以下四颗地雷：")
    doc.add_paragraph("• 【地雷一：纯职能型简历（Functional Resume）】把所有时间线全部抹去，只写“项目管理能力、财务审计能力”。人类 HR 看到这种简历的第一秒就会判定该求职者在刻意隐瞒严重的履历污点，在初筛淘汰率高达 95% 以上。")
    doc.add_paragraph("• 【地雷二：年份模糊法（Year-only Masking）】所有工作只写年份不写月份（例如写“2018 - 2021”）。ATS 系统在解析只有年份的数据时，会自动默认设置为该年的 1 月 1 日，常常导致原本正常的工龄被机器误算成大断层，弄巧成拙。")
    doc.add_paragraph("• 【地雷三：多栏排版与复杂图形】使用左右分栏、技能进度条（如显示“Python掌握80%”的图表）。这些非文本元素在 ATS 解析器中全部沦为不可读乱码，导致核心关键词提取失败。")
    doc.add_paragraph("• 【地雷四：导出为低质图片或加密PDF】有些求职者担心排版错乱把简历存成全图 PDF，ATS 无法识别 OCR，直接判定为空白简历。")

    add_heading_2(doc, "4. 正确方法：单栏倒序“混合型（Hybrid）”架构")
    doc.add_paragraph(
        "既要让机器算法满意，又要让人类 HR 惊艳，唯一在实战中经过检验的解决方案是：**【单栏倒序混合型简历（Hybrid Chronological Resume）】**。\n"
        "这种架构的核心设计哲学是：\n"
        "1. **对机器绝对友好**：纯单栏排版，无文本框、无复杂表格嵌套、使用标准的 `YYYY.MM - 至今` 日期格式，确保 ATS 机器人能够 100% 精确提取时间轴与关键词；\n"
        "2. **对人类先声夺人**：在简历最上方黄金视觉区（首屏前 1/3），设立高强度的“专业成果矩阵与现代化工具栈”，用真实的商业价值先入为主地建立高段位人设，随后自然衔接第二章搭建的“过桥顾问项目”，让人类 HR 在看到过往全职工作之前，就已经认定了你是一名具备活跃战斗力的专业老兵。"
    )

    add_callout(
        doc,
        "混合型简历排版三大金律：\n"
        "1. 绝不使用双栏或多栏，全文自上而下单向流动（Single Column Only）。\n"
        "2. 日期格式全篇严格统一为【YYYY.MM – YYYY.MM】或【YYYY.MM – 至今】，靠右对齐或紧跟在公司名后。\n"
        "3. 字体选用跨平台标准无衬线字体（中文：微软雅黑/苹方，英文：Calibri/Arial），字号正文严格保持在 10～10.5 磅之间。",
        title="ATS 穿透设计规范"
    )

    add_heading_2(doc, "5. 具体步骤：自上而下重塑简历的四大物理板块")
    doc.add_paragraph("请打开空白文档，按照以下标准层级自上而下重新组装你的简历：")

    doc.add_paragraph("第一板块：头部名片与核心标签（Header & Title）\n"
                  "姓名、清晰的联系方式（手机、邮箱、常驻城市、领英/作品集链接）。紧随其后给出极其精准的专业定位标签（例如：资深运营总监 | 10年跨国供应链与数字化项目管理经验）。")

    doc.add_paragraph("第二板块：专业成果与核心能力矩阵（Executive Summary & Core Competencies）\n"
                  "严禁写“本人吃苦耐劳”等空话。用 3～4 条带有硬核数字的要点总结你职业生涯的核心商业价值：\n"
                  "• 累计主导超过 3000 万规模的数字化重构项目，团队管理峰值达 25 人；\n"
                  "• 擅长复杂业务流程解耦与跨部门利益博弈，平均降低交付周期 25%；\n"
                  "• 深度掌握现代协作工具栈（飞书/Notion/Jira）及利用生成式 AI 搭建业务提效工作流。")

    doc.add_paragraph("第三板块：最新在职过桥项目（Current Advisory / Projects）\n"
                  "【时间】：2024.08 – 至今\n"
                  "【身份】：独立商业咨询 / 项目顾问（可注明业务领域，如：零售数字化业务咨询）\n"
                  "【核心交付】：按【业务痛点 → 采取行动 → 量化结果】写 2～3 条真实微型交付成果。这一栏的物理存在，在算法上直接重置了系统的“失业天数计数器”，彻底切断了 ATS 的断层拦截。")

    doc.add_paragraph("第四板块：历史全职核心履历（Professional Experience，时间倒序）\n"
                  "按标准倒序排布你休假前的高光任职：【公司名称】、【任职年月】、【官方职衔】。\n"
                  "每一段经历精选 3～5 条带有强动作动词（主导、重塑、搭建、谈判、优化）与可验证业绩指标的陈述。")

    add_heading_2(doc, "6. 示例：标准单栏混合型简历模板骨架展示")
    
    # 模拟简历样板框
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    cell = table.cell(0, 0)
    cell.width = Inches(6.2)
    set_cell_background(cell, "FAFAFA")
    set_cell_margins(cell, 120, 120, 140, 140)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    
    sample_text = (
        "【张建国 | 资深供应链与精益运营专家】\n"
        "电话：138-XXXX-XXXX | 邮箱：jianguo.zhang@email.com | 现居：上海市浦东新区\n"
        "————————————————————————————————————————\n"
        "【核心专业实力与工具矩阵】\n"
        "• 12年制造业供应链全链路统筹经验，累计管理采购与生产周转资金逾1.5亿元。\n"
        "• 擅长利用数字化工具对传统仓储与排产流程进行敏捷重塑，平均降低呆滞物料库存30%以上。\n"
        "• 掌握工具栈：SAP S/4HANA, 飞书多维表格, Python数据清洗, 自动化工作流与生成式AI辅助审计。\n\n"
        "【专业项目经历 / 独立商业咨询】\n"
        "独立精益运营顾问 | 某消费制造企业数字化重塑项目        2024.09 – 至今\n"
        "• 业务背景：受聘为处于转型期的小微制造企业提供仓储周转与订单流向诊断咨询。\n"
        "• 行动方案：独立重构物料入库质检与BOM表自动校对流程，搭建轻量级自动化跟单看板。\n"
        "• 交付成果：协助客户消除了70%的人工跨表对账冗余，准时交付率从81%提升至94%。\n\n"
        "【全职工作经历（历史核心）】\n"
        "某某全球物流供应链集团 | 华东区供应链总监               2016.03 – 2022.08\n"
        "• 统筹下辖4个区域分拨中心日常运转，领导由4名经理、35名专业专员构成的运营团队。\n"
        "• 主导实施WMS仓储管理系统与TMS运输调度系统无缝对接，年节约外包干线运费逾420万元。\n"
        "• 建立供应商双月度动态绩效考核与红黄牌淘汰机制，入围供应商交付合规率达到98.5%。\n"
        "（...后续依次倒序排列更早期的真实任职...）"
    )
    run_sample = p.add_run(sample_text)
    run_sample.font.name = 'Consolas'
    run_sample.font.size = Pt(8.5)
    run_sample.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_heading_2(doc, "7. 检查清单：ATS 穿透与版式自查 7 项铁律")
    doc.add_paragraph("在点击投递之前，逐一核实以下 7 项标准：")
    doc.add_paragraph("【1】单栏排版：全文从头到尾只有一栏，绝无左右分栏设计。")
    doc.add_paragraph("【2】无文本框：全文文字全部写在主文档流中，未插入任何可移动的独立文本框或图形。")
    doc.add_paragraph("【3】规范日期：所有经历起止时间均为标准的 `YYYY.MM - YYYY.MM` 格式，最新过桥项目明确标注为 `YYYY.MM - 至今`。")
    doc.add_paragraph("【4】标准字体：采用系统原生无衬线字体，未嵌入任何小众特殊字体或自制图标。")
    doc.add_paragraph("【5】格式导出：导出格式为标准的 `.docx` 或由 Word 直接导出的非加密文本型 `.pdf`（严禁打印扫描成图片）。")
    doc.add_paragraph("【6】文本可复制：用鼠标在导出的 PDF 上随意划选一段文字，能流畅复制并粘贴出清晰的文字，无乱码。")
    doc.add_paragraph("【7】关键词命中：针对目标岗位的招聘描述（JD），岗位所要求的核心硬技能名词已自然融入前两板块的矩阵中。")

    add_heading_2(doc, "8. 读者可以立即执行的行动")
    doc.add_paragraph(
        "【立即行动】：不要在现有的旧简历上小修小补。今天新建一个空白 Word 文档，将上面第 6 节的单栏骨架复制进去，"
        "将你现有的文字逐段清洗并填充进去。完成之后，将其存为纯文本 `.txt` 打开检查一遍：如果文字顺序完全清晰可读，"
        "你的简历就已经成功战胜了全网 80% 会被系统直接绞碎的花哨简历。"
    )
    
    doc.add_page_break()

print("Chapter 3 module ready.")
