# Medical Data Visualizer

This is the boilerplate for the Medical Data Visualizer project. Instructions for building your project can be found at [https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer)  

---

## Task

- [X] Add an overweight column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight.  
  - [X] Use the value 0 for NOT overweight and the value 1 for overweight.
- [X] Normalize the data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, make the value 0. If the value is more than 1, make the value 1.  
- [X] Convert the data into long format and create a chart that shows the value counts of the categorical features using seaborn's catplot(). The dataset should be split by 'Cardio' so there is one chart for each cardio value. The chart should look like **examples/Figure_1.png**

![examples/Figure_1.png.](examples/Figure_1.png)

- [X] Clean the data. Filter out the following patient segments that represent incorrect data:
  - [X] diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
  - [X] height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
  - [X] height is more than the 97.5th percentile
  - [X] weight is less than the 2.5th percentile
  - [X] weight is more than the 97.5th percentile
- [X] Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's heatmap(). Mask the upper triangle. The chart should look like **examples/Figure_2.png.**

![examples/Figure_2.png.](examples/Figure_2.png)

## Result

---  

### catplot

![catplot.png](catplot.png)

### heatmap

![heatmap.png](heatmap.png)  
