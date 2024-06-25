---
marp: true
footer: 'Workshop on Climate and Weather Hazards for Urban New York Area,
June 26, 2024'

---

# Exploring Extreme Rainfall from Hurricane Ida using the Warn-on-Forecast System

Ty Janoski<sup>1,2</sup>, James Booth<sup>1</sup>, Thomas Galarneau<sup>2</sup>

<sup>1<sub>City College of New York</sub>
2<sub>NOAA National Severe Storms Laboratory</sub></sup>

<!-- theme: gaia -->

---

## Background --  Ida
- Many of us are already familiar with the impacts of Hurricane Ida on the New York City area
- Dozens of deaths, widespread flooding, and significant damage
- Suffice it to say, it is worth studying

---

<div style="text-align: center;">
  <img src="image.png" alt="A plot of hourly rainfall records at Newark NJ" style="width:70%;"/>
  <p style="font-size: 14px;"><em>Source: New York Times</em></p>
</div>

---

## Background: Warn-on-Forecast System (WoFS)
- High-resolution (3km), convection-allowing model ensemble system
- Produces probabilistic forecasts of severe weather
- Assimilates radar, satellite, and surface observations
- Run every hour starting at 17Z
    - 6-hour long forecasts

---

<div style="text-align: center;">
  <img src="wofs.gif" alt="An animated gif of the composite reflectivity from the 23Z WoFS with NWS warnings overlaid" style="width:50%;"/>
  <p style="font-size: 14px;"><em>Source: WoFS Cloud-based Web Viewer</em></p>
</div>

---

## Research Questions
1. **What are the main factors *across scales* that contributed to the extreme rainfall from Ida?**
2. In what ways was Ida unique compared to other extreme rainfall events in the New York City area?
3. What lessons can we learn from Ida to improve our understanding and prediction of extreme rainfall in the New York City area?

---

## Methodology

- Analyze retrospective WoFS forecasts of Ida
- Separate the forecasts into two groups based on the average 01–02 UTC rainfall in the New York City area
    - The **5 wettest** and **5 driest** ensemble members from *each* of the 20Z, 21Z, 22Z, and 23Z initializations
- Compare the two groups to identify the main factors that contributed to the extreme rainfall

---

<div style="text-align: center;">
  <img src="precip-histogoram.png" alt="A histogram showing the area-avaeraged 01-02 UTC rainfall in a 48km box centered on NYC" style="width:70%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

## Sample Results

<div style="text-align: center;">
  <img src="MLCAPE-wet-vs-dry.png" alt="" style="width:70%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

<div style="text-align: center;">
  <img src="comp-refl-wet-vs-dry.png" alt="" style="width:60%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>