import pandas as pd
import report, plot, reportExporter

fileLocation = 'real_data.csv'
encoding = 'UTF8' #Default is 'UTF8' if throws error try 'cp1252'
companyName = 'CUSTOMER' #For Chart Titles

vehicleIdentifier = 'CARERID' #These should be the column name of the correct column
vehicleIdentifier2 = 'COLOUR'
CombinedUniqueKey = False #Do you need both of the above to make a unique vehicle? [True/False]

mileageColumn = 'STDMILES'
dateColumn = 'THEDATE'

departmentColumn = 'DEPARTMENT' #Needed if showBarChart is True, otherwise ignored

showReport = True
generateReport = False
includeBox = True
includeBar = False
includeReport = True
buffer = 15 #Width around title of report

showBarChart = False
saveBarChart = False
rotate_xlabels_bar = [True, 45]
milesOverPercentage = 150 # Range to show percentage of journeys under this distance
label_spacing = 5
rotate_bar = True

showBoxPlot = False
saveBoxPlot = True
rotate_xlabels_box = [True, -90] #True or False, note capital, degrees to rotate: 0 = horizontal, 90 = up
labelX = -1 #Where in the x-axis the labels for the example EV ranges should be
rotate_box = True #Should boxplot be vertical (False) or horizontal (True)

width_px = 595 
height_px = 842
dpi = 100

'''Don't change anything below unless you're sure- remember, it's backed up on Github so you can always pull again'''

fleetFile = pd.read_csv(fileLocation,encoding=encoding, delimiter=',', error_bad_lines=False)

if (CombinedUniqueKey):
    dayArray = fleetFile.groupby([vehicleIdentifier,vehicleIdentifier2, dateColumn])[mileageColumn].sum().unstack()
else:
    dayArray = fleetFile.groupby([vehicleIdentifier, dateColumn])[mileageColumn].sum().unstack()

#dayArray = dayArray.reindex(index=dayArray.index.to_series().str[-2:].astype(int).sort_values().index)  '''Sorts on last 2 characters as ints'''

if showBarChart:
    plot.showBarChart(fleetFile, departmentColumn, mileageColumn, milesOverPercentage, companyName, width_px, height_px, dpi, rotate_xlabels_bar, saveBarChart, label_spacing)

if showBoxPlot:
    plot.showBoxPlot(dayArray, rotate_box, width_px, height_px, dpi, labelX, companyName, rotate_xlabels_box, saveBoxPlot)

if showReport:
    print(report.reportText(dayArray, companyName))

if generateReport:
    reportExporter.report(companyName, buffer, milesOverPercentage, includeBox, includeBar, dayArray, includeReport)
