# Atmospheric CO<sub>2</sub> Trends
*Audience: The Climate Curious*


<hr style="background-color:silver;height:3px;" />

## Project Summary
<hr style="background-color:silver;height:3px;" />
The goal of this notebook is to explore atmospheric CO$_2$ readings and perform time series forcasting to predict CO2 levels in the near future. I will be using CO$_2$ readings from the Mauna Lao Observatory in Hawaii, which has the longest, directly-measured record of atmospheric CO$_2$ readings.
<br /><br />
I encourage reading the rest of this - especially if you plan to run the code yourself!  However, if you're just looking for the highlights, feel free to <a href="https://github.com/Cayt-Schlichting/Climate-Data-Analysis/blob/main/CO2_Basics/Final_Report.ipynb">jump right in to the report</a>.


### Background

**Carbon Dioxide (CO$_2$)** is a naturally occuring gas that exists in the earth's atmosphere.  Its concentration in the atmosphere is measured in "parts per million" or ppm.  There are many natural processes through which carbon dioxide enters and leaves the atmosphere.  Some common processes are through the breathing of animals and photosynthesis from plant life.  Carbon dioxide is an important part of our Earth's system as it is one of a subset of gases in our atmosphere that block outgoing heat - in the form of radiation.  This essentially bounces back heat that would normally radiate into space, creating a **greenhouse effect** that makes the Earth warm enough for us to live.

However, this is one of the cases where there can be **too much of a good thing**. As CO$_2$ is added to the atmosphere, the greenhouse effect increases, causing the average surface temperature of the earth to increase.  The sharp increase in CO$_2$ levels over the past century have been predominantly caused by humans.  In particular, our use of fossil fuels takes carbon that was stored deep in the earth's crust and releases it in the form of CO$_2$.   Reducing our CO$_2$ emissions (along with other greenhouse gas emissions) is crucial to preventing **climate degradation** - more commonly referred to as climate change or global warming.  


### Project Deliverables
> - A final report notebook
> - Python modules for automation and to facilitate project reproduction
> - Notebooks that show:
>   - Data acquisition and preparation 
>   - exploratory analysis, model creation, refinement and evaluation

### Initial questions on the data

>  - How have atmospheric CO$_2$ levels changed over time?
>  - What does the seasonal cycle of atmospheric CO$_2$ look like?
>  - How does a seasonal decomposition with statsmodel compare with other methods of pulling the seasonal cycle?
>  - Is there a trend in atmospheric CO$_2$ levels?

### Discoveries
> - The last 40 years of atmospheric CO$_2$ readings show a clear upward trend
> - There is a distinct seasonal pattern in the CO$_2$ readings, with a peak at the end of Spring and a trough in the Fall.  Annual readings can vary by 6 ppm
> - Modeling the time series, I was able to forecast 10 years with an rmse of 4 ppm.  Given that the error grew the farther the data was projected out, I extrapolated an error rate to be used on the future dataset.
> - Forecasting 15 years into the future, my model predicts that Earth will reach over 450 ppm by 2037.

<hr style="background-color:silver;height:3px;" />

## Data Dictionary
<hr style="background-color:silver;height:3px;" />

|Variable|Definition|
|:-------|:----------|
| co2 | Atmospheric CO$_2$ levels as recorded at the Mauna Loa Observatory and provided by the [Scripps CO2 Program](https://scrippsco2.ucsd.edu/data/atmospheric_co2/mlo.html).|
|mn|Month: either in '01,02,03' or 'Jan,Feb,Mar' format|
|yr|Year: YYYY format|

<hr style="background-color:silver;height:3px;" />

## References
<hr style="background-color:silver;height:3px;" />

- C. D. Keeling, S. C. Piper, R. B. Bacastow, M. Wahlen, T. P. Whorf, M. Heimann, and H. A. Meijer, Exchanges of atmospheric CO2 and 13CO2 with the terrestrial biosphere and oceans from 1978 to 2000. I. Global aspects, SIO Reference Series, No. 01-06, Scripps Institution of Oceanography, San Diego, 88 pages, 2001.
- [NASA's earth observatory website](https://earthobservatory.nasa.gov/world-of-change/global-temperatures)
- [IPCC's Global Climate Projections](https://www.ipcc.ch/site/assets/uploads/2018/02/ar4-wg1-chapter10-1.pdf)

<hr style="background-color:silver;height:3px;" />

## Reproducing this project
<hr style="background-color:silver;height:3px;" />

> In order to reproduce this project you will need to:
> - Read this README
> - Clone the repository or download all files into your working directory
> - Run the Final_Report notebook or explore the other notebooks for greater insight into the project.


---

### Project Plan 

<details>
  <summary><i>Click to expand</i></summary>
  <ul>
    <li><b>Acquire</b> data from the Scripps CO<sub>_2</sub> Program.</li>
    <li>Clean and <b>prepare</b>data for the exploration. </li>
    <li>Create utils.py to store functions I created to automate the cleaning and preparation process.</li>
    <li>Split train and test subsets for exploration and modeling.</li>
    <li><b>Explore</b> the data through visualizations; Document findings and takeaways.</li>
    <li>Perform <b>modeling</b>:
    <ul>
        <li>Identify model evaluation criteria</li>
        <li>Create at least three different models.</li>
        <li>Evaluate models on test subset.</li>
        <li>Forecast future values for atmospheric CO<sub>2</sub></li>
    </ul>
    </li>
    <li>Create <b>Final Report</b> notebook with a curtailed version of the above steps.</li>
    <li>Create and review README. </li>
    
  </ul>
</details