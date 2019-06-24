from fpdf import FPDF
import datetime
import report as numeric
import constants

def report(companyName, buffer, milesOverPercentage, includeBox, includeBar, dayArray, includeReport):
    reportPdf = FPDF()
    reportPdf.set_auto_page_break(0)
    titlePage(companyName, buffer, reportPdf)
    if includeReport:
        numericPage(reportPdf, dayArray, companyName)
        reportPdf.ln(5)
        reportPdf.write(5, '* estimated')
    descriptionPage(reportPdf, 'intro_explain.txt')
    if includeBox:
        chartPage(reportPdf, companyName+' Fleet Boxplot '+ str(datetime.date.today())+'.png', 'description_box.txt')
        reportPdf.set_font('Arial', 'I', 8)
        with open('citationsList.txt', 'r') as fd:
            
            lines = fd.read().splitlines()
            reportPdf.set_y(-5-(5*len(lines)))
            for line in lines:
                reportPdf.cell(0, 10, line)
                reportPdf.ln(5)
    if includeBar:
        chartPage(reportPdf, companyName+' Fleet Boxplot '+ str(datetime.date.today())+'.png', 'description_bar.txt')    
    descriptionPage(reportPdf, 'outtro_explain.txt')
    reportPdf.output(companyName+ ' HelloEV analysis.pdf', 'F')

def titlePage(companyName, buffer, reportPdf):
    reportPdf.add_page()
    reportPdf.set_font('Arial', 'B', 15)
    width = reportPdf.get_string_width(companyName) + buffer

    reportPdf.image('logo_topLeft.png', 10, 8, 33)
    reportPdf.image('logo_topRight.png', 166, 3, 33)
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
    reportPdf.cell(width-10, 9, constants.owner.name+', '+constants.owner.company+': '+constants.owner.email)
    
def chartPage(reportPdf, image, descriptionTextFile):
    reportPdf.set_auto_page_break(0)
    reportPdf.add_page()
    reportPdf.set_font('Arial', '', 14)
    reportPdf.image(image)
    reportPdf.add_page()
    reportPdf.write(5, open(descriptionTextFile, 'r').read())
    
def descriptionPage(reportPdf, descriptionFile):
    reportPdf.set_auto_page_break(1)
    reportPdf.add_page()
    reportPdf.set_font('Arial', '', 14)
    reportPdf.write(5, open(descriptionFile, 'r').read())
    
def numericPage(reportPdf, dayArray, companyName):
    reportPdf.set_auto_page_break(1)
    reportPdf.add_page()
    reportPdf.set_font('Courier', '', 14)
    reportPdf.write(5, str(numeric.reportText(dayArray, companyName)))
