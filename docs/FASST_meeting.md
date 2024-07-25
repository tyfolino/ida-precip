---
marp: true
footer: 'FASST Meeting, July 24th, 2024'
html: true

---

# Exploring Extreme Rainfall from Hurricane Ida using WoFS

Ty Janoski<sup>1,2</sup>, James Booth<sup>1</sup>, Thomas Galarneau<sup>2</sup>

<sup>1<sub>City College of New York</sub>
2<sub>NOAA National Severe Storms Laboratory</sub></sup>

<!-- theme: gaia -->

---

## Background --  Ida
- Hurricane Ida's impacts on the New York City region cannot be understated
- Record-breaking hourly rainfall
  - **3.15" in Central Park**
  - **3.24" in Newark, NJ**
- NYC particularly susceptible to damage from urban flooding
  - Subways, basement apartments, etc.
- Dozens of deaths and significant damage to infrastructure

---

<div style="text-align: center;">
  <img src="image.png" alt="A plot of hourly rainfall records at Newark NJ" style="width:70%;"/>
  <p style="font-size: 14px;"><em>Source: New York Times</em></p>
</div>

---

## Background -- Meteorological History of Ida
- Made landfall in Louisiana on August 29th as a Cat 4
- Became fully extratropical by September 1st
- Moisture, instability, and shear led to the creation of supercells
  - Tornados (up to EF3) in PA & NJ
- **Robust & long-lived T-storms produced the extreme rainfall in NYC**


---

<div style="text-align: center;">
  <img src="wofs.gif" alt="An animated gif of the composite reflectivity from the 23Z WoFS with NWS warnings overlaid" style="width:55%;"/>
  <p style="font-size: 14px;"><em>Source: WoFS Cloud-based Web Viewer</em></p>
</div>

---

## Research Questions
1. **What are the main factors *across scales* that contributed to the extreme rainfall from Ida?**
    - Synoptic, frontal, and mesoscale processes
2. What sets Ida apart from other extreme precipitation events?
3. What lessons can we learn from Ida to improve our understanding and prediction of extreme rainfall in the New York City area?

---

## Methodology

- Analyze retrospective WoFS forecasts of Ida
  - Use the ensemble spread to our advantage
- Separate the forecasts into two groups based on the average 01–02 UTC rainfall in the New York City area
    - The **5 wettest** and **5 driest** ensemble members from *each* of the 20Z, 21Z, 22Z, 23Z, & 0Z initializations
- Compare the two groups to identify the main factors that contributed to the extreme rainfall

---

<div style="text-align: center;">
  <img src="new-wofs-histogram.png" alt="" style="width:70%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### Dry ensemble has precip farther NW

<div style="text-align: center;">
  <img src="pmm-rain-and-uh.png" alt="" style="width:95%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### Time evolution of composite reflectivity

<div style="text-align: center;">
  <img src="comp_refl_23to02.gif" alt="" style="width:95%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### Wet - Dry: Mainly location?

<div style="text-align: center;">
  <img src="pmm-rain-wet-dry-diff.png" alt="" style="width:100%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### Well, partially. Wet ens. has higher max precip anywhere in domain.

<div style="text-align: center;">
  <img src="max-rainfall-entire-domain-histogram.png" alt="" style="width:70%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

## What is influencing the different behvaior between the wet and dry ensemble?

---

### Instability? MLCAPE greater in wet ens. in NJ

<div style="text-align: center;">
  <img src="mlcape_23_00_wet_dry_diff.png" alt="" style="width:70%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### Moisture may play a role too

<div style="text-align: center;">
  <img src="pw_23_00_wet_dry_diff.png" alt="" style="width:70%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### Wet ens. has higher 500mb heights, especially in southern part of domain

<div style="text-align: center;">
  <img src="500mb_gz_23_00_diffs.png" alt="" style="width:60%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### Different geostrophic winds...

<div style="text-align: center;">
  <img src="layer_average_geo_winds_wet_dry_diff.png" alt="" style="width:60%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

### More cyclonic flow in actual 850-500mb winds

<div style="text-align: center;">
  <img src="layer_average_winds_wet_dry_diff.png" alt="" style="width:60%;"/>
  <p style="font-size: 14px;"><em></em></p>
</div>

---

## Next steps

- Figure out what is going on—is it the overlying circulation? Or convective ingredients?
- Explore other factors (moisture flux convergence, shear, etc.)
- The same ensemble members generally make up the wet and dry ensembles with no overlap
  - Do these difference materialize at even earlier times?
  - Has the scene already been set ~6 hours before 1Z?
- Compare to observations and/or reanalysis
  - Are the key factors we are finding present in the observations?

---

  ## I'd love to hear your thoughts!
  email: [tyler.janoski@noaa.gov](mailto:tyler.janoski@noaa.gov)