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
Oxygen peaks around 40 dbar, then drops quickly: this is the **oxycline**. Chlorophyll peaks around 45 dbar, in the upper thermocline: this is the **chlorophyll maximum**, where phytoplankton find both enough light from above and nutrients from below (Cullen, 2015).
::::

::::{card} 🌀 Turbulence is not uniform
$\varepsilon$ is of order $10^{-7}$ W kg⁻¹ at the base of the mixed layer and of order $10^{-9}$ W kg⁻¹ around 80 dbar: **a decrease by a factor of about 100 over a few tens of metres**.
::::

:::::

Note also the grey dots in the $\varepsilon$ panel. Successive estimates, only a few metres apart, can differ by a factor of ten. Turbulence comes **in patches and bursts: it is intermittent**. This is one reason why ocean turbulence is difficult to observe, and why we will average many estimates later on.

These values are of the same order of magnitude as previous observations in the tropical Atlantic (Hummels et al., 2013) and in the global ocean (Waterhouse et al., 2014).

The coincidence of the turbulence peak with the oxygen and chlorophyll maxima is striking. Is it a chance, or does turbulence play a role in shaping these layers? Keep this question in mind: we come back to it in parts 3 and 5.

::::{note} Your turn: find the special depth
Compare the four panels of {numref}`fig-profile` side by side, at the same depth.

Is there a depth range where something particular happens in **all four** profiles at once?

:::{dropdown} Answer
Between about 40 and 45 dbar:

- $\varepsilon$ shows a **subsurface peak**, around 43 dbar;
- oxygen reaches its **maximum**, around 40 dbar;
- chlorophyll reaches its **maximum**, around 45 dbar;
- temperature drops fastest: this is where the **vertical temperature gradient** is strongest.

Is this a coincidence, or does turbulence play a role in shaping these layers? Keep this question in mind: we come back to it in parts 3 and 5.
:::
::::

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
- Turbulence, measured by $\varepsilon$, decreases by about two orders of magnitude over a few tens of metres below the mixed layer, with a subsurface peak close to the oxygen and chlorophyll maxima.
- Turbulence is intermittent: single estimates are noisy, and averages are needed.
:::
