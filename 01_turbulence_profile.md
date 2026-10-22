# 1. What does ocean turbulence look like?

Before any theory, let's look at the data.

On the night of 4 April 2026, at 0°N, 10°W, a vertical microstructure profiler was dropped from R/V *Thalassa*. While falling freely through the water, it measured temperature, oxygen and chlorophyll, and tiny fluctuations of velocity from which we estimate $\varepsilon$, the **dissipation rate of turbulent kinetic energy**. For now, read $\varepsilon$ simply as *"how strong the turbulence is"*. We will see exactly what it means in part 2.

:::{figure} figures/fig1_profile.png
:label: fig-profile
A night profile at 0°N, 10°W (PIRATA FR-36, 4 April 2026, 00:01 UTC). From left to right: temperature, dissolved oxygen, chlorophyll, and dissipation rate $\varepsilon$ (grey dots: individual estimates; black line: median in 2-dbar bins). Square: base of the mixed layer (MLD, density criterion of de Boyer Montégut et al., 2004). Triangle: 20 °C isotherm, a common marker of the tropical thermocline.
:::

## Reading the profile

:::::{grid} 1 1 3 3

::::{card} 🌡️ A layered ocean
A warm, well-mixed surface layer, about 13 m thick, sits on top of the **thermocline**, where temperature drops by about 10 °C in 50 m. Below, the water is colder and changes slowly.
::::

::::{card} 🫧 Life just below the surface layer
Oxygen peaks around 40 dbar, then drops quickly: this is the **oxycline**. Chlorophyll peaks around 47 dbar, in the upper thermocline: this is the **chlorophyll maximum**, where phytoplankton find both enough light from above and nutrients from below (Cullen, 2015).
::::

::::{card} 🌀 Turbulence is not uniform
$\varepsilon$ is about $10^{-7}$ W kg⁻¹ near the surface and about $10^{-9}$ W kg⁻¹ below 80–100 dbar: **two orders of magnitude** over 100 m. Turbulence is strong above the thermocline and weak below it.
::::

:::::

Note also the grey dots in the $\varepsilon$ panel. Successive estimates, only a few metres apart, can differ by a factor of ten. Turbulence comes in **patches and bursts**: it is *intermittent*. This is one reason why ocean turbulence is difficult to observe, and why we will average many estimates later on.

These values are typical of the upper tropical ocean. Across the global ocean, measured values of $\varepsilon$ cover several orders of magnitude, from about $10^{-10}$ W kg⁻¹ or less in the quiet interior to much larger values near the surface and over rough topography (Waterhouse et al., 2014).

::::{note} Your turn
Using {numref}`fig-profile`, estimate:

1. the depth of the base of the mixed layer;
2. the depth of the 20 °C isotherm;
3. the depth of the chlorophyll maximum;
4. the value of $\varepsilon$ at 30 dbar and at 120 dbar. By how much does it change?

:::{dropdown} Answers
1. About 13 dbar. 2. About 57 dbar. 3. About 47 dbar, between the mixed layer and the 20 °C isotherm.
4. About $10^{-8}$ to $3\times10^{-8}$ W kg⁻¹ at 30 dbar, and about $1\times10^{-9}$ to $3\times10^{-9}$ W kg⁻¹ at 120 dbar: roughly a factor of 10 to 30.
:::
::::

## The questions this profile raises

This single profile leads to the four questions of the rest of the course:

::::{grid} 1 2 2 2

:::{card} 2. What is turbulence?
What does $\varepsilon$ measure physically, and why is turbulence weaker below the thermocline?
:::

:::{card} 3. Why does it matter?
Does this turbulence move heat, oxygen and nutrients across the thermocline?
:::

:::{card} 4. How do we measure it?
How do we get a value of $\varepsilon$ from a profiler falling through the ocean?
:::

:::{card} 5. Is it the same elsewhere?
Would we find the same profile a few degrees south of the equator?
:::

::::

:::{tip} Take-home
- The upper ocean is layered: a mixed layer, a thermocline, and a colder interior.
- Turbulence, measured by $\varepsilon$, varies by orders of magnitude with depth: strong above the thermocline, weak below.
- Turbulence is intermittent: single estimates are noisy, and averages are needed.
:::
