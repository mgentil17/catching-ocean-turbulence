# 2. What is turbulence?

In part 1, $\varepsilon$ decreased by a factor of about 100 over a few tens of metres. To understand why, we need to know what makes the ocean turbulent, what $\varepsilon$ measures, and what can make turbulence strong in one layer and weak in another.

## 2.1 From laminar to turbulent flow

In 1883, Reynolds ran a simple experiment. Water flowed through a long glass tube, and he injected a thin filament of coloured dye at its entrance. At low speed, the filament stayed straight along the whole tube: the flow was **laminar** ({numref}`fig-reynolds`, top). When he increased the speed, the filament suddenly mixed with the surrounding water and filled the tube with colour: the flow had become **turbulent** (middle). When he lit the tube with an electric spark, the coloured cloud resolved into distinct curls: **eddies** (bottom).

:::{figure} figures/reynolds1883.png
:label: fig-reynolds
:width: 90%
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


## 2.2 The energy cascade: what $\varepsilon$ really is

:::{admonition} 🚧 To write
:class: dropdown
**Message.** Energy enters the ocean at large scales, is passed to smaller and smaller eddies, and is turned into heat at the smallest ones. $\varepsilon$ is the rate of this transfer: the energy dissipated per unit mass and per unit time (W kg⁻¹). **This is where $\varepsilon$ is defined.**

**Content.**
- Back to {numref}`fig-swirls`: the swirls seen from space are the top of the cascade.
- Energy sources: wind, tides and internal waves, shear between currents.
- Richardson's rhyme (1922): *"Big whorls have little whorls..."*
- Kolmogorov (1941): far from the large scales, small eddies depend only on $\varepsilon$ and $\nu$.
- Equation: the Kolmogorov scale $\eta = (\nu^3/\varepsilon)^{1/4}$. Applied to our profile: $\varepsilon = 10^{-7}$ W kg⁻¹ gives $\eta \approx 2$ mm; $\varepsilon = 10^{-9}$ W kg⁻¹ gives $\eta \approx 6$ mm. This is why we talk about **micro**structure.
- Equation: the inertial-range spectrum $E(k) = C\,\varepsilon^{2/3} k^{-5/3}$, in words only: energy is passed on without loss until viscosity takes over.
- **Key idea for part 4**: dissipation happens where the velocity changes over millimetres, so $\varepsilon$ is linked to the small-scale velocity gradients (the *shear*). Say it in words here; the formula $\varepsilon = \frac{15}{2}\nu\overline{(\partial u'/\partial z)^2}$ and the shear spectrum come in part 4, where the VMP measures exactly this.
- *Your turn*: compute $\eta$ at the base of the mixed layer and at 80 dbar.

**Figures.**
- Reference: the first oceanic test of the $k^{-5/3}$ law, in a tidal channel: Grant, Stewart & Moilliet (1962), *J. Fluid Mech.*, 12, 241–268. Copyrighted: **link only** on the site; can be shown in the slides with its source.
- Optional: a schematic of the cascade, made by us.
:::

## 2.3 Stratification fights back

:::{admonition} 🚧 To write
:class: dropdown
**Message.** In a stratified ocean, mixing costs energy (keep $N^2$: it is needed again in part 3 to compute $K = \Gamma\varepsilon/N^2$): dense water must be lifted and light water pushed down. Shear provides the energy, stratification resists. The Richardson number tells which one wins.

**Content.**
- Equation: $N^2 = -\frac{g}{\rho_0}\frac{\partial \rho}{\partial z}$, the buoyancy frequency.
- Equation: $Ri = N^2/S^2$, with $S^2 = (\partial u/\partial z)^2 + (\partial v/\partial z)^2$.
- Miles (1961) and Howard (1961): a steady stratified shear flow can become unstable only if $Ri < 1/4$ somewhere. A **necessary** condition, not a guarantee.
- Kelvin–Helmholtz billows: waves at the interface roll up, break and mix the two layers.

**Figures.**
- Our simulation of Kelvin–Helmholtz billows: roll-up, then mixing of light and dense water. Ours (2D simulation; the real breakdown to turbulence is 3D, to say in the caption).
- The same instability in the sky: Kelvin–Helmholtz clouds, photo by Carlo Cafaro, CC BY 3.0, credit "Carlo Cafaro (distributed via imaggeo.egu.eu)". *To download.*
- If possible, real observations: echosounder images of billows in the ocean (Moum et al. / Smyth & Moum, 2012, *Oceanography*). **Ask Jim Moum for permission** before putting it on the site.
:::

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
*To write once the sections are done (two points maximum).*
:::
