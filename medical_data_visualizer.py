import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
# column : id,age,sex,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active,cardio

# Add 'overweight' column
#Calculation BMI = weight(kg)/(heigth(m))**2
bmi = df['weight'] / (df['height']/100)**2
# Judge overweight from BMI
bmi_bool = (bmi > 25)
# Convert the bool to 0,1 as int
df['overweight'] = bmi_bool.astype(int)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# if value = 1 mean 0 , value > 1 mean 1
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)



# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars= ['cardio'],value_vars= ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])
    #pd.melt(df, id_vars =['Name'], value_vars =['Course'])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable",y="total",hue="value",data=df_cat,col="cardio",kind="bar").fig


    # Get the figure for the output

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    mask1 = (df['ap_lo'] <= df['ap_hi'])
    mask2 = (df['height'] >= df['height'].quantile(0.025))
    #height is more than the 97.5th percentile <<<< incorrect data
    mask3 = (df['height'] <= df['height'].quantile(0.975))  #<<< keep correct
    #weight is less than the 2.5th percentile <<<<<< incorrect data
    mask4 = (df['weight'] >= df['weight'].quantile(0.025)) #<<< keep greater than
    #weight is more than the 97.5th percentile <<<<<< incorrect data
    mask5 = (df['weight'] <= df['weight'].quantile(0.975))
    #combind boolen
    df_heat = df[(mask1) & (mask2) & (mask3) & (mask4) & (mask5)]

    # Calculate the correlation matrix
    corr =  df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True


    # Set up the matplotlib figure
    with sns.axes_style("white"):
        fig, ax = plt.subplots(figsize=(7, 5))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, vmax=.32, square=True,annot=True,vmin=-0.16,annot_kws={"size":5},fmt='.1f')


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
