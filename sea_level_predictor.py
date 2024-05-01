import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', index_col= 0)
    df
    
    # Create scatter plot
    plt.figure(figsize= (12,12))
    x = df.index
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)

    # Create first line of best fit
    fit1 = linregress(x,y)
    y_fit = fit1.intercept + fit1.slope * x
    
    plt.scatter(x,y, color = 'blue')
    plt.plot(x, y_fit, 'r')

    # Create second line of best fit
    DfMask = df.index >= 2000
    RecentDf = df[DfMask]
    
    x1 = RecentDf.index    
    y1 = RecentDf['CSIRO Adjusted Sea Level']
    fit2 = linregress(x1, y1)
    
    # list range from 2000 to 2050
    x2 = list(range(2000,2051))
    x2 =pd.Series(x2)
    
    #develop prediction line
    yPred = fit2.intercept + fit2.slope * x2
    yPred
    
    #plot data, fit line  from dataset, and prediction line from 2000-2050
    plt.scatter(x,y, color = 'blue')
    plt.plot(x, y_fit, 'r')
    plt.plot(x2, yPred, 'g')
    


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.show()
        
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()