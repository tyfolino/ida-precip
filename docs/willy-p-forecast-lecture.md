---
marp: true
theme: cybertopia
class: invert

footer: 'Meteorology Guest Lecture, William Paterson University, March 2025'
paginate: true

---
<!-- <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 50vh; text-align: center;"> -->

# How to Become a Forecaster in an Hour ☁️🌡️
By: Ty Janoski, Ph.D.
City College of New York \& NOAA National Severe Storms Laboratory
March 26<sup>th</sup>, 2025

---

## A bit about myself...
- Born \& raised in Wayne
- Always been interested in the weather
- Originally wanted to be a TV meteorologist

**Two events in high school sealed the deal for me**

---

### \#1: Hurricane Irene

<!-- footer: "" -->

![bg left:40%](willy-p-figs/irene-rainfall-map.gif)

- August 28-29, 2011
- Wayne got \> 10" of rain
- Record-breaking Passaic river flooding

<div style="text-align: center;">
  <img src="willy-p-figs/willowbrook-irene.jpg" style="width:70%;"/>
  <p style="font-size: 18px;">Willowbrook Mall, August 2011</p>
</div>

---

### \#2: Hurricane Sandy

![bg right:40%](willy-p-figs/sandy_winds.png)

- Unique "left hook" into NJ
- Power outages for weeks
- Up to 9 feet storm surge in NJ

---

## Academic Journey: Undergrad
- B.S. in **meteorology** and **marine science** at Rutgers (2017)
- Started as an undergraduate research assistant with a professor
  - Collaborated with NOAA lab in Princeton
- Meteorology ➡️ Climate Science? 🤔

---

### Undergraduate research: Snowfall changes with increasing CO<sub>2</sub>

<img src="willy-p-figs/janoski-et-al-2018.png" width=65%>

---

## Academic Journey: Graduate School

- Enjoyed doing research, so Ph.D. was next step
- Received my Ph.D. in Earth \& Environmental Sciences from Columbia University in 2024
- Graduate school is definitely **not for everyone**, but I had a great experience

---

### Ph.D. research: Polar amplification

<img src="willy-p-figs/janoski-et-al-2023.png" width=90%>

---

## Now: Postdoctoral Fellow

- At CUNY City College of New York and the NOAA National Severe Storms Laboratory (NSSL) in Norman, OK
- Studying the **extreme rainfall** from Hurricane Ida (2021) in NYC
  - NYC got **\> 4" of rain in an hour**!
- Using one of NSSL's high-resolution **forecast models**
  - We'll take a look at it later

---

### Postdoctoral Research: Hurricane Ida

<img src="willy-p-figs/Fig1-mrms-rainfall.png" width=80%>

---

# Now, let's get to the science.

---

## Fact: Forecasting is Important
- We take weather forecasts for granted
- Consider the state of affairs *before* we had weather forecast access 24/7 on our phones
- Example: Galveston Hurricane of 1900
  - **Deadliest natural disaster in US History**
  - 6,000 - 12,000 fatalities
  - Forecast that day: "Rain Saturday, with high northerly winds; Sunday rain, followed by clearing."

---

## Galveston Hurricane Aftermath

<img src="willy-p-figs/galveston-hurricane.jpg" width=80%>

---

## Forecasting basics
The modern challenge: **so much data**. How do we make sense of it all?

<img src="forecast-diagram.jpg" width=45%%>

---

## Learning Objectives

**By the end of this lecture, you will be able to:**
- Access and interpret some of the most common observational data in meteorology
- Understand how weather models use this data to generate a forecast simulation
- Have the tools to create your own weather forecast

---

# Part 1: Observations

---

## Radar

- Radar stands for **Ra**dio **D**etection **A**nd **R**anging
- Useful for finding **precipitation**
- Real-time data with **high spatial and temporal resolution**

![bg left:55%](willy-p-figs/ida-radar-loop.gif)

---

## Radar Basics

1. Radar sends out a pulse of energy
2. Energy bounces off objects in atmosphere and returns to radar
3. Radar detects the **strength** and **timing** of return

---

<div style="text-align: center;">
  <img src="doppler_ani.gif" style="width:90%;"/>
  <p style="font-size: 14px;">Source: NOAA</p>
</div>

Keep in mind: the radar is rotating at different angles to sample the whole sky!

---

## Key Radar Quantities
- Three important quantities from radar:
    - **Reflectivity**: How much energy is bouncing back to the radar
    - **Time delay**: How long it takes for the energy to bounce back
        - **Shorter time delay = closer to the radar**
    - **Elevation angle**: The angle at which the radar is pointing
        - **⬇️ elevation angle = closer to the ground**

---

<div style="text-align: center;">
  <img src="radar-elevation-angle.png" style="width:90%;"/>
  <p style="font-size: 14px;"><em>Source: NOAA</em></p>
</div>

---

### More Radar Features:
- dual polarization to detect precipitation type ❄️☔
- doppler velocity for radar-relative motion 🌪️

<img src="willy-p-figs/dual-pol-radar.jpg" width=60%>

---

![bg right:50%](willy-p-figs/phased-array-anim.gif)

### Next generation radar: Phased Array Radars
- NWS WSR-88D radars near end of lifespan
- Likely to be replaced by PAR in 2030s
- Network of mini-antenna sending beams at once

---

## Radar resources & demo

- [NOAA NWS Radar](https://radar.weather.gov) (official site)
- [MRMS](https://mrms.nssl.noaa.gov/qvs/product_viewer/) (radar data archive \& advanced products)
- [College of DuPage](https://weather.cod.edu/satrad/) (satellite + radar together)
- [Rutgers Weather Center](https://synoptic.envsci.rutgers.edu) (great NJ radar loop)
- RadarScope app is excellent but unfortunately not free

---

## Satellite Data

---

## Satellite basics
- Take measurements of the atmosphere from space
- Weather satellites normally observe the **brightness of Earth's atmosphere** in specific wavelength bands
  - They **do not** directly measure temperature or water vapor—just radiation
- Often our *only* source of data in remote parts of the world
  
---

<div style="text-align: center;">
  <img src="satellite-paths.jpg" style="width:45%;"/>
  <p style="font-size: 14px;"><em>Source: ThoughtCo</em></p>
</div>

<div style="text-align: center;">
  <img src="geosynchronous-orbit.gif" style="width:30%;"/>
  <p style="font-size: 14px;"><em>Source: Wikimedia Commons</em></p>
</div>

---

## Question: How far away are geostationary satellites from Earth?
- A) 200 miles
- B) 2,000 miles
- C) 20,000 miles
- D) 200,000 miles

---

## Types of satellite imagery
- **Visible Imagery**: shows reflected sunlight (**day only**)
  - Great for clouds and surface features
- **Infrared (IR) Imagery**: shows cloud-top temperatures
    - Can see cloud tops and motion **day or night**
- **Water Vapor Imagery**: measures wavelengths absorbed by water vapor **day or night**
    - Great for finding cyclones, dry slots, atmospheric rivers, etc.
---

![bg left:50%](visible-satellite.gif)

## Visible imagery
**Light colors**: thick clouds, snow

 **Dark colors**: clear skies

---

<!-- ![bg right:50%](ir-satellite.gif) -->

## Infrared imagery
- Different colors = different temperatures
- Colder temps = higher clouds = red/white
- Warmer temps = lower clouds = blue/green

<div style="text-align: center;">
  <img src="ir-satellite.gif" style="width:40%;"/>
  <p style="font-size: 14px;"><em>Source: Just In Weather</em></p>
</div>

---

## Water vapor imagery
- Different colors = different moisture levels
- White, blue, and green = moist air
- Yellow, orange, and red = dry air

<div style="text-align: center;">
  <img src="wv-satellite.gif" style="width:45%;"/>
  <p style="font-size: 14px;"><em>Source: Just In Weather</em></p>
</div>

---

## Satellite Resources & Demo
- [NOAA GOES Image Viewer](https://www.star.nesdis.noaa.gov/GOES/index.php) (Official NOAA source)
- [CSU RAMMB Slider](https://rammb-slider.cira.colostate.edu) (Multiple satellite, last 20 days)
- [College of DuPage](https://weather.cod.edu/satrad/) (satellite + radar together)
- [NASA Worldview](https://worldview.earthdata.nasa.gov/) (global satellite data but hard to use tbh)

---

## Upper air observations

---

## Upper air observations basics
- Measurements taken directly from the atmosphere
- Essential for understanding vertical structure of atmosphere and predicting weather
- Collected via:
    - Weather balloons (radiosondes)
    - Aircraft

---

## Weather balloons and radiosondes
- Weather balloons carry radiosondes into the atmosphere
- Radiosondes measure:
    - Temperature
    - Humidity
    - Pressure
    - Wind speed and direction
- Data is sent back to the ground via radio

---

<div style="text-align: center;">
  <img src="weather-balloon.jpg" style="width:80%;"/>
  <p style="font-size: 14px;"><em>Source: WCNC</em></p>
</div>

---

<div style="text-align: center;">
  <img src="launch-sites.gif" style="width:70%;"/>
  <p style="font-size: 14px;"><em>Source: NWS</em></p>
</div>

---

## Reading upper air observations
- Show vertical profiles of temperature, moisture, and wind
  - **Temperature**: red line
  - **Dew point**: green line
  - **Wind speed**: barbs
  - **Wind direction**: direction **from which** wind blows
- Temperature and dew point are close = clouds (usually)!
- Temperature increases with height = inversion

---

## Example: NYC on Monday
<div style="text-align: center;">
  <img src="willy-p-figs/nyc-sounding.png" style="width:55%;"/>
  <p style="font-size: 14px;"><em>Source: College of Dupage</em></p>
</div>

---

## New York City Skyline

<img src="willy-p-figs/nyc-skyline.jpg" width=80%>

---

## Upper-air maps

Data from soundings ➡️ upper-air maps on pressure levels to show us the flow of the atmosphere

<img src="willy-p-figs/upper-air-map.gif" width=50%>

---

## Upper Air Resources \& Demo
- Soundings:
  - [NWS Storm Prediction Center](https://www.spc.noaa.gov/exper/soundings/) (Official NOAA source, tons of data)
  - [University of Wyoming](https://weather.uwyo.edu/upperair/sounding.html) (Great for past soundings)
- Upper air maps:
  - [NWS Storm Prediction Center](https://www.spc.noaa.gov/obswx/maps/) (A bit ugly)
  - [Mountain Weather](https://www.mountainweather.com/weather-maps/upper-air-maps/) (Clear analyses)

---

## Surface observations

---

## Surface observations basics
- Measurements taken at the Earth's surface
- Collected via:
    - Automated weather stations 
    - Manual observations 
    - Ships and buoys
- Record temperature, moisture, cloud cover, current weather

---

## Station symbols
- Surface observations are plotted on a map using station symbols
<div style="text-align: center;">
  <img src="station-model.gif" style="width:60%;"/>
  <p style="font-size: 14px;"><em>Source: NOAA WPC</em></p>
</div>

---

![bg right](weather-symbols.gif)

## Many types of weather symbols

---

## Surface map analyses - Fronts and symbols

<div style="text-align: center;">
  <img src="front-symbols.png" style="width:70%;"/>
  <p style="font-size: 14px;"><em>Source: Aviation Weather</em></p>
</div>

---

## Ida (2021) Example

<div style="text-align: center;">
  <img src="willy-p-figs/surface-analysis-ida.jpg" style="width:60%;"/>
  <p style="font-size: 14px;"><em>Source: NOAA WPC</em></p>
</div>

---

## Surface Analysis Resources \& Demo

- [NOAA Weather Prediction Center](https://www.wpc.ncep.noaa.gov/html/sfc-zoom.php) (archived every three hours)
- [Rutgers University](https://synoptic.envsci.rutgers.edu/surface/) (great for NJ weather stations)
- [College of DuPage](https://weather.cod.edu/analysis/) (click on Surface Maps)
- [NJ Weather Network](https://www.njweather.org) (not analysis but shows real-time NJ conditions)

---

# Part 2: Forecast Models

---

## What are weather forecast models?
- Numerical Weather Prediction (NWP) models simulate the atmosphere with math \& physics
- **Input**: All the data we've discussed so far, past model runs (sometimes)
- **Output**: Predicted atmospheric conditions (temperature, precipitation) at future times

---

## How do NWP models work?
1. **Data collection**: Gather data from satellites, weather stations, balloons, etc.
2. **Data assimilation**: Combine observations with model data to create a starting point for the model
3. **Model integration**: Solve equations of motion, thermodynamics, moisture, etc. *forward in time*
4. **Post-processing**: Transform model output into usable information

---

<img src="willy-p-figs/climate-model-diagram.png" width=60%>

---

## Global models
 - Cover the entire globe, run every 6-12 hours
 - Produce forecasts out to 16 days
 - Examples: GFS (Global Forecast System), ECMWF (European Centre for Medium-Range Weather Forecasts)

---

## Regional Models
- Cover smaller areas, run more frequently, higher resolution
- Produce forecasts out to 3-5 days
- Examples: NAM (North American Mesoscale), HRRR (High-Resolution Rapid Refresh), WoFS (Warn-on-Forecast System)

---

<div style="text-align: center;">
  <img src="global-vs-regional.png" style="width:60%;"/>
  <p style="font-size: 14px;"><em>Source: Copernicus</em></p>
</div>

---

## Why aren't forecasts from models perfect?
- **Observations are not perfect**
    - Missing data, errors, spotty coverage...
- **Physical equations are not perfect**
    - Simplifications, approximations, parameterizations...
- Computational limits and rounding errors affect precision
  - Butterfly effect

---

## Example: Convective parameterization
- A typical thunderstorm ➡️ ~15 miles diameter
- GFS (American) model ➡️ ~ 18 mile grid spacing
  **Problem: Model too coarse to *explicitly resolve* individual thunderstorms**

---

**Parameterization**: represent small-scale processes with simplified equations and estimates

<img src="willy-p-figs/arakawa-scheme.jpg" width=60%>

---

#### Example of Forecast Spread: Spaghetti Plot

![bg right:60%](willy-p-figs/cyclone-track.png)

---

## Using model output
- U.S. weather models available for free (may not last long in current administration 😅)
- Advanced tools sometimes behind paywall
  - Create soundings, take cross-sections, apply fancy algorithms
- **Do not put all your eggs in one forecast model basket!**

---

## Forecast model resources
- [NOAA Model Analysis and Guidance (MAG)](https://mag.ncep.noaa.gov/)
- [Tropical Tidbits](https://www.tropicaltidbits.com/) (easy interface, lots of models)
- [Pivotal Weather](https://www.pivotalweather.com/) (beautiful visualizations, some paid features)
- [College of DuPage](https://weather.cod.edu/forecast/)
- [NOAA NSSL Warn-on-Forecast System](cbwofs.nssl.noaa.gov/forecast) (high-resolution, only run some days)
- Lots of apps!

---

# Part III: Putting it all together

---

### Building a forecast

- **Start globally to forecast locally**
- **Global-scale** phenomena
  - Ex: Satellite data ➡️ global flow, upper air observations ➡️ jet stream
- **Synoptic-scale**
  - Fronts, high/low pressures, radar data ➡️ precip
- **Mesoscale/Local Scale**
  - Surface observations, convective quantities

---

## Snellman Funnel

<img src="willy-p-figs/snellman-funnel.jpg" width=70%>

---

### My approach for NJ forecasting
1. Look at global/CONUS satellite imagery.
2. Check out jet stream with upper air maps.
3. Start looking at synoptic features with radar, surface analyses, and surface observations.
4. (Optional) Look at "special" (severe, winter) weather fields.
5. Observe local conditions in NJ.
6. Consult appropriate forecast models.
7. Make forecast narrative for time period of interest.
8. **Verify your forecast!**

---

### Forecasting resources
- [Storm Prediction Center](https://www.spc.noaa.gov/)
- [NOAA Weather Prediction Center](https://www.wpc.ncep.noaa.gov/)
- [NWS Forecast Points](https://www.weather.gov/forecastpoints)
- [Ventusky](https://www.ventusky.com/)

---

### Conclusions
- Forecasting requires data, models, and experience.
  - Don't fall for data overload. Stick with the basics.
- Satellite, radar, upper air, and surface observations are all useful tools that give us different information.
- Forecast models are our most powerful tools but need to be used judiciously.
- Practice as much as you can, but keep it fun 😄.

---

### Additional Learning Resources

- [NOAA Jetsream](https://www.weather.gov/jetstream/)
- [Comet MetEd](https://www.meted.ucar.edu/)
- [Other NWS Educator Resources](https://www.weather.gov/owlie/educate)
- I run a forecast discussion every Friday at 1:30 at Zoom for CCNY students, email me if you want to join!

---
![bg left](willy-p-figs/callie.jpg)
Thank you! I'm happy to talk about meteorology, graduate school, research, jobs, etc.

📧: [tjanoski@ccny.cuny.edu](mailto:tjanoski@ccny.cuny.edu)