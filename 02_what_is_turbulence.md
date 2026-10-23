# 2. What is turbulence?

In part 1, we saw what ocean turbulence looks like: swirls within swirls, and a dissipation rate $\varepsilon$ that changes by a factor of 100 with depth. We read $\varepsilon$ as *"how strong the turbulence is"*. Here, we look at what turbulence is, and follow $\varepsilon$: what it is, where it comes from, and what it does to the water.

## 2.1 A turbulent flow: where $\varepsilon$ lives

In 1883, Reynolds injected a thin filament of dye into water flowing through a glass tube. At low speed, the filament stayed straight: the flow was **laminar** ({numref}`fig-reynolds`, top). At higher speed, it suddenly mixed with the water and filled the tube: the flow had become **turbulent** (middle). Lit by an electric spark, the coloured cloud resolved into distinct curls: **eddies** (bottom).

:::{figure} figures/reynolds1883.png
:label: fig-reynolds
:width: 70%
Reynolds' sketches of the dye filament in his glass tube. Top: laminar flow, the filament stays straight. Middle: turbulent flow, the dye fills the tube. Bottom: the same turbulent flow seen by the light of an electric spark, which reveals the eddies. From Reynolds (1883), Figs. 3–5, *Philosophical Transactions of the Royal Society of London*, 174, 935–982 (public domain).
:::

Reynolds showed that the change depends on one number, the **Reynolds number**:

$$
Re = \frac{U L}{\nu}
$$

It compares **inertia** ($U$ a velocity, $L$ the scale over which it changes), which stretches the flow into smaller and smaller structures, with **viscosity** ($\nu \approx 10^{-6}$ m² s⁻¹ for seawater), which smooths them out. In a tube, the flow becomes turbulent above $Re$ of a few thousand. In the ocean, $Re$ reaches $10^6$ for a current changing by 0.1 m s⁻¹ over 10 m, and $10^{11}$ at the scale of a basin (Stewart, 2008). **The ocean is turbulent.**

:::{dropdown} Where does $Re$ come from?
In the equation of motion of a fluid (the Navier–Stokes equation), inertia appears in the advection term $(\mathbf{u}\cdot\nabla)\mathbf{u}$, of order $U^2/L$, and viscosity in the term $\nu\nabla^2\mathbf{u}$, of order $\nu U/L^2$. Their ratio is $UL/\nu = Re$. When $Re$ is large, viscosity is negligible at the scale $L$ of the flow.
:::

A turbulent flow is irregular: its eddies cannot be predicted one by one. Reynolds (1895) proposed to describe it in two parts, a **mean flow** and **fluctuations** around it:

$$
u = \bar{u} + u'
$$

$\bar{u}$ is the current, averaged over time or space; $u'$ are the eddies. The energy of the eddies is the **turbulent kinetic energy**, $\frac{1}{2}\left(\overline{u'^2} + \overline{v'^2} + \overline{w'^2}\right)$, per kilogram of water. $\varepsilon$ is about this energy.

## 2.2 Where $\varepsilon$ comes from: the energy chain

The energy of the eddies follows a chain in three steps (Tennekes & Lumley, 1972):

1. **Production.** Where the current changes with depth (the **shear**), the current gives part of its energy to the eddies. Winds, tides and currents are the original sources of this shear.
2. **Cascade.** Large eddies break into smaller eddies, which break into even smaller ones. As Richardson (1922, p. 66) put it:

   > *Big whirls have little whirls that feed on their velocity,*\
   > *and little whirls have lesser whirls and so on to viscosity.*

3. **Dissipation.** When the eddies are only millimetres to centimetres across, viscosity can finally act: it turns their energy into heat.

**$\varepsilon$ is the rate of this last step**: the energy dissipated by viscosity, per kilogram of water and per second (W kg⁻¹). When turbulence is steady, what is dissipated at the end of the chain is what was produced at the start: **$\varepsilon$ tells us how much energy flows through turbulence**. In a stratified ocean, part of the energy is also used to lift dense water; we come back to this in part 3 (Osborn, 1980).

The size of the eddies where dissipation happens is the **Kolmogorov scale** (Kolmogorov, 1941). It depends only on the viscosity and on $\varepsilon$:

$$
\eta = \left(\frac{\nu^3}{\varepsilon}\right)^{1/4}
$$

Between production and dissipation, Kolmogorov (1941) showed that energy is passed on without loss, and that its distribution across scales follows a simple law: the energy spectrum decreases as $k^{-5/3}$, where $k$ is the wavenumber (the inverse of the scale) ({numref}`fig-spectrum`). $\varepsilon$ says *how much* energy is dissipated, $\eta$ says *at what size*. The more energy, the smaller the last eddies. Because dissipation happens over millimetres, measuring $\varepsilon$ means measuring how the velocity changes over millimetres: this is what the vertical microstructure profiler does (part 4).

:::{figure} figures/energy_spectrum.png
:label: fig-spectrum
:width: 85%
The energy chain of turbulence, seen across eddy sizes: our schematic of the classic energy spectrum of turbulence (e.g., Tennekes & Lumley, 1972). The wavenumber $k$ is the inverse of the eddy size: large eddies on the left, small eddies on the right. The energy spectrum $E(k)$ shows how much energy the eddies of each size hold. Energy enters at the largest eddies (size $l$), is passed on to smaller eddies along a slope in $k^{-5/3}$ (inertial range), and is turned into heat near the Kolmogorov scale $\eta$, at the rate $\varepsilon$.
:::

:::{dropdown} Does energy always go to smaller scales?
No. In the ocean, large eddies (tens to hundreds of kilometres) are nearly two-dimensional because of the Earth's rotation and the stratification, and part of their energy moves to *larger* scales: this is the inverse cascade (Kraichnan, 1967; Scott & Wang, 2005). In this course, we follow the energy that goes down to small scales.
:::

## 2.3 What $\varepsilon$ tells us: stirring and mixing

The eddies carry everything that is in the water: momentum, but also heat, salt, oxygen or nutrients, called **tracers**.

Eddies stretch and fold a patch of tracer into thinner and thinner filaments. This is **stirring**: the gradients become stronger, but the water is not mixed yet. When the filaments are thin enough, **molecular diffusion** smooths them out. This is **mixing** (Eckart, 1948; Osborn, 1998). **Turbulent mixing** is the two in series, and its rate is set by the stirring (Müller & Garrett, 2002).

:::{figure} figures/stirring_mixing.png
:label: fig-stirring
:width: 80%
*To make.* A patch of dye in a fluid at rest, smoothed by molecular diffusion only (top), and in a turbulent flow, stirred and then mixed (bottom).
:::

The net result is a **turbulent flux**. For heat, it is $\overline{w'T'}$: on average, warm water moves down while cold water moves up. Seen from far away, this flux acts like a diffusion down the mean gradient, but much stronger than molecular diffusion:

$$
\overline{w'T'} = -K\,\frac{\partial \bar{T}}{\partial z}
$$

where $K$ is the **eddy diffusivity** (Taylor, 1921). In the ocean interior, a tracer released at sea spread vertically with $K \approx 10^{-5}$ m² s⁻¹, about 100 times the molecular diffusivity of heat (Ledwell et al., 1993).

Unlike molecular diffusivity, which is a property of seawater, $K$ is a property of the flow: the more energy flows through turbulence, the stronger the mixing. **This is why we measure $\varepsilon$**: in part 3, we use it to compute $K$, and then the fluxes of heat and oxygen.

::::{note} Your turn
Molecular diffusion of heat ($\kappa_T \approx 1.4 \times 10^{-7}$ m² s⁻¹) smooths a temperature difference over a distance $L$ in a time $t \approx L^2/\kappa_T$. Compute $t$ for $L = 1$ m and for $L = 1$ mm.

:::{dropdown} Answer
About **80 days** for 1 m, and about **7 seconds** for 1 mm. Diffusion alone is far too slow at the scale of the thermocline; stirring is what brings the tracer down to millimetre scales, where diffusion is fast.
:::
::::

% In class: a glass of water with a drop of dye, left at rest, then stirred with a spoon.

## 2.4 Reading $\varepsilon$ on our profile

:::::{grid} 1 1 3 3

::::{card} ⚡ Energy flowing through turbulence
At the base of the mixed layer, each kilogram of water dissipates about $10^{-7}$ W. Around 80 dbar, about $10^{-9}$ W: **100 times less energy** flows through turbulence there.
::::

::::{card} 🔬 The last eddies
With $\varepsilon = 10^{-7}$ W kg⁻¹, the last eddies are about **2 mm** across; with $10^{-9}$ W kg⁻¹, about **6 mm**. This is why we talk about **micro**structure.
::::

::::{card} 🌀 Where the gradients are
The peak of $\varepsilon$ around 40–45 dbar lies in the layer where temperature changes fastest, and where oxygen and chlorophyll reach their maximum: turbulence is strong where there are strong gradients to mix.
::::

:::::

::::{note} Your turn
Check the values of the second card with $\eta = (\nu^3/\varepsilon)^{1/4}$ and $\nu = 10^{-6}$ m² s⁻¹. What would $\eta$ be in a very energetic layer with $\varepsilon = 10^{-5}$ W kg⁻¹?

:::{dropdown} Answer
About 1.8 mm and 5.6 mm. With $\varepsilon = 10^{-5}$ W kg⁻¹, $\eta \approx 0.6$ mm: the more energy, the smaller the last eddies, and the finer the profiler must resolve.
:::
::::

Two questions remain open. Why does so much energy flow through turbulence at 40–45 dbar, in a strongly stratified layer? And how much heat and oxygen does this turbulence actually move? This is part 3.

:::{tip} Take-home
- **A turbulent flow** is a mean flow plus irregular eddies. In the ocean, $Re$ is huge: the ocean is turbulent.
- **$\varepsilon$ is the end of the energy chain**: the shear of the current feeds the eddies, the cascade carries the energy down to millimetre-scale eddies, and viscosity dissipates it at the rate $\varepsilon$.
- **Turbulence stirs, molecular diffusion mixes**: the result is a turbulent flux, much stronger than molecular diffusion, whose strength depends on $\varepsilon$.
:::
