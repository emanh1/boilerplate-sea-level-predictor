import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    slope, intercept = res.slope, res.intercept
    x = pd.Series(range(df['Year'].min(), 2051)) 
    y_reg = x*slope + intercept
    plt.plot(x, y_reg, label='All data')
    # Create second line of best fit
    dfrecent = df[df['Year'].astype(int) >= 2000]
    res = linregress(dfrecent['Year'], dfrecent['CSIRO Adjusted Sea Level'])
    slope, intercept = res.slope, res.intercept
    x2 = pd.Series(range(dfrecent['Year'].min(), 2051))
    y_reg = x2*slope + intercept
    plt.plot(x2, y_reg, label='Recent ')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.xlim(1850, 2075)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()