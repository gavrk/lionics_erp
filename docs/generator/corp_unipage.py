from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph
from docs.generator.styles import dn1_style, pd1_style, ft1_style


def corp_unipage(c, doc, doc_date, doc_id):
    global dn1_text

    c.saveState()
    c.setFont('FreeSans', 12)
    styles = getSampleStyleSheet()

    # draw a rectangle
    c.setFillColorRGB(0.0, 0, 0.0)
    c.setStrokeColorRGB(0.0, 0, 0.0)
    c.rect(0.0 * cm, 27 * cm, 1 * cm, 3 * cm, fill=1)
    c.setFillColorRGB(0.35, 0, 0.35)
    c.setStrokeColorRGB(0.35, 0, 0.35)
    c.rect(0.0 * cm, 20 * cm, 1 * cm, 7 * cm, fill=1)
    c.setFillColorRGB(0.5, 0, 0.5)
    c.setStrokeColorRGB(0.5, 0, 0.5)
    c.rect(0.0 * cm, 0.0 * cm, 1 * cm, 20 * cm, fill=1)

    c.setFillColorRGB(0.5, 0, 0.5)
    c.setStrokeColorRGB(0.5, 0, 0.5)
    c.rotate(45)
    c.rect(13.85 * cm, 13.47 * cm, 1 * cm, 5 * cm, fill=1)
    c.rotate(-45)

    c.setFillColorRGB(0, 0, 0)
    c.setStrokeColorRGB(0, 0, 0)
    c.rotate(45)
    c.rect(17.79 * cm, 18.41 * cm, 2 * cm, 5 * cm, fill=1)
    c.rotate(-45)

    c.setFillColorRGB(0.35, 0, 0.35)
    c.setStrokeColorRGB(0.35, 0, 0.35)
    c.rect(13 * cm, 27 * cm, 8.5 * cm, 0.9 * cm, fill=1)

    c.setFillColorRGB(0.35, 0, 0.35)
    c.setStrokeColorRGB(0.35, 0, 0.35)
    c.rect(0.0 * cm, 0 * cm, 2 * cm, 6 * cm, fill=1)

    c.rotate(45)
    c.setFillColorRGB(0.35, 0, 0.35)
    c.setStrokeColorRGB(0.35, 0, 0.35)
    c.rect(3.665 * cm, 2.851 * cm, 2 * cm, 6 * cm, fill=1)
    c.rotate(-45)

    c.rotate(135)
    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(1, 1, 1)
    c.rect(0 * cm, -3 * cm, 3.2 * cm, 0.05 * cm, fill=1)
    c.rotate(-135)

    c.setFillColorRGB(0.35, 0, 0.35)
    c.setStrokeColorRGB(0.35, 0, 0.35)
    c.rect(2.035 * cm, 2.15 * cm, 16.5 * cm, 0.09 * cm, fill=1)

    pd1_text = f'г. Санкт-Петербург   /   {doc_date}'
    pd1 = Paragraph(pd1_text, pd1_style)
    pd1.wrap(500, 200)
    pd1.drawOn(c, 300, 772)

    dn1 = Paragraph(f'Договор № {doc_id}', dn1_style)
    dn1.wrap(500, 200)
    dn1.drawOn(c, 360, 800)

    c.drawImage('/home/gavrks/Documents/import_export_ops/aux/corp_int_logo.png',
                3 * cm, 0.6 * cm, width=0.9 * cm, height=0.9 * cm)

    web_text = 'www.oursite.com'
    wt1 = Paragraph(web_text, ft1_style)
    wt1.wrap(500, 200)
    wt1.drawOn(c, 20, 28)

    email_text = 'support@oursite.com'
    et1 = Paragraph(email_text, ft1_style)
    et1.wrap(500, 200)
    et1.drawOn(c, 20, 17)

    c.drawImage('/home/gavrks/Documents/import_export_ops/aux/corp_add_logo.png',
                13 * cm, 0.6 * cm, width=0.9 * cm, height=0.9 * cm)

    tel_text = '+7 (981) 915-89-50'
    tl1 = Paragraph(tel_text, ft1_style)
    tl1.wrap(500, 200)
    tl1.drawOn(c, 160, 28)

    email_text = '+7 (981) 915-89-50'
    et1 = Paragraph(email_text, ft1_style)
    et1.wrap(500, 200)
    et1.drawOn(c, 160, 17)

    c.drawImage('/home/gavrks/Documents/import_export_ops/aux/corp_tel_logo.png',
                8 * cm, 0.6 * cm, width=0.9 * cm, height=0.9 * cm)

    tel_text = '196158, г. Санкт-Петербург'
    tl1 = Paragraph(tel_text, ft1_style)
    tl1.wrap(500, 200)
    tl1.drawOn(c, 305, 28)

    email_text = 'Московское ш. 46, оф. 316'
    et1 = Paragraph(email_text, ft1_style)
    et1.wrap(500, 200)
    et1.drawOn(c, 305, 17)

    c.setFillColorRGB(1, 1, 1)
    c.setStrokeColorRGB(1, 1, 1)
    c.setFont('FreeSansBold', 12)
    c.drawString(25, 25, str(doc.page))

    c.restoreState()