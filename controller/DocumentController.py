from docx import Document
from docx.document import Document as Doc
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import RGBColor
from docx.shared import Inches
from docx.shared import Pt

def write_name_card(document: Doc, name_card):
    p = document.add_paragraph()
    text = p.add_run(name_card)
    text.bold = True
    text.font.size = Pt(12)

def write_info(document: Doc, title: str, info: str):
    p = document.add_paragraph()
    p.add_run(f'{title}: ').bold = True
    p.add_run(info)

def write_activities(document: Doc, activities: list):
    p = document.add_paragraph()
    p.add_run('Atividades:').bold = True

    if activities:
        cont = 0
        for activity in activities:
            cont+=1
            p.add_run(f'\n\n{cont}. ').bold = True
            p.add_run(f'{activity["name"]} ({activity["state"]})')
    else:
        write_not_added(p, 'Nenhuma atividade adicionado')

def write_evidences(document: Doc, folder_evidences: str, evidences: list):
    p = document.add_paragraph()
    p.add_run('Evidências:').bold = True

    images_not_found = []
    if evidences:
        for evidence in evidences:
            p = document.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            file_extension = str(evidence['url']).split('.')[-1].lower()
            file_name = str(evidence['name']).split('.')[0] + '.' + file_extension
            
            try:
                p.add_run().add_picture(f"{folder_evidences}/{file_name}", width=Inches(6))
                document.add_paragraph('Figura: linha product line').alignment = WD_ALIGN_PARAGRAPH.CENTER
            except:
                images_not_found.append(file_name)
    else:
        write_not_added(p, 'Nenhuma evidência adicionada')

    if images_not_found:
        print('Imagens não encontradas: ')
        print(images_not_found)

def write_blank_line(document: Doc):
    document.add_paragraph('\n')

def write_not_added(paragraph, info):
    text = paragraph.add_run(f' {info}')
    text.italic = True
    text.font.color.rgb = RGBColor(255, 0, 0)