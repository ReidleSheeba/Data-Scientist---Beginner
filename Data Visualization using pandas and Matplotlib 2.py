#!/usr/bin/env python
# coding: utf-8

# ## Data Visualization using Pnadas and Matplotlib

# - Matplotlib is the most popular visualization lirary in Python
# - There are 2 key components in a Plot (see the image Matplotlib)
#     - 1) Figure
#         -  The "Figure" is the top level container that act as a windowor page on which Everything is drawn.
#         - It contains:
#             - multiple independent figures
#             - multiple Axes
#             - A subtitle (which is a centered title for the Figure)
#             - A Legend
#             - A Color bar etc.
#     - 2) Axes
#         - This is where we plot our data and any lables/ticks associated with it.
#         - Each Axes has an X-Axis and Y- Axis 

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


import matplotlib.image as mpimg
plt.imshow(mpimg.imread('Matplotlib.png'))


# ## There are 2 approaches for creating the plots
# - 1) Functional Approach
# - 2) Object Oriented Interface

# ## Functional Approach

# In[3]:


# using 2 Numpy Arrays lets Plot.
import numpy as np

x = np.linspace(0, 10, 20) # Generating 20 datapoints in b/w '0' to '10'
y = x**2                   # Generating Array 'y' from the square root of 'x'


# In[4]:


plt.plot(x,y);

#or
#plt.show() #while using Matplotlib within a python script.


# In[5]:


# let's
# name the x-axis, y-axis and adding the title
# Using ".xlabel()", ".ylabel()", ".title()"
plt.plot(x,y)
plt.title('its title here')
plt.xlabel('name  of the x axis')
plt.ylabel('name of the y axis')


# #### subplot using .subplot()

# - with ".subplot()", we can have more than 1 plot on the canvas
# - The ".subplot()" takes in 3 parameters
#     - "nrows" = the no.of rows in the figure
#     - "ncols" = the no.of columns in the figure
#     - "plot_number" = which reffers to a specific plot in the figure

# In[6]:


#plt.subplot(nrows, ncols, plot_number)
plt.subplot(1,3,1)
plt.plot(x, y, 'red')

plt.subplot(1, 3, 2)
plt.plot(x, y, 'green')

plt.subplot(1, 3, 3)
plt.plot(x, y, 'blue')


# ## Object Oriented Interface
# - The idea is to create "figure objects" and call methods of it.

# In[7]:


# create a blank figure using .figure() method.
fig = plt.figure()


# - now we need to add set of axes into it using ".add_axes" method
# - This method takes ina list of 4 arguments (left, bottom, width, height) ranging from '0' to '1'

# In[8]:


ax = fig.add_axes([0.1,0.2,0.8,0.9]) # the blank set of axes is created


# In[9]:


# now plot the 'x' and 'y' arrays into it.
ax.plot(x, y, 'red')


# - using ".set_xlabel()", "set_ylabel()", "set_title()", we can-

# In[10]:


fig = plt.figure()
ax = fig.add_axes([0.1,0.2,0.8,0.9])
ax.plot(x, y, 'red')
ax.set_title(" plot by the object oriented approach")
ax.set_xlabel("name of the x-axis")
ax.set_ylabel("name of the y-axis")


# - Remember, a "figure" can contain multiple figures, so

# In[11]:


# putting 2 sets of figure into 1 canvas
fig = plt.figure()

ax1 = fig.add_axes([0.1,0.2,0.8,0.9])
ax2 = fig.add_axes([0.2,0.5,0.4,0.3])


# - plot x and y arrays on the plots created

# In[12]:


fig = plt.figure()
ax1 = fig.add_axes([0.1,0.2,0.8,0.9])
ax2 = fig.add_axes([0.2,0.5,0.4,0.3])
ax1.plot(x,y)
ax1.set_title("the outer plot")
ax1.set_xlabel("the outer plot x-axis")
ax1.set_ylabel("the outer plot y-axis")
ax2.plot(y,x)
ax2.set_title("the plot in the plot")
ax2.set_xlabel("in plot x-axis")
ax2.set_ylabel("in plot y-axis")


# #### subplots using   .subplots()

# - creating multiple plots in the object-oriented approach using the .subplots()
# - not .subplot()
# - the .subplots() method takes in "nrows" - the no.of rows a figure shouls have 
# - and "ncols" - the no.of columns the figure should have

# In[13]:


# creating a 3x3 subplot

fig, axes = plt.subplots(nrows = 3, ncols = 3)
plt.tight_layout()


# In[14]:


# plot x, y on the axes at index position (0,1) and y, x on the axes at position (1,2)

fig, ax = plt.subplots(nrows = 3, ncols = 3)

ax[0,1].plot(x,y)
ax[1,2].plot(y,x)

ax[0,0].set_title("title 0x0")
ax[0,1].set_xlabel("x-axis 0x1")
ax[0,2].set_ylabel("y-axis 0x2")


plt.tight_layout()


# ## Figure size, aspect ratio, and DPI
# - The figsize is a tuple of the width and height of the figure (in inches), and dpi is the dots-per-inch (pixel-per-inch).

# In[15]:


fig = plt.figure(figsize = (8,2), dpi = 100)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)


# #### with .subplots()

# In[16]:


fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (8,2), dpi = 100)
ax[0].plot(x,y)
ax[1].plot(y,x)

plt.tight_layout()


# ## Save Figure using ".savefig()"

# In[17]:


fig.savefig('saved figure.png')


# In[18]:


#confirm the image by displaying it using:

import matplotlib.image as mpimg
plt.imshow(mpimg.imread('saved figure.png'))


# ## Legends
# - it allows to distinguish b/n plots
# - using .legend() and then specify the label=” ” attribute for each plot

# In[19]:


fig = plt.figure(figsize = (8,4), dpi = 60)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label = "x square plot")
ax.plot(x,x**3, 'red', label = "x cube plot")

ax.legend()


# In[20]:


fig, ax =plt.subplots(nrows=2, ncols=1, figsize =(12,4), dpi = 60)

ax[0].plot(x,x**2, label="x square plot")
ax[0].plot(x,x**3, label ="x cube plot")

ax[1].plot(x,x**1, label = "1")
ax[1].plot(x,x**2, label = "2")
ax[1].plot(x,x**3, label = "3")

ax[0].legend()
ax[1].legend()
plt.tight_layout()


# now lets move on to
# - linewidth-lw- of 3,  linestyle-ls- to be double dashes, map out our datapoints using ‘o’ and the markersize of 8

# In[21]:


fig = plt.figure(figsize = (8,2), dpi = 60)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y, color = 'red', lw = 3, ls = '--', marker = 'o', markersize = 8)


# ## Plot Range

# - configuring the range of our plots using the "set_ylim" and "set_xlim" methods of the axis object, or axis(‘tight’) to automatically get “tightly fitted” axes ranges. 
# 
# - For example, we can choose to show only plots between 0 to 1 of the x axis, and 0 to 5 of the y axis

# In[22]:


fig = plt.figure(figsize = (8,2), dpi = 60)
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)

ax.set_xlim([0,20]) # signifies the lower bound and the upper bound of the x-axis
ax.set_ylim([0,10]) # signifies the lower bound and the upper bound of the y-axis


# ## Plot Types
# - based on the purpose of viualization

# ### Histograms: 
# - to understand the distribution of a numeric value in a way that you cannot with mean or median alone.
# - Using .hist() method, we can create a simple histogram

# In[23]:


x = np.random.randn(1000)
plt.hist(x);


# ## Time series (Line Plot):
# - to show trends over a period of time. 
# - It allows you to test various hypotheses under certain conditions, like what happens different days of the week or between different times of the day

# In[24]:


import datetime
x = np.array([datetime.datetime(1999,9,11,i,0)for i in range (12)])
y = np.random.randint(50, size = x.shape)
plt.plot(x,y)


# ## Scatter plots 
# - to visualize how two numeric values are related in the data. 
# - to understand thr relationships between multiple variables. 
# - Using .scatter() method, we can create a scatter plot

# In[25]:


fig, ax = plt.subplots()
x = np.linspace(-1, 1, 50)
y = np.random.randn(50)
ax.scatter(x,y)


# In[26]:


fig = plt.figure(figsize = (8,2), dpi = 100)
ax = fig.add_axes([0,0,1,1])
ax.scatter(x,y, color = 'red')


# ## Bar graphs 
# - for comparing numeric values of several groups. 
# - Using .bar() method, we can create a bar graph:

# In[27]:


my_df = pd.DataFrame(np.random.rand(10,4), columns = ['a', 'b', 'c', 'd'])

my_df.plot(kind = 'barh', figsize = (8,6));


# # let's look into  real world example

# - to find the richest country in the world on a per-person basis.
# 
# - nations.csv Data from the World Bank Indicators portal, which is an incredibly rich resource. Contains the following fields:
#     - iso2c, iso3c ::: Two- and Three-letter codes for each country, assigned by the International Organization for Standardization.
#     - country ::: Country name.
#     - year
#     - population ::: Estimated total population at mid-year, including all residents apart from refugees.
#     - gdp_percap ::: Gross Domestic Product per capita in current international dollars, corrected for purchasing power in different territories.
#     - life_expect ::: Life expectancy at birth, in years.
#     - population ::: Estimated total population at mid-year, including all residents apart from refugees.
#     - birth_rate ::: Live births during the year per 1,000 people, based on mid-year population estimate.
#     - neonat_mortal_rate :::Neonatal mortality rate: babies dying before reaching 28 days of age, per 1,000 live births in a given year.
#     - region, income ::: World Bank regions and income groups.
# 
# Lets, compare different country’s gdp per capita by :
#     - First, we will import all necessary packages.
#     - Load our dataset.
#     - Clean the dataset by filling in missing values.
#     - Aggregate values using .groupby().
#     - Sort the values.
#     - Represent our data in either line or bar plot

# In[28]:


# we already have imported the  necessary packages

#import matplotlib.pyplot as plt
#import pandas as pd


# In[29]:


df = pd.read_csv("nations.csv")
df.head(5)


# In[30]:


df.tail()


# In[31]:


df.shape


# In[32]:


df.info()


# In[33]:


df.isnull().sum()


# In[34]:


# In this particular example, since we are concentrating on the "gdp_percap", 
# lets start by working with the missing values in "gdp_percap".

df['gdp_percap'].fillna(df['gdp_percap'].median(), inplace = True) # replacing NaN values with "median" values of the column.
df.head()


# In[35]:


# finding he mean gdp_percap for each country 
# lets group by he column "country" and find the mean of all clumns wrt each country

df.groupby(['country']).mean()


# In[36]:


# let's narrow down to the average gdp_percap of all the available years for each country and save it in the new variable

avg_gdp_percap = df.groupby(['country']).mean()['gdp_percap']
avg_gdp_percap


# In[37]:


# sorting the top 5
top_five_countries = avg_gdp_percap.sort_values(ascending = False).head()
top_five_countries


# - United Arab Emirates has the highest avg_gdp_percap
# - lets look into detail to findout if United Arab Emirates is the most richest country in the world on a person-basis

# In[38]:


UAE = df[df['country'] == 'United Arab Emirates']
UAE


# In[39]:


# plotting the change of gdp_percap in United Arab Emirates over time.

plt.plot(UAE['year'], UAE['gdp_percap'])
plt.xlabel('Year')
plt.ylabel('GDP')
plt.title('GDP Per capita of United Arab Emirates')


# - well.... the line graph looks how it looks ;)
# - let's go for bar graph for better insights.

# In[40]:


UAE.plot.bar(x = 'year', y = 'gdp_percap', figsize = (12,6))


# - United Arab Emirates's GPD was high in the years 2003 and 2004
# - how ever its the lowest in the year 2010

# In[41]:


# plotting gdp_percap and population on the same plot using .subplot()

plt.subplot(311)
plt.bar(UAE['year'],UAE['gdp_percap'], color = 'g')
plt.title('GDP Per capita')

plt.subplot(312)
plt.bar(UAE['year'], UAE['population'] * UAE['gdp_percap']/10**9, color = 'b')
plt.title('GDP in Billions')

plt.subplot(313)
plt.bar(UAE['year'], UAE['population']/10**6, color = 'r')
plt.title("Popilation in millions")

plt.tight_layout()


# - from the above plot we can see that United Arab Emirates's GDP  droped during 2010 and its trying to pick up towards 2015 and heir population have significantly grown as well.
# 
# - However, how do we tell ow much faster their population grew relative to their GDP?
# - So, we'll compare their relative growth in a single plot by showing the population growth in the first year. Lets set the first years population to 100 as a basis of comparison, then repest the same for "gdp" and "gdp_percap".

# In[42]:


plt.bar(UAE['year'], (UAE['population']/UAE['population'].iloc[0]*100),color = 'r')

UAE_gdp = UAE['population'] * UAE['gdp_percap']
plt.bar(UAE['year'],UAE_gdp/UAE_gdp.iloc[0]/100, color = 'g')

plt.bar(UAE['year'], UAE['gdp_percap']/UAE['gdp_percap'].iloc[0]/100, color = 'b')

plt.title("GDP and Population growth in UAE (first year = 100)")
plt.legend(['population', 'GDP', 'GDP Per capita'], loc = 4)


# - as we can see at no point did UAE's gdp ever catchup with the population growth
# 
# - to further clarify the same let's compare the UAE's gdp_percap with that of another country in the "top_five_countries".
# 
# - let's try and plot the gdp_percap of both Qatar and UAE in the same chart.
# 

# In[43]:


qt = df[df['country'] == 'Qatar']

plt.bar(qt['year'], qt['gdp_percap'])
plt.bar(UAE['year'], UAE['gdp_percap'])
plt.legend(['Qatar', 'UAE'])


# - As of the year 2000 the both the countries had almost the same GDP however Qatar was edging a bit on the higher side, and eventually by 2014 Qatar has a sinificantly higher GDP than UAE.
# - Hence it can't be said that UAE has the higher gdp per capita based on a per person basis.
