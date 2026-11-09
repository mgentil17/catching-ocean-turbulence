---
numbering:
  enumerator: 3.%s
---
# 3. Why does it matter?

Part 2 explained how turbulence mixes the water, and how $\varepsilon$ gives the turbulent fluxes of heat and other tracers. Does this mixing matter? We now look at what it does at a larger scale, over a whole season and a whole region, for each of the three properties of our profile ({numref}`fig-profile`).

% Time: ~20 min. One idea and one figure per section.

## 3.1 Heat: cooling the sea surface temperature 

The clearest example comes from the equatorial Pacific, where a mooring measured turbulence for a whole year ({numref}`fig-moum`). The sun and the atmosphere heat the surface layer (red), while turbulence carries heat down below it (blue). From February to May, surface heating exceeds turbulent cooling, and the sea surface temperature (SST) rises. From June to September, turbulent cooling exceeds surface heating, and the SST decreases (Moum et al., 2013). The same holds in the Atlantic cold tongue, where turbulent mixing is the main cooling term of the surface layer during the cold season (Hummels et al., 2013).

:::{figure} figures/moum2013_fig3a.png
:label: fig-moum
:width: 70%
One year at the equator, 140°W (Pacific), from January to January. Black: sea surface temperature (SST). Red: heat brought into the surface layer by the sun and the atmosphere. Blue: heat carried down by turbulence below the surface layer. The SST rises when red exceeds blue, and decreases when blue exceeds red. From Moum et al. (2013), *Seasonal sea surface cooling in the equatorial Pacific cold tongue controlled by ocean mixing*, Nature, 500, 64–67, Fig. 3a
:::

This matters for the climate, because the SST sets the exchanges of heat and moisture between the ocean and the atmosphere. In the tropical Atlantic, it affects rainfall over West Africa and South America, the position of the Intertropical Convergence Zone and hurricane activity (Foltz et al., 2019), and even, through the atmosphere, the climate of the tropical Pacific (Rodríguez-Fonseca et al., 2009). By lowering the SST, turbulent mixing takes part in all of this.

## 3.2 Nutrients: feeding phytoplankton

Phytoplankton need light from above and nutrients from below (Cullen, 2015). In the equatorial Atlantic, turbulence is strongest in the layer between the surface and the core of the Equatorial Undercurrent, a strong eastward current below the surface (dashed line in {numref}`fig-nitrate`). Whether mixing brings nitrate up depends on where the **nitracline**, the depth below which nitrate is abundant, lies compared with turbulent layer (Brandt et al., 2025):

- **In April**, the nitracline lies below the current core: mixing acts on nitrate-poor water, and chlorophyll stays deep.
- **In July**, the nitracline rises into the mixing layer: mixing brings nitrate up, and chlorophyll reaches the surface.

:::{figure} figures/brandt2025_fig6.png
:label: fig-nitrate
:width: 90%
The equatorial Atlantic in April (left) and July (right), in the upper 150 m, from west (W) to east (E). Dashed line: core of the Equatorial Undercurrent; turbulence is strong above it. In April, the nitracline is below this core and chlorophyll stays deep; in July, the nitracline is above it, mixing brings nitrate up, and chlorophyll reaches the surface. From Brandt et al. (2025), *Seasonal productivity of the equatorial Atlantic shaped by distinct wind-driven processes*, Nature Geoscience, 18, 84–90, Fig. 6 (CC BY 4.0).
:::

Our profile ({numref}`fig-profile`)c was taken in April: its deep chlorophyll maximum, around 45 dbar, is the April case.

## 3.3 Oxygen: ventilating the oxygen minimum zone

In the eastern tropical North Atlantic, between about 350 and 550 m, lies water poor in oxygen: an **oxygen minimum zone** (OMZ). There, respiration consumes oxygen, and several processes supply it. {numref}`fig-oxygen` shows this budget: vertical mixing (black) is one of these supplies, of the same order as the others (Brandt et al., 2015). This matters for marine life: many fish and zooplankton cannot live in oxygen-poor water, and the expansion of OMZs reduces their habitat (Stramma et al., 2012; Lévy et al., 2022).

:::{figure} figures/levy2022_fig2.png
:label: fig-oxygen
:width: 70%
Oxygen budget of the OMZ of the eastern tropical North Atlantic, as a function of depth. Green: consumption by respiration. Black: supply by vertical (turbulent) mixing. Purple: supply by horizontal mixing. Yellow: supply by currents. Grey band: the OMZ. From Lévy et al. (2022), *The crucial contribution of mixing to present and future ocean oxygen distribution*, in *Ocean Mixing: Drivers, Mechanisms and Impacts*, Elsevier, Fig. 2, adapted from Brandt et al. (2015), *Biogeosciences*, 12, 489–512.
:::

Our profile ({numref}`fig-profile`)b shows the same contrast at a smaller scale: below 40 dbar, the oxycline separates oxygen-rich water above from oxygen-poor water below, with turbulence in between.

## 3.4 Back to our profile

In part 1, we asked whether the turbulence of our profile matters. These three examples show that it can: mixing cools the sea surface, brings nutrients up, and supplies oxygen to the OMZ. In the deep ocean, mixing also makes dense water lighter, so that it can rise back toward the surface: it is a key part of the global overturning circulation (Munk & Wunsch, 1998). How large these fluxes are on our profile, at the equator and off the equator, is what we compute in part 5, after learning how $\varepsilon$ is measured (part 4).

:::{tip} Take-home
- **Turbulent mixing connects the surface to the ocean interior**: it cools the sea surface temperature, brings nutrients up to phytoplankton, and brings oxygen to the OMZ.
- **These effects reach the climate and marine life**: through the SST, mixing affects rainfall; through nutrients and oxygen, it shapes where marine life can grow and live.
:::
