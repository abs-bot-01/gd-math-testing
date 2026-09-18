from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from pathlib import Path

out = Path('/home/abs-bot-01/Hermes/hermes-tester/tester-data/reports/stackBasicShapes_device_test_report.docx')
doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(.6); sec.bottom_margin = Inches(.6); sec.left_margin = Inches(.65); sec.right_margin = Inches(.65)
styles = doc.styles
styles['Normal'].font.name = 'Arial'; styles['Normal'].font.size = Pt(9)
for name in ['Heading 1','Heading 2']:
    styles[name].font.name='Arial'

def heading(text, level=1): doc.add_heading(text, level=level)
def para(text, bold_prefix=None):
    p=doc.add_paragraph()
    if bold_prefix and text.startswith(bold_prefix):
        p.add_run(bold_prefix).bold=True; p.add_run(text[len(bold_prefix):])
    else: p.add_run(text)

def table(headers, rows):
    t=doc.add_table(rows=1, cols=len(headers)); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for c,h in zip(t.rows[0].cells,headers): c.text=h
    for row in rows:
        cells=t.add_row().cells
        for c,v in zip(cells,row): c.text=str(v)
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs: r.font.size=Pt(7.5)
    return t

doc.add_heading('Device Test Report: stackBasicShapes',0)
para('Result: PASS — one board completed and transitioned to a new board during direct Godot execution.', 'Result: ')
heading('Level Information',2)
table(['Property','Value'],[
['Level ID','stackBasicShapes'],['Title','Sort Objects by 2D Shape'],['Device','Linux desktop via Godot 4.6.1 / Xvfb :99'],['Level type','icmV2'],['Age','6'],['Branch','Geometry'],['Variants','numberTile → numberSlot'],['Challenge','{}'],['Configured board count','10'],['Board time','28 seconds'],['Learning concept','Sort objects by 2D shape'],['Source','/shared/hermes/gd-math-godot/assets/config.json']])
heading('Correct Solution Sequence',2)
for x in ['Drag the first circular-shape object to the upper circular group slot.','Drag the second circular-shape object to the upper circular group slot.','Drag the first non-circular shape object to the lower group slot.','Drag the second non-circular shape object to the lower group slot.','All objects are grouped; the board transitions to a new board, confirming completion.']:
    doc.add_paragraph(x, style='List Number')
heading('Test Results',2)
table(['Property','Expected','Observed','Result','Evidence'],[
['Level loading','Board opens','Board rendered in Godot','PASS','00_initial'],['Identity','Correct ID/title','Matched ID and title','PASS','00_initial'],['Board layout','Objects/slots visible','Visible','PASS','00_initial'],['Touch interaction','Drag/drop responds','Drag gestures performed','PASS','01–04 before/after'],['Correct validation','Objects accepted','Objects stayed in groups','PASS','01–04 after'],['Completion','Board completes','New board appeared','PASS','final'],['Device layout','No clipping','1280×720 visible','PASS','00_initial'],['Performance','No crash/freeze','None observed','PASS','Video']])
heading('Action-by-Action Evidence',2)
table(['Action','Object / group','Before screenshot','After screenshot','Observed result'],[
['01','Circular object → upper circular group','stackBasicShapes_01_before_move.png','stackBasicShapes_01_after_move.png','Accepted'],['02','Shape object → lower group','stackBasicShapes_02_before_move.png','stackBasicShapes_02_after_move.png','Accepted'],['03','Circular object → upper circular group','stackBasicShapes_03_before_move.png','stackBasicShapes_03_after_move.png','Accepted'],['04','Shape object → lower group','stackBasicShapes_04_before_move.png','stackBasicShapes_04_after_move.png','Accepted']])
heading('Issues Found',2)
para('No confirmed gameplay defect for the completed board. Earlier attempts showed that releasing near the slot boundary can reject a drag; the completed attempt released inside the destination group.')
heading('Recommended Fixes',2)
for x in ['No code fix implemented.','Keep drop targets sufficiently large and visually clear.','For future QA, record each board separately because the level configuration specifies 10 boards.']:
    doc.add_paragraph(x, style='List Bullet')
heading('Final Result',2)
para('PASS — one board was completed and the game transitioned to the next board. This report does not claim that all 10 configured boards were completed.', 'PASS —')
heading('Screenshot Paths',2)
base='/home/abs-bot-01/Hermes/hermes-tester/tester-data/artifacts/gd-math-levels/action-evidence/'
for n in ['stackBasicShapes_00_initial.png','stackBasicShapes_01_before_move.png','stackBasicShapes_01_after_move.png','stackBasicShapes_02_before_move.png','stackBasicShapes_02_after_move.png','stackBasicShapes_03_before_move.png','stackBasicShapes_03_after_move.png','stackBasicShapes_04_before_move.png','stackBasicShapes_04_after_move.png','stackBasicShapes_final.png']:
    doc.add_paragraph(base+n, style='List Bullet')
para('Evidence note: Screenshots are PNG captures at 1280×720. No project files, source, assets, scenes, settings, or configuration were modified.')
doc.save(out)
print(out)
