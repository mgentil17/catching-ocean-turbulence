---
numbering:
  enumerator: 2.%s
---

# 2. What is turbulence?

In part 1, we saw a dissipation rate $\varepsilon$ that changes by a factor of 100 with depth. We read $\varepsilon$ as *"how strong the turbulence is"*. Here, we look at what turbulence is, and follow $\varepsilon$: what it is, where it comes from, and what it does to the water.

## 2.1 A turbulent flow: where $\varepsilon$ lives

In 1883, Reynolds injected a thin filament of dye into water flowing through a glass tube. At low speed, the filament stayed straight: the flow was **laminar** ({numref}`fig-reynolds`, top). At higher speed, it suddenly mixed with the water and filled the tube: the flow had become **turbulent** (middle). Lit by an electric spark, the colored cloud resolved into distinct curls: **eddies** (bottom).

:::{figure} figures/reynolds1883.png
:label: fig-reynolds
:width: 70%
Reynolds' sketches of the dye filament in his glass tube. Top: laminar flow, the filament stays straight. Middle: turbulent flow, the dye fills the tube. Bottom: the same turbulent flow seen by the light of an electric spark, which reveals the eddies. From Reynolds (1883), Figs. 3–5, *Philosophical Transactions of the Royal Society of London*, 174, 935–982 (public domain).
:::

Reynolds showed that the change depends on one number, the **Reynolds number**:

$$
Re = \frac{U L}{\nu}
$$

It compares **inertia** ($U$ a velocity, $L$ the scale over which it changes), which stretches the flow into smaller and smaller structures, with **viscosity** ($\nu \approx 10^{-6}$ m² s⁻¹ for seawater), which smooths them out. In a tube, the flow becomes turbulent above $Re \approx 2000. In the ocean, $Re$ reaches $10^6$ for a current changing by 0.1 m s⁻¹ over 10 m, and $10^{11}$ at the scale of a basin (Stewart, 2008). **The ocean is turbulent.**

:::{dropdown} Where does $Re$ come from?
In the equation of motion of a fluid (the Navier–Stokes equation), inertia appears in the advection term $(\mathbf{u}\cdot\nabla)\mathbf{u}$, of order $U^2/L$, and viscosity in the term $\nu\nabla^2\mathbf{u}$, of order $\nu U/L^2$. Their ratio is $UL/\nu = Re$. When $Re$ is large, viscosity is negligible at the scale $L$ of the flow.
:::

A turbulent flow is irregular: its eddies cannot be predicted one by one. Reynolds (1895) proposed to describe it in two parts, a **mean flow** and **fluctuations** around it:

$$
u = \bar{u} + u'
$$

$\bar{u}$ is the current, averaged over time or space; $u'$ are the eddies. The energy of the eddies is the **turbulent kinetic energy**, $\frac{1}{2}\left(\overline{u'^2} + \overline{v'^2} + \overline{w'^2}\right)$, per kilogram of water. $\varepsilon$ is the rate at which this energy is lost.

The word "eddy" is used for two different things. The eddies seen from space in part 1 are tens to hundreds of kilometers across. At these scales, the Earth's rotation and the stratification constrain the motion: these eddies are nearly two-dimensional, and much of their energy moves to *larger* scales (Kraichnan, 1967; Scott & Wang, 2005). The eddies of turbulence are three-dimensional: they are small enough that rotation and stratification no longer constrain them. Energy reaches them from larger motions through other processes, such as breaking internal waves. In this course, we follow the energy of three-dimensional turbulence.

## 2.2 Where $\varepsilon$ comes from: the energy chain

The energy of these turbulent eddies follows a chain in three steps (Tennekes & Lumley, 1972):

1. **Production.** Where the current changes with depth (the **shear**), the current gives part of its energy to the eddies. Winds, tides and currents are the original sources of this shear. In the ocean, currents change much faster with depth than horizontally: over tens of meters vertically, against tens of kilometers horizontally. This is why we focus on the vertical shear.
2. **Cascade.** The largest turbulent eddies break into smaller eddies, which break into even smaller ones. As Richardson, 2007 wrote:

   > *Big whirls have little whirls that feed on their velocity,*\
   > *and little whirls have lesser whirls and so on to viscosity.*

3. **Dissipation.** When the eddies are only millimeters to centimeters across, viscosity can finally act: it turns their energy into heat.

**$\varepsilon$ is the rate of this last step**: the energy dissipated by viscosity, per kilogram of water and per second (W kg⁻¹). When turbulence is steady, what is dissipated at the end of the chain is what was produced at the start: **$\varepsilon$ tells us how much energy flows through turbulence**. In a stratified ocean, part of the energy is also used to lift dense water; we come back to this in section 2.3.

The size of the largest turbulent eddies is set by the stratification. Above the **Ozmidov scale** (Ozmidov, 1965), the stratification flattens the eddies; below it, they are three-dimensional:

$$
L_O = \left(\frac{\varepsilon}{N^3}\right)^{1/2}
$$

where $N$ measures the strength of the stratification (section 2.3). The size of the smallest eddies, where dissipation happens, is the **Kolmogorov scale** (Kolmogorov, 1941). It depends only on the viscosity and on $\varepsilon$:

$$
\eta = \left(\frac{\nu^3}{\varepsilon}\right)^{1/4}
$$

Between production and dissipation, Kolmogorov (1941) showed that energy is passed on without loss, and that its distribution across scales follows a simple law: the energy spectrum decreases as $k^{-5/3}$, where $k$ is the wavenumber (the inverse of the scale) ({numref}`fig-spectrum`). **$\varepsilon$ says *how much* energy is dissipated, $\eta$ says *at what size***. The more energy, the smaller the last eddies. Because dissipation happens over centimeters, measuring $\varepsilon$ means measuring how the velocity changes over this scale: this is what the vertical microstructure profiler does (part 4).

:::{figure} figures/energy_spectrum.png
:label: fig-spectrum
:width: 85%
The energy chain of turbulence, seen across eddy sizes: our schematic of the classic energy spectrum of turbulence (e.g., Tennekes & Lumley, 1972). The wavenumber $k$ is the inverse of the eddy size: large eddies on the left, small eddies on the right. The energy spectrum $E(k)$ shows how much energy the eddies of each size hold. Energy enters at the largest eddies (size $l$), is passed on to smaller eddies along a slope in $k^{-5/3}$ (inertial range), and is turned into heat near the Kolmogorov scale $\eta$, at the rate $\varepsilon$.
:::

## 2.3 What $\varepsilon$ tells us: stirring and mixing

The eddies carry everything that is in the water: momentum, but also heat, salt, oxygen or nutrients, called **tracers**.

Eddies stretch and fold a patch of tracer into thinner and thinner filaments. This is **stirring**: the gradients become stronger, but the water is not mixed yet. When the filaments are thin enough, **molecular diffusion** smooths them out. This is **mixing** (Eckart, 1948). **Turbulent mixing** is the two in series, and its rate is set by the stirring (Müller & Garrett, 2002).

:::{figure} figures/stirring_mixing.png
:label: fig-stirring
:width: 80%
The same warm layer between cold water, as in a thermocline, at three times ($t = 0$, then $t_1$, then $t_2 > t_1$). Top: with molecular diffusion only, the boundaries between warm and cold water barely widen. Bottom: with the same diffusion, eddies stretch the warm water into thin filaments (stirring), which molecular diffusion then erases (mixing): the water becomes uniform much faster. Red: warm; blue: cold; yellow: mixed. Our two-dimensional simulation, following the idea of Eckart (1948).
:::

::::{note} Your turn
Molecular diffusion of heat ($\kappa_T \approx 1.4 \times 10^{-7}$ m² s⁻¹) smooths a temperature difference over a distance $L$ in a time $t \approx L^2/\kappa_T$. Compute $t$ for $L = 1$ m and for $L = 1$ mm.

:::{dropdown} Answer
About **80 days** for 1 m, and about **7 seconds** for 1 mm. Diffusion alone is far too slow at the scale of the thermocline; stirring is what brings the tracer down to millimeter scales, where diffusion is fast.
:::
::::

The result is a **turbulent heat flux**, written $\overline{w'T'}$ with the fluctuations of section 2.1: eddies carry warm water down and cold water up. Taylor (1922) showed that this flux acts like a diffusion, but much stronger than molecular diffusion:

$$
\overline{w'T'} = -K_\rho\,\frac{\partial \bar{T}}{\partial z}
$$

$K_\rho$ depends on the flow, and this is where $\varepsilon$ comes back. In a stratified ocean, mixing costs energy: dense water must be lifted up, and light water pushed down. Of the energy that the shear gives to the eddies, most is dissipated ($\varepsilon$), and a small part lifts dense water. Osborn (1980) assumed that this small part is about 0.2 times $\varepsilon$: for every 5 joules dissipated, about 1 joule lifts dense water. This gives:

$$
K_\rho = \Gamma\,\frac{\varepsilon}{N^2}
$$

with $\Gamma \approx 0.2$ (a common choice, though not universal; Gregg et al., 2018) and $N^2 = -(g/\rho_0)\,\partial\rho/\partial z$ the strength of the stratification. More energy dissipated means more mixing; stronger stratification means less. **This is why we measure $\varepsilon$**: with $N^2$, it gives $K_\rho$. We use the same $K_\rho$ for heat, salt and oxygen. Where turbulence is strong, $K_\rho$ is much larger than the molecular diffusivity of heat, salt or oxygen: eddies mix them all at the same rate. This is a good approximation, but not always valid, for example with double diffusion. With $K_\rho$, we compute the turbulent fluxes of heat and oxygen in part 3.

Eddies also carry the speed of the currents. A parcel of slow water moving up into a faster layer slows it down; a parcel of fast water moving down speeds up the slower layer below. This **momentum flux**, $\overline{u'w'}$, acts as a friction between layers of current. At the surface, it also passes the push of the wind into the ocean. It is described by another coefficient, the turbulent viscosity $K_m$. $K_m$ is not equal to $K_\rho$: their ratio, the turbulent Prandtl number $Pr_t = K_m/K_\rho$, depends on the stratification, because momentum can also be carried by pressure, through waves, without moving water. We do not treat it here.

% In class: a glass of water with a drop of dye, left at rest, then stirred with a spoon.

## 2.4 Reading $\varepsilon$ on our profile

Let us look again at our profile ({numref}`fig-profile`) with what we now know.

:::::{grid} 1 1 3 3

::::{card} ⚡ Energy flowing through turbulence
At the base of the mixed layer, each kilogram of water dissipates about $10^{-7}$ W. Around 80 dbar, about $10^{-9}$ W: **100 times less energy** flows through turbulence there.
::::

::::{card} 🔬 The size of turbulent eddies
On our profile, the largest turbulent eddies (Ozmidov scale) are about 2 to 9 cm across, and the smallest (Kolmogorov scale) about 2 to 4 mm. Turbulence lives between these two sizes: this is why we talk about **micro**structure.
::::

::::{card} 🌀 Where the gradients are
On our profile, $\varepsilon$ shows a subsurface peak around 40–45 dbar, in the layer where temperature changes fastest, and where oxygen and chlorophyll reach their maximum.
::::

:::::

::::{note} Your turn
In a very energetic layer, $\varepsilon = 10^{-5}$ W kg⁻¹, with $N^2 = 10^{-3}$ s⁻² and $\nu = 10^{-6}$ m² s⁻¹. What are the Kolmogorov scale and the Ozmidov scale? Compare with our profile.

:::{dropdown} Answer
$\eta \approx 0.6$ mm and $L_O \approx 0.6$ m. Turbulent eddies now range over three orders of magnitude, from tens of centimeters to below a millimeter. The more energy, the larger the range, and the finer the profiler must resolve (part 4).
:::
::::

On our profile, the subsurface peak of turbulence lies where temperature, oxygen and chlorophyll change fast with depth. If it mixes heat, oxygen and nutrients across the thermocline, what does this change for the ocean, the atmosphere and marine life? This is part 3.

:::{tip} Take-home
- **A turbulent flow** is a mean flow plus irregular eddies. In the ocean, $Re$ is huge: the ocean is turbulent.
- **$\varepsilon$ is the end of the energy chain**: the shear of the current feeds the eddies, the cascade carries the energy down to millimeter-scale eddies, and viscosity dissipates it at the rate $\varepsilon$.
- **Turbulence stirs, molecular diffusion mixes**: the result is a turbulent flux, much stronger than molecular diffusion, whose strength depends on $\varepsilon$.
:::
