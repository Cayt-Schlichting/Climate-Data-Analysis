# Atmospheric CO<sub>2</sub> Trends
*Audience: The Climate Curious*


<hr style="background-color:silver;height:3px;" />

## Project Summary
<hr style="background-color:silver;height:3px;" />
The goal of this notebook is to explore atmospheric CO2 readings and perform time series forcasting to predict CO2 levels in the near future.

### Project Deliverables
> - A final report notebook
> - Python modules for automation and to facilitate project reproduction
> - Notebooks that show:
>  - Data acquisition and preparation 
>  - exploratory analysis, model creation, refinement and evaluation

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

---
### Project Plan 

- [ ] **Acquire** data from the Scripps CO$_2$ Program. 
- [ ] Clean and **prepare** data for the exploration. 
- [ ] Create utils.py to store functions I created to automate the cleaning and preparation process. 
- [ ] Split train and test subsets for exploration and modeling.
- [ ] **Explore** the data through visualizations.
    - [ ] Document findings and takeaways.
- [ ] Perform **modeling**:
   - [ ] Identify model evaluation criteria
   - [ ] Create at least three different models.
   - [ ] Evaluate models on test subset.
   - [ ] Forecast future values for atmospheric CO$_2$
- [ ] Create **Final Report** notebook with a curtailed version of the above steps.
- [ ] Create and review README. 


<hr style="background-color:silver;height:3px;" />

## Data Dictionary
<hr style="background-color:silver;height:3px;" />

|Target|Definition|
|:-------|:----------|
| co2 | Atmospheric CO$_2$ levels as recorded at the Mauna Loa Observatory and provided by the [Scripps CO$_2$ Program](https://scrippsco2.ucsd.edu/data/atmospheric_co2/mlo.html).|

<hr style="background-color:silver;height:3px;" />

## Reproducing this project
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

