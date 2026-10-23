# 2. What is turbulence?

In part 1, $\varepsilon$ decreased by a factor of about 100 over a few tens of metres. To understand why, we need to know what makes the ocean turbulent, what $\varepsilon$ measures, and what can make turbulence strong in one layer and weak in another.

## 2.1 From laminar to turbulent flow

In 1883, Reynolds ran a simple experiment. Water flowed through a long glass tube, and he injected a thin filament of coloured dye at its entrance. At low speed, the filament stayed straight along the whole tube: the flow was **laminar** ({numref}`fig-reynolds`, top). When he increased the speed, the filament suddenly mixed with the surrounding water and filled the tube with colour: the flow had become **turbulent** (middle). When he lit the tube with an electric spark, the coloured cloud resolved into distinct curls: **eddies** (bottom).

:::{figure} figures/reynolds1883.png
:label: fig-reynolds
:width: 70%
Reynolds' sketches of the dye filament in his glass tube. Top: laminar flow, the filament stays straight. Middle: turbulent flow, the dye fills the tube. Bottom: the same turbulent flow seen by the light of an electric spark, which reveals the eddies. From Reynolds (1883), Figs. 3–5, *Philosophical Transactions of the Royal Society of London*, 174, 935–982 (public domain).
:::

Reynolds showed that the change does not depend on the speed alone, but on a dimensionless number, now called the **Reynolds number**:

$$
Re = \frac{U L}{\nu}
$$

where $U$ is a typical velocity, $L$ a typical length of the flow, and $\nu \approx 10^{-6}$ m² s⁻¹ the kinematic viscosity of seawater. $L$ is the scale over which the velocity changes: in Reynolds' tube, it is the diameter of the tube; in the ocean, it can be the thickness of a layer where the current changes with depth.

$Re$ compares **inertia**, which stretches the flow into smaller and smaller structures, with **viscosity**, which smooths them out. In a tube, the flow stays laminar below $Re \approx 2300$ and becomes turbulent above a few thousand.

:::{dropdown} Where does $Re$ come from?
In the equation of motion of a fluid (the Navier–Stokes equation), inertia appears in the advection term $(\mathbf{u}\cdot\nabla)\mathbf{u}$, of order $U^2/L$, and viscosity in the term $\nu\nabla^2\mathbf{u}$, of order $\nu U/L^2$. Their ratio is
$$
\frac{U^2/L}{\nu U/L^2} = \frac{UL}{\nu} = Re .
$$
When $Re$ is large, viscosity is negligible at the scale $L$ of the flow.
:::

::::{note} Your turn
Take a current whose speed changes by 0.1 m s⁻¹ over 10 m of depth, a modest value for the upper ocean. What is $Re$? Compare it with the value in Reynolds' tube.

:::{dropdown} Answer
$Re = (0.1 \times 10)/10^{-6} = 10^{6}$, several hundred times larger than the transition in a tube. With the scale of an ocean basin ($U = 0.1$ m s⁻¹, $L = 1000$ km), $Re$ reaches $10^{11}$ (Stewart, 2008). Whatever the scale, $Re$ is huge.
:::
::::

In the ocean, $Re$ is far above the threshold of a tube: at the scale of currents, viscosity is much too weak to keep the flow laminar. **The ocean is turbulent.**

Yet turbulence cannot grow without limit. Winds, tides and currents supply it with energy all the time: this energy must be removed somewhere, or turbulence would keep increasing. The only process that turns the energy of motion into heat is viscosity. But we have just seen that viscosity is negligible at the scale of ocean currents. So where can viscosity act? As we will see, it is a question of scale.


### 2.2 The energy cascade: what $\varepsilon$ really is

Winds, tides and currents put energy into the ocean at large scales. Large eddies are stretched and broken by the flow into smaller eddies, which break into even smaller ones: energy is passed from large to small scales. This is the **energy cascade**, summarised by Richardson (1922):

> *Big whorls have little whorls, which feed on their velocity,*\
> *And little whorls have lesser whorls, and so on to viscosity.*

As the eddies get smaller, the velocity changes over shorter and shorter distances: the **velocity gradients** become stronger. When the eddies are only a few millimetres across, viscosity smooths these gradients out, and the kinetic energy of the eddies is turned into heat. The size of these smallest eddies is the **Kolmogorov scale** (Kolmogorov, 1941):

$$
\eta = \left(\frac{\nu^3}{\varepsilon}\right)^{1/4}
$$

This answers the question of section 2.1: viscosity acts at the end of the cascade, at the millimetre scale.

We can now define $\varepsilon$. **$\varepsilon$ is the rate at which viscosity turns the kinetic energy of the eddies into heat**, per unit mass (W kg⁻¹). When turbulence is steady, it is equal to the rate at which energy is supplied at the top of the cascade. Because this happens where the velocity gradients are strongest, $\varepsilon$ is computed from the velocity gradients at the millimetre scale: this is what a microstructure profiler measures (part 4).

:::{figure} figures/cascade_schematic.png
:label: fig-cascade
:width: 80%
*To make.* The energy cascade: energy enters at large scales, is passed to smaller and smaller eddies, and is turned into heat by viscosity at the Kolmogorov scale $\eta$.
:::

:::{dropdown} Does energy always go to smaller scales?
No. In the ocean, large eddies (tens to hundreds of kilometres) are nearly two-dimensional because of the Earth's rotation and the stratification, and part of their energy moves to *larger* scales: this is the inverse cascade (Kraichnan, 1967; Scott & Wang, 2005). In this course, we follow the energy that goes down to small scales.
:::

::::{note} Your turn
Compute $\eta$ at the base of the mixed layer ($\varepsilon \approx 10^{-7}$ W kg⁻¹) and around 80 dbar ($\varepsilon \approx 10^{-9}$ W kg⁻¹), with $\nu = 10^{-6}$ m² s⁻¹.

:::{dropdown} Answer
$\eta = (10^{-18}/10^{-7})^{1/4} \approx 2$ mm at the base of the mixed layer, and $\eta = (10^{-18}/10^{-9})^{1/4} \approx 6$ mm at 80 dbar. The last eddies are a few millimetres across: this is why we talk about **micro**structure.
:::
::::

## 2.3 From stirring to mixing

The same eddies do not only act on the velocity: they also carry everything that is in the water, such as heat, salt, oxygen or nutrients. These quantities are called **tracers**.

Eddies stretch and fold a patch of tracer into thinner and thinner filaments. This is **stirring**: the gradients become stronger, but the water is not mixed yet. When the filaments are thin enough, **molecular diffusion** smooths them out, and the water becomes uniform. This is **mixing** (Eckart, 1948; Osborn, 1998). **Turbulent mixing** is the two in series: stirring makes the filaments thin, molecular diffusion erases them, and the overall rate is set by the stirring (Müller & Garrett, 2002).

:::{figure} figures/stirring_mixing.png
:label: fig-stirring
:width: 80%
*To make.* A patch of dye in a fluid at rest, smoothed by molecular diffusion only (top), and in a turbulent flow, stirred and then mixed (bottom).
:::

::::{note} Your turn
Molecular diffusion of heat ($\kappa_T \approx 1.4 \times 10^{-7}$ m² s⁻¹) smooths a temperature difference over a distance $L$ in a time of order $t \approx L^2/\kappa_T$. Compute $t$ for $L = 1$ m and for $L = 1$ mm.

:::{dropdown} Answer
For $L = 1$ m: $t \approx 1/(1.4 \times 10^{-7}) \approx 7 \times 10^{6}$ s, about **80 days**. For $L = 1$ mm: $t \approx 10^{-6}/(1.4 \times 10^{-7}) \approx$ **7 seconds**. Diffusion alone is far too slow at the scale of the thermocline, but very fast on millimetre filaments. Stirring is what brings the tracer down to these scales.
:::
::::

% Slides only: Smyth & Moum, "3D Turbulence", Encyclopedia of Ocean Sciences (copyrighted, show with source).
% Note for 2.4: in a stratified ocean, temperature and salt set the density, so they are not fully passive.

## 2.4 Stratification fights back

So far, we have described turbulence as if the water had the same density everywhere. The upper ocean is not like that: it is **stratified**, with light, warm water above dense, cold water, as in the thermocline of part 1. To mix a stratified ocean, eddies must lift dense water up and push light water down. This costs energy: part of the energy of turbulence is used to lift dense water, and the rest is dissipated at the rate $\varepsilon$ (Osborn, 1980). We come back to this in part 3.

The strength of the stratification is measured by the **buoyancy frequency** $N$:

$$
N^2 = -\frac{g}{\rho_0}\frac{\partial \rho}{\partial z}
$$

where $g$ is gravity, $\rho$ the density and $\rho_0$ a reference density. A parcel of water moved up or down oscillates around its position at the frequency $N$. The larger $N^2$, the harder it is to mix.

The energy that can overcome the stratification comes from the **shear** $S$: the change of the current with depth, $S^2 = (\partial u/\partial z)^2 + (\partial v/\partial z)^2$. Which one wins is measured by the **Richardson number**:

$$
Ri = \frac{N^2}{S^2}
$$

Miles (1961) and Howard (1961) showed that a steady, stratified shear flow can become unstable only if $Ri < 1/4$ somewhere. This is a **necessary** condition: $Ri < 1/4$ makes instability possible, not certain. When it happens, the interface between the layers starts to wave, the waves roll up into **Kelvin–Helmholtz billows**, and the billows break into turbulence and mix the two layers ({numref}`fig-kh`).

[Figure: our 2D Kelvin–Helmholtz simulation — the real breakdown into turbulence is 3D]

Shear instability is one of the main sources of turbulence in the ocean interior (Smyth & Moum, 2012). Where it acts, the strength of turbulence depends on the balance between shear and stratification, not on either one alone. This is how turbulence can be strong in one layer and weak in another.

Your turn: in the thermocline of part 1, T drops by ~10 °C over 50 m. Ignoring salinity (Δρ ≈ ρ0 α ΔT, α ≈ 3×10⁻⁴ K⁻¹), compute N². What shear S is needed to get Ri < 1/4?
Answer: Δρ ≈ 3 kg m⁻³, N² ≈ 6×10⁻⁴ s⁻², N ≈ 0.024 s⁻¹ (period ~4 min). Ri < 1/4 requires S > 2N ≈ 0.05 s⁻¹, e.g. 0.5 m s⁻¹ over 10 m. To know whether this happens on our profile, we need the current measurements (section 2.5).

## 2.4 Back to our profile

:::{admonition} 🚧 To write
:class: dropdown
**Message.** Just below the mixed layer at the equator, the shear of the Equatorial Undercurrent keeps $Ri$ close to 1/4: turbulence is strong. Deeper, stratification wins and $\varepsilon$ drops. This is the answer to the question of part 1.

**Content.**
- The Equatorial Undercurrent: an eastward current below the westward surface flow, in the upper thermocline.
- "Marginal instability": $Ri$ stays close to 1/4 over long periods (Smyth & Moum, 2013, Pacific).
- Comparison with observations in the Atlantic (Hummels et al., 2013).
- Transition to part 3: if turbulence mixes, what does it carry?

**Figure.** Our profile again, with $N^2$ (and later $S^2$ and $Ri$ from the ADCP). *Current data: to come.*
:::

:::{tip} Take-home
- At high Reynolds number, the flow becomes irregular and full of eddies: **the ocean is turbulent**.
- Energy cascades to millimetre-scale eddies, where viscosity turns it into heat at the rate **ε**.
- The same eddies **stir** heat, salt and oxygen into thin filaments, and molecular diffusion **mixes** them.
- **Stratification resists mixing**: shear can overcome it only where Ri < 1/4, so turbulence is strong in some layers and weak in others.
:::
