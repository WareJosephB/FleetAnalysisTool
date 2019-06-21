[ui!] uk Fleet Analysis and Report Tool
==============

Requirements:
--------------

Pandas, matplotlib.pyplot, usually bundled with a Python installation, e.g. Anaconda, otherwise available through pip
FPDF available through pip

Python

Instructions for use
--------------

Fill out the example_constants.py file and rename to constants.py- this ensures that any changes you make to this file won't be overwritten at a later time. Any additions to this file will be mentioned in the commits and reflected in example_constants.

Place the logos you want in the top left and top right of the cover sheet in the project directory named 'logo_topLeft.png', 'logo_topRight.png', you may need to edit lines 18-19 of reportExporter.py to get them where you want or if you want to use a different file format [FPDF does not currently support .pngs with alpha channels or .svgs].

intro_explain.txt contains the text to be placed on the page after the title page, an introduction to what the project is and its aims. To ignore it, comment out line 8 of reportExporter.py. If this is ever used by someone outside of [ui!]uk then lines 10, 26, 28 also need removing of HelloEV to be changed to the relevant project you're working on. 

Ideally, you would have a CSV with at least the column[s] that identify a vehicle, the date of a journey [each date can have multiple journies, we encourage the most granularity possible], the number of miles gone on the journey and [if a departmental boxplot is wanted] a column identifying the department or collective that the journey is within. This would also be placed in the file directory and fileLocation, vehicleIdentifier [and _2 and the boolean CombinedUniqueKey if they are required for uniquely identifying a vehicle, e.g. Forename, Surname], mileageColumn, dateColumn, departmentColumn [if required] in FleetAnalysis.py edited to reflect the file (or vice versa).

I would recommend disabling the generateReport until you are happy with the charts and can have edited the description texts to add any insight you have gained from this information or from your interactions with the client. If there isn't a saved version of the BarChart or BoxPlot [saveBarChart or saveBoxPlot haven't been true at any point of running] then they will not be available for the report generator and includeBox/includeBar must be false or it will throw an error. They will automatically add a description page (description_[box/bar].txt), so this should be tailored appropriately.