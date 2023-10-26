"""Answer the Research questions from Dataset"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

class inference:
    """Class for providing graphical visualization of research questions."""
    
    def __init__(self, df):
        """inference has a `pandas.DataFrame` object as an attribute."""
        self.data = df
    
    def matplt_seabrn_inf1(self):
        """
    Perform a one-way ANOVA test and visualize the data using box plots with Matplotlib and Seaborn.

    Parameters:
        None

    Returns:
        None

    Description:
        This function conducts a one-way ANOVA test to determine if there is a statistically significant difference in engagement
        scores between different engagement categories.

        The function then visualizes the data using box plots with Matplotlib and Seaborn, allowing you to compare the distribution
        of engagement scores across different categories.

        - The first box plot is created using Matplotlib, showing engagement scores for each category.
        - The second box plot is created using Seaborn, providing a similar visualization with Seaborn's styling.

        The function also displays the result of the one-way ANOVA test, indicating whether there is a statistically significant
        difference in engagement between categories based on the p-value.

    Usage:
        To use this function, call it with no arguments as follows:
        
        matplt_seabrn_inf1() in jupyter lab
    """
        # Perform one-way ANOVA test
        f_statistic, p_value = f_oneway(*[self.data[self.data['ENGAGEMENT_CATEGORY'] == category]['CITYWIDE_COUNT'] for category in self.data['ENGAGEMENT_CATEGORY'].unique()])

        # Visualize the data
        plt.figure(figsize=(10, 6))

        # Box plot using Matplotlib
        plt.subplot(1, 2, 1)
        data = [self.data[self.data['ENGAGEMENT_CATEGORY'] == category]['CITYWIDE_COUNT'].values for category in self.data['ENGAGEMENT_CATEGORY'].unique()]
        plt.boxplot(data)
        plt.xlabel('Category')
        plt.ylabel('citywide')
        plt.title('Box Plot of Engagement Score by citywide (Matplotlib)')
        
        
        # Box plot using Seaborn
        plt.subplot(1, 2, 2)
        sns.boxplot(x='ENGAGEMENT_CATEGORY', y='CITYWIDE_COUNT', data=self.data)
        plt.xlabel('Category')
        plt.ylabel('citywide')
        plt.title('Box Plot of Engagement Score by citywide (Seaborn)')

        plt.tight_layout()

        # Interpretation
        if p_value < 0.05:
            print("The p-value is", p_value, "which is less than 0.05. Therefore, there is a statistically significant difference in engagement between citywide.")
        else:
            print("The p-value is", p_value, "which is greater than 0.05. Therefore, there is no statistically significant difference in engagement between citywide.")
            
        return plt.show()

   
    def matplt_inf2(self):
        """
    Create a horizontal bar plot to visualize the distribution of age groups within the 'EMPLOYMENT-BUDGETED' as engagement category.

    This function filters the dataset to select only the entries where 'ENGAGEMENT_CATEGORY' is 'EMPLOYMENT-BUDGETED',
    and then creates a horizontal bar plot to show the distribution of age groups in that category.

    Returns:
        None: The function displays the plot but does not return any values.
     
        """
        # Filter the dataset for entries where 'ENGAGEMENT_CATEGORY' is 'EMPLOYMENT-BUDGETED'
        employment_data = self.data[self.data['ENGAGEMENT_CATEGORY'] == 'EMPLOYMENT-BUDGETED']

        # Create a horizontal bar plot using Matplotlib
        plt.figure(figsize=(10, 8))
        plt.barh(employment_data['AGE_GROUP'], employment_data['CITYWIDE_COUNT'], color='purple')  # Use a color similar to Seaborn
        plt.xlabel('Count')
        plt.ylabel('Age Group')
        plt.title('Distribution of Age Groups in EMPLOYMENT-BUDGETED (Matplotlib)')
        return plt.show()
    

    def seabrn_inf2(self):
        """
    Create a horizontal bar plot using Seaborn to visualize the distribution of age groups within the 'EMPLOYMENT-BUDGETED' engagement category.

    Parameters:
        None

    Returns:
        None

    Description:
        This function filters the dataset to select only the entries where 'ENGAGEMENT_CATEGORY' is 'EMPLOYMENT-BUDGETED'.
        It then creates a horizontal bar plot using Seaborn to display the distribution of age groups in that category.

        The Seaborn plot is styled with a white grid background and a 'viridis' color palette, making it visually appealing.

    Usage:
        To use this function, call it with no arguments as follows:
        
        seaborn_inf2()
       """
        # Filter the dataset for entries where 'ENGAGEMENT_CATEGORY' is 'EMPLOYMENT-BUDGETED'
        employment_data = self.data[self.data['ENGAGEMENT_CATEGORY'] == 'EMPLOYMENT-BUDGETED']

        # Create a horizontal bar plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")  # Set a white grid background
        sns.barplot(data=employment_data, y='AGE_GROUP', x='CITYWIDE_COUNT', palette='viridis')
        plt.xlabel('Count')
        plt.ylabel('Age Group')
        plt.title('Distribution of Age Groups in EMPLOYMENT-BUDGETED (Seaborn)')
        plt.show()
        
    def matplt_seabrn_inf3(self):
        
        """
    Generate time series line plots to visualize the evolution of youth engagement by age group over time.

    Parameters:
        None

    Returns:
        None

    Description:
        This function filters the dataset for relevant columns ('REPORT_DATE', 'AGE_GROUP', 'CITYWIDE_COUNT'). 
        It then groups the data by 'REPORT_DATE' and 'AGE_GROUP', calculating the sum of 'CITYWIDE_COUNT' for each group.
        The results are stored in the grouped_data DataFrame and data is reset to ensure proper indexing.

        The function displays the time series line plots using Matplotlib and Seaborn to show the evolution of youth engagement
        by age group over time. It creates separate line plots for each age group with different colors and provides a legend for
        clarity.

        - The Matplotlib plot shows time series line plots for each age group.
        - The Seaborn plot displays the same information using Seaborn's styling with a different color palette.
        """
        # Filter the dataset for relevant columns
        relevant_columns = ['REPORT_DATE', 'AGE_GROUP', 'CITYWIDE_COUNT']
        filtered_data = self.data[relevant_columns]

        # Group the data by REPORT_DATE and AGE_GROUP and calculate the sum of CITYWIDE_COUNT
        grouped_data = filtered_data.groupby(['REPORT_DATE', 'AGE_GROUP']).sum().reset_index()

        # Create a time series line plot using Matplotlib
        plt.figure(figsize=(12, 8))
        age_groups = grouped_data['AGE_GROUP'].unique()

        for age_group in age_groups:
            age_group_data = grouped_data[grouped_data['AGE_GROUP'] == age_group]
            plt.plot(age_group_data['REPORT_DATE'], age_group_data['CITYWIDE_COUNT'], label=f'Age Group {age_group}')

        plt.xlabel('Report Date')
        plt.ylabel('Total Engagement Count')
        plt.title('Evolution of Youth Engagement by Age Group Over Time (Matplotlib)')
        plt.legend()
        plt.show()

        # Create a Seaborn time series line plot
        plt.figure(figsize=(12, 8))
        sns.set_style("whitegrid")
        sns.lineplot(data=grouped_data, x='REPORT_DATE', y='CITYWIDE_COUNT', hue='AGE_GROUP', palette='husl')
        plt.xlabel('Report Date')
        plt.ylabel('Total Engagement Count')
        plt.title('Evolution of Youth Engagement by Age Group Over Time (Seaborn)')
        plt.legend(title='Age Group')
        return plt.show()


