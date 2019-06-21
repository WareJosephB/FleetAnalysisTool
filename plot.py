import matplotlib.pyplot as plt
import datetime
import constants

def add_value_labels(ax, spacing):
    for rect in ax.patches:
        ax.annotate("{:.1f}".format(rect.get_height()),(rect.get_x() + rect.get_width() / 2, rect.get_height()), xytext=(0, spacing),
                    textcoords="offset points", ha='center', va='bottom')

def showBoxPlot(dayArray, rotatePlot, width_px, height_px, dpi, labelX, companyName, rotate_xlabels_box, saveBoxPlot):
    X=(0, len(dayArray)+0.5)
    fig1, ax1 = plt.subplots()
    fig1.set_size_inches(width_px/dpi, height_px/dpi)
    if rotatePlot:
        spacing = 0
        dayArray.T.boxplot(vert=False)
        for vehicle in constants.garage:
            Y=(vehicle.mileRange,vehicle.mileRange)    
            ax1.plot(Y,X)
            if rotate_xlabels_box[0]:
                ax1.text(vehicle.mileRange,labelX+spacing, vehicle.name, rotation=rotate_xlabels_box[1])
            else:
                ax1.text(vehicle.mileRange,labelX+spacing, vehicle.name)
            spacing += labelX
    else:
        dayArray.T.boxplot()
        for vehicle in constants.garage:
            Y=(vehicle.mileRange,vehicle.mileRange)    
            ax1.plot(X,Y)
            ax1.text(labelX, vehicle.mileRange, vehicle.name)
    plt.suptitle("")
    ax1.set_title(companyName + " Fleet Analysis: " + str(datetime.date.today()))
    if (rotate_xlabels_box[0]):
        plt.xticks(rotation=rotate_xlabels_box[1])
    if saveBoxPlot:
        fig1.savefig(companyName+' Fleet Boxplot '+ str(datetime.date.today())+'.png', dpi=dpi, bbox_inches="tight")
    
def showBarChart(fleetFile, departmentColumn, mileageColumn, milesOverPercentage, companyName, width_px, height_px, dpi, rotate_xlabels_bar, saveBarChart, label_spacing):
    departmentArray = fleetFile.groupby(departmentColumn)[mileageColumn].agg(lambda x: 100*(1-sum(x>milesOverPercentage)/sum(x>0)))  
    fig1, ax1 = plt.subplots()
    ax1.set_title(companyName + " journeys under " +str(milesOverPercentage)+" miles: " + str(datetime.date.today()))
    ax1.set_ylabel('%age of all journeys under '+str(milesOverPercentage)+" miles.")
    fig1.set_size_inches(width_px/dpi, height_px/dpi)
    departmentArray.plot.bar()
    if (rotate_xlabels_bar[0]):
        plt.xticks(rotation=rotate_xlabels_bar[1])
    add_value_labels(ax1, label_spacing)
    if saveBarChart:
        fig1.savefig(companyName+' Department over '+str(milesOverPercentage)+' miles '+ str(datetime.date.today())+'.png', dpi=dpi, bbox_inches="tight")