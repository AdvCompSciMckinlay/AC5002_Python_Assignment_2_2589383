#Library imports
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
import plotly.express as px
import pandas as pd
import matplotlib.image as img 
import csv
import re


#Function to read the data from the csv file
def importCSV():
    #Remove the cap that panda has on csv files
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    #Use the panda library to read the csv file and then save the lat and lon to seperate variables
    CSVPanda = pd.read_csv("GrowLocations.csv")
    CSVLat = CSVPanda["Latitude"]
    CSVLon = CSVPanda["Longitude"]
    getLonAndLat(CSVLon, CSVLat)


#Function to get the longitude and latitude of the plots and store them in a list
def getLonAndLat(CSVLon,CSVLat):
    plotLongitude = []
    plotLatitude = []
    counter = 0
    for i in CSVLon:
        lonPoint = float(CSVLon[counter])
        latPoint = float(CSVLat[counter])
        #Since there are some errors within the column, swap the lat and lon values with each other if the two have been mixed up in the data set
        if lonPoint > latPoint:
            tempLat = latPoint
            tempLon = lonPoint
            latPoint = tempLon
            lonPoint = tempLat
        if(lonPoint != 0 and latPoint != 0):
            if (lonPoint > -10.592 and lonPoint < 1.6848 and latPoint > 50.681 and latPoint < 57.985):
                plotLongitude.append(lonPoint)
                plotLatitude.append(latPoint)
        counter += 1
    plotMap(plotLongitude,plotLatitude)


#Function to plot the map
def plotMap(plotLongitude, plotLatitude):
    plotCounter = 0
    #Get the map
    mapImage = img.imread('map7.png')
    #Plot the data on map
    print (len(plotLatitude))
    plt.imshow(mapImage, extent=[-10.592,1.6848,50.681,57.985])
    plt.scatter(plotLongitude,plotLatitude)
    print(plotLatitude)
    print(plotLongitude)
    plt.show()

#Main function that is ran when program starts
def main():
    importCSV()
    





#Run main on program start
if __name__ == "__main__":
    main()

