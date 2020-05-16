#!/usr/bin/env python
# coding: utf-8

# Data Visualization is used to understand the significance of data by summarizing and presenting a huge amount of data in a simple and easy-to-understand format and helps communicate information clearly and effectively.

# # Data Visualization using Pandas and Matplotlib
# - Pandas have built-in capabilities for data visualization. It’s built-off of matplotlib, and it's merged into pandas for easier usage.

# In[1]:


# importing necessary libraries and data files.
import numpy as np
import pandas as pd
import matplotlib as plt
# need to set backend of matplotlib to to in line to view visuals in jupyter notebook.
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# the data is kindf faked for the illustrative purpose however 
# in the later part we'll be visualizing with genuine datasets as well.

df1 = pd.read_csv('df1.csv', index_col = 0)
df2 = pd.read_csv('df2.csv')


# In[3]:


df1.head()


# In[4]:


df2.head()


# ## Style Sheets
# - Style Sheets can be used to make the plot a little nicer.
# - it includes :
#     - plot_bmh
#     - plot_fivethirtyeight
#     - plot_ggplot and more
#     
# As you may have guessed these are style rules that the plot follows.

# In[5]:


# Before plt.style.use() plots would look like this
df1['A'].hist();


# In[6]:


# now let's see how the plot looks like with some of the "style sheets"
# for that we have to import matplotlib as plt

plt.style.use('bmh')
df1['A'].hist();


# In[7]:


plt.style.use('ggplot')
df1['A'].hist();


# In[8]:


plt.style.use('fivethirtyeight')
df1['A'].hist();


# In[9]:


#plt.style.use('dark_background')
#df1['A'].hist();


# ## Plot Types
# - There are several plot types built nto Pandas and most of them are statistical by nature.
#     - df.plot.area
#     - df.plot.barh
#     - df.plot.density
#     - df.plot.hist
#     - df.plot.line
#     - df.plot.bar
#     - df.plot.box
#     - df.plot.scatter
#     - df.plot.hexbin
#     - df.plot.kde
#     - df.plot.pie
#     
# we can call df.plot(kind = 'hist') or replace the kind argument with any of the other key terms.

# ## Area
# - it displays graphically quantitative data.
# - it is based on the line chart.
# - the area between the line and the axis are commonly emphasised with colours, textures and hatchings.
# - used compare two or more quantities with an area chart

# In[10]:


df2.plot.area(figsize = (10,4));


# ## Boxplots
# - A bar chart or bar graph is a chart or graph that represents the categorical data with rectangular bars with heights or lengths which are proportional to the values they represent.

# In[11]:


df2.plot.bar(figsize = (10,4));


# In[12]:


df2.plot.bar(stacked = True, figsize = (10,4));


# ## Histograms
# - shows the underlying frequency distribution(shape) of continuous set of data
# - eg:
#     - normal distribution
#     - outliers
#     - skewness etc.

# In[13]:


df1['A'].plot.hist(bins = 50, figsize = (10,4));


# ## Line Plots
# - shows the frequency of a data along a number line.
# - best use case - time series data

# In[14]:


df1.plot.line( y = 'A', lw = 1, figsize = (10,4));


# ## Scatter Plot
# - used to show the relationship b/w 2 variables
# - also called as correlation plots coz they show how two variables are correlated.

# In[15]:


df1.plot.scatter(x = 'A', y = 'B', c = 'r', cmap = 'coolwarm');


# In[16]:


# use s to indicate size based off another column
# s parameter needs to be an array, not just the name of a column
df1.plot.scatter(x = 'A', y = 'B', c = 'r', cmap = 'coolwarm', s = df1['C']*100);


# ## Box Plots
# - a plot in which a rectngle is drawn to represent the seond and third quartile
# - a vertical line inside the rectangle is used to show the median value
# - the lower and upper quartiles are shown as horizontal lines on either side of the rectangle
# 
# 
# - it shows the distribution of the data in 5 number summary
#     - minimum
#     - first quatrile(q1)
#     - median
#     - third quartile(q3)
#     - maximum
#     
# - used to detect the outliers and wot their values are.
# - can also say:
#     - if the data is symmetrical
#     - how tightly the data is grouped
#     - how the data is skewed

# In[17]:


df2.plot.box();


# ## Hexagonl Bin Plots
# - used to manage when the ponts start to overlap
# - it plots density raher than points
# - points are binned into gridded hexagons and distribution(the number of points per hexagon) is displaye using either the colour or the area of the hexagon.
# - useful for bivariate data
# - alternate for Scatter plot

# In[18]:


df = pd.DataFrame(np.random.randn(1000,2), columns = ['a', 'b'])
df.plot.hexbin(x = 'a', y = 'b', gridsize = 25, cmap = 'Oranges');


# ## Kernel Density Estimation Plot (KDE)
# - To create a smoot curve to visualize the shape of the data
# - as a continuous replacement for the discrete histogram

# In[19]:


df2['b'].plot.kde();


# In[20]:


df2.plot.density();

