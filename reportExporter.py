from fpdf import FPDF
import datetime

def report(companyName, buffer, owner, milesOverPercentage):
    reportPdf = FPDF()
    titlePage(companyName, buffer, reportPdf, owner)
    descriptionPage(reportPdf, 'HelloEV explanation.txt')
    chartPage(reportPdf, companyName+' Fleet Boxplot '+ str(datetime.date.today())+'.png', 'description.txt')
    reportPdf.output(companyName+ ' HelloEV analysis.pdf', 'F')


def titlePage(companyName, buffer, reportPdf, owner):
    reportPdf.add_page()
    reportPdf.set_font('Arial', 'B', 15)
    width = reportPdf.get_string_width(companyName) + buffer

    reportPdf.image('logo_[ui!]uk.png', 10, 8, 33)
    reportPdf.image('logo_HelloEV.png', 166, 3, 33)
    reportPdf.ln(100)
    reportPdf.set_x((210 - width) / 2)
    if len(companyName) > 40:
        reportPdf.cell(width-buffer, 9, companyName+':')
        reportPdf.ln(5)
        reportPdf.set_x((210 - width) / 2)
        reportPdf.cell(71, 9, 'HelloEV analysis '+str(datetime.date.today()))
    else:
        reportPdf.cell(width / 2, 9, companyName+': HelloEV analysis '+str(datetime.date.today()))
    reportPdf.ln(10)
    reportPdf.set_x((210 - width) / 2)
    reportPdf.set_font('Arial', '', 12)
    reportPdf.cell(width-10, 9, owner.name+', '+owner.company+': '+owner.email)
    
def chartPage(reportPdf, image, descriptionTextFile):
    reportPdf.add_page()
    reportPdf.set_font('Arial', '', 14)
    reportPdf.image(image)
    reportPdf.ln(10)
    reportPdf.write(5, open(descriptionTextFile, 'r').read())
    
def descriptionPage(reportPdf, descriptionFile):
    reportPdf.add_page()
    reportPdf.set_font('Arial', '', 14)
    reportPdf.write(5, open(descriptionFile, 'r').read())