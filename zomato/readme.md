# Zomato Data Analysis

This Jupyter Notebook (`zomato.ipynb`) contains an exploratory data analysis (EDA) of a Zomato restaurant dataset. The analysis aims to uncover insights related to restaurant ratings, pricing, and online ordering patterns.

## Overview of Contents:

* **Data Loading and Initial Inspection**: Loads the `Zomato-data.csv` file into a pandas DataFrame and provides an initial overview of its structure and data types.
* **Missing Value and Unique Value Check**: Identifies and counts any missing values and unique entries within each column to assess data completeness and cardinality.
* **Data Cleaning**: Includes a function (`handleRate`) to clean the 'rate' column, converting it from a string format (e.g., "4.1/5") to a numerical (float) format for analysis.
* **Visualizations**:
    * **Restaurant Type Distribution**: A count plot showing the distribution of different restaurant types listed in the dataset.
    * **Votes by Listing Type**: A line plot displaying the sum of votes for each type of restaurant listing.
    * **Rating Distribution**: Histograms (both basic and with KDE) to visualize the distribution of restaurant ratings.
    * **Online Order vs. Rate**: A box plot illustrating the relationship between online ordering availability and restaurant ratings.
    * **Approximate Cost Distribution**: A count plot showing the distribution of approximate costs for two people, with x-axis labels rotated for readability.
    * **Online Order vs. Listing Type Heatmap**: A heatmap showing the count of restaurants based on their listing type and whether they offer online ordering.

This notebook provides a foundational analysis of the Zomato dataset, offering insights into various aspects of the restaurant data. 
