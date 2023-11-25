"""Exploratory Data Analysis"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class eda:
    """Class for providing graphical visualization of dataframe."""
    
    def __init__(self, df):
        """eda has a `pandas.DataFrame` object as an attribute."""
        self.data = df
    
    def desc(self):
        """ Get the statistical details from the dataframe"""
        return self.data.describe()
    
    def matplt_bar_age_group(self):
        """
        Creating a bar plot for 'Age' using Seaborn
        
        parameter:
            age_group_counts: Count the frequency of each age group

        function:
            plt.figure to give the size of graph
            plt.barplot() to create a bar plot for age groups. The x-axis represents the age groups, and the y-axis represents frequencies of each age group.
            plt.xlabel to label the name of x-Axis
            plt.ylabel to label the name of y-Axis

        return:
            plot bar graph
        
        """
        # Count the frequency of each age group
        age_group_counts = self.data['AGE_GROUP'].value_counts()

        # Creating a bar plot
        plt.figure(figsize=(8, 6))
        age_group_counts.plot(kind='bar', color='blue', edgecolor='black')

        plt.xlabel('Age Group')
        plt.ylabel('Frequency')
        plt.title('Bar Plot of Age Groups')
        return plt.show()

        
    def seabrn_bar_age_group(self):
        """
        Creating a bar plot for 'Age' using Seaborn

        function:
             sns.countplot() to create a bar plot for age groups. The x-axis represents the age groups, and the y-axis represents the counts or frequencies of each age                    group.
        return:
            plot bar graph
            
        Description:
            - This graph shows the how many number of people in specific age group.
        """
        plt.figure(figsize=(8, 6))
        sns.countplot(data=self.data, x='AGE_GROUP', color='blue')

        plt.xlabel('Age Group')
        plt.ylabel('Frequency')
        plt.title('Bar Plot of Age Groups (Seaborn)')

        return plt.show()
    
    def matplt_bar_engagement_category(self):
        """
        Visualize Citywide Count by Engagement Category as a bar plot using Matplotlib.

        This function creates a bar chart to represent the total Citywide Count for different Engagement Categories.

        Parameters:
            - self: The class instance containing the data to be visualized. Make sure the 'data' attribute is set within the instance.

        Returns:
            None
    
        """
        # Visualize the data using Matplotlib
        plt.figure(figsize=(12, 6))

        # Plot 1: Bar plot of Citywide Count by Engagement Category
        engagement_category_counts = self.data.groupby('ENGAGEMENT_CATEGORY')['CITYWIDE_COUNT'].sum()
        engagement_category_counts.plot(kind='bar', color='skyblue')
        plt.title('Citywide Count by Engagement Category')
        plt.ylabel('Citywide Count')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility

        
        return plt.show()
    
    def seabrn_bar_engagement_category(self):
        """
        Visualize Citywide Count by Engagement Category as a bar plot using Seaborn.

        This function creates a bar chart to represent the total Citywide Count for different Engagement Categories using Seaborn, a data visualization library. It                  sets the Seaborn style, color palette, and creates the bar plot.

        Parameters:
            - self: The class instance containing the data to be visualized. Make sure the 'data' attribute is set within the instance.

        Returns:
            None

        """
        # Set Seaborn style and color palette
        sns.set(style="whitegrid")
        sns.set_palette("pastel")

        # Create a bar plot of Citywide Count by Engagement Category using Seaborn
        plt.figure(figsize=(12, 6))
        sns.barplot(x='ENGAGEMENT_CATEGORY', y='CITYWIDE_COUNT', data=self.data, color='skyblue')
        plt.title('Citywide Count by Engagement Category (Seaborn)')
        plt.xlabel('Engagement Category')
        plt.ylabel('Citywide Count')
        
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        
        return plt.show()
    
    def matplt_line_report_date(self):
        """
        Visualize the Citywide Count over time as a time series line plot using Matplotlib.

        This function creates a time series line plot to represent the changes in Citywide Count over time. It converts the 'REPORT_DATE' column to a datetime format,                 aggregates the data by date, and plots the time series.

        Parameters:
            - self: The class instance containing the data to be visualized. Make sure the 'data' attribute is set within the instance.

        Returns:
            None

        Description:

            - The function converts 'REPORT_DATE' to a datetime format, aggregates data by date, and creates a time series line plot.
            - The plot is displayed using plt.show(), and the function does not return a value.

        """

        self.data['REPORT_DATE'] = pd.to_datetime(self.data['REPORT_DATE'])
        time_series_data = self.data.groupby('REPORT_DATE')['CITYWIDE_COUNT'].sum()
        time_series_data.plot(kind='line', color='green', marker='o')
        plt.title('Citywide Count Over Time')
        plt.xlabel('Report Date')
        plt.ylabel('Citywide Count')

        plt.tight_layout()
        return plt.show()
    
    
    def seabrn_line_report_date(self):
        """
        Visualize the Citywide Count over time as a time series line plot using Seaborn.

        This function creates a time series line plot to represent the changes in Citywide Count over time using Seaborn, a data visualization library. It sets the                  Seaborn style and color palette, and then creates the line plot.

        Parameters:
            - self: The class instance containing the data to be visualized. Make sure the 'data' attribute is set within the instance.

        Returns:
            None

        Description:

            - The function sets the Seaborn style and color palette and uses Seaborn to create the line plot.
            - The plot is displayed using plt.show(), and the function does not return a value.

       """
        # Set Seaborn style and color palette
        sns.set(style="whitegrid")

        # Create a line plot of Citywide Count over time using Seaborn
        plt.figure(figsize=(12, 6))
        sns.lineplot(x='REPORT_DATE', y='CITYWIDE_COUNT', data=self.data, color='green', marker='o')
        plt.title('Citywide Count Over Time (Seaborn)')
        plt.xlabel('Report Date')
        plt.ylabel('Citywide Count')

        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        
        plt.tight_layout()
        return plt.show()