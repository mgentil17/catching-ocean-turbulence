# 2. What is turbulence?

*In part 1, $\varepsilon$ decreased by a factor of about 100 over a few tens of metres. What does $\varepsilon$ measure, and why does it change so much with depth? To answer, we follow the energy: where it comes from, where it goes, and what stops it from mixing the ocean.*

% Time: 25 min. Five equations in total, each explained in one sentence and applied to our profile.

## 2.1 From smooth to turbulent

In 1883, Osborne Reynolds ran a simple experiment. Water flowed through a long glass tube, and he injected a thin filament of coloured dye at its entrance. At low speed, the filament stayed straight along the whole tube: the flow was **laminar**. When he increased the speed, the filament suddenly broke into eddies and the colour spread across the whole tube: the flow had become **turbulent** ({numref}`fig-reynolds`).

:::{figure} figures/reynolds1883.png
:label: fig-reynolds
:width: 70%
Reynolds' sketches of the dye filament in his glass tube: straight at low speed (top), broken into eddies at higher speed (bottom). From Reynolds (1883), *Philosophical Transactions of the Royal Society of London*, 174, 935–982 (public domain).
:::

Reynolds showed that the change does not depend on the speed alone, but on one dimensionless number, now called the **Reynolds number**:

$$
Re = \frac{U L}{\nu}
$$

where $U$ is a typical velocity, $L$ the length scale over which the velocity changes, and $\nu \approx 10^{-6}$ m² s⁻¹ the kinematic viscosity of seawater. $Re$ compares two effects in the equations of motion: **inertia**, which stretches the flow into smaller and smaller structures, and **viscosity**, which smooths them out (Thorpe, 2007). In Reynolds' tube, the flow became turbulent when $Re$, based on the tube diameter and the mean velocity, exceeded about 2000.

::::{note} Your turn
Take a current whose speed changes by 0.1 m s⁻¹ over 10 m of depth, a modest value for the upper ocean. What is $Re$? Compare it with the value in Reynolds' tube.

:::{dropdown} Answer
$Re = (0.1 \times 10)/10^{-6} = 10^{6}$, about 500 times larger than the transition in Reynolds' tube. Ocean flows have very large Reynolds numbers.
:::
::::

So the ocean *can* be turbulent almost everywhere. Yet in part 1, $\varepsilon$ was about 100 times smaller below the thermocline than just below the mixed layer. A large Reynolds number is therefore not enough: something else decides **where** turbulence is strong. To understand what, we first need to know what turbulence does with its energy.

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
