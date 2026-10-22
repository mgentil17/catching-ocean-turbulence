# 2. What is turbulence?

*In part 1, $\varepsilon$ decreased by a factor of about 100 over a few tens of metres. What does $\varepsilon$ measure, and why does it change so much with depth? To answer, we follow the energy: where it comes from, where it goes, and what stops it from mixing the ocean.*

% Time: 25 min. Five equations in total, each explained in one sentence and applied to our profile.

## 2.1 From smooth to turbulent

:::{admonition} 🚧 To write
:class: dropdown
**Message.** A flow becomes turbulent when inertia wins over viscosity. In the ocean, it almost always does.

**Content.**
- Reynolds' dye experiment in a glass pipe (1883): a straight dye line, then sudden spreading.
- Equation: $Re = UL/\nu$. Inertia (creates smaller and smaller motions) versus viscosity (smooths them out).
- Ocean example: $U \approx 0.1$ m s⁻¹, $L \approx 10$ m, $\nu \approx 10^{-6}$ m² s⁻¹ gives $Re \approx 10^6$, far above the transition in Reynolds' pipe.
- *Your turn*: compute $Re$ for one ocean case.

**Figure.** Reynolds' original drawings of the dye experiment. Public domain. Source: Reynolds (1883), *Phil. Trans. R. Soc. Lond.*, 174, 935–982. *To download.*
:::

## 2.2 The energy cascade: what $\varepsilon$ really is

:::{admonition} 🚧 To write
:class: dropdown
**Message.** Energy enters the ocean at large scales, is passed to smaller and smaller eddies, and is turned into heat at the smallest ones. $\varepsilon$ is the rate of this transfer: the energy dissipated per unit mass and per unit time.

**Content.**
- Back to {numref}`fig-swirls`: the swirls seen from space are the top of the cascade.
- Energy sources: wind, tides and internal waves, shear between currents.
- Richardson's rhyme (1922): *"Big whorls have little whorls..."*
- Kolmogorov (1941): far from the large scales, small eddies depend only on $\varepsilon$ and $\nu$.
- Equation: the Kolmogorov scale $\eta = (\nu^3/\varepsilon)^{1/4}$. Applied to our profile: $\varepsilon = 10^{-7}$ W kg⁻¹ gives $\eta \approx 2$ mm; $\varepsilon = 10^{-9}$ W kg⁻¹ gives $\eta \approx 6$ mm. This is why we talk about **micro**structure.
- Equation: the inertial-range spectrum $E(k) = C\,\varepsilon^{2/3} k^{-5/3}$, in words only: energy is passed on without loss until viscosity takes over.
- *Your turn*: compute $\eta$ at the base of the mixed layer and at 80 dbar.

**Figures.**
- Reference: the first oceanic test of the $k^{-5/3}$ law, in a tidal channel: Grant, Stewart & Moilliet (1962), *J. Fluid Mech.*, 12, 241–268. Copyrighted: **link only** on the site; can be shown in the slides with its source.
- Optional: a schematic of the cascade, made by us.
:::

## 2.3 Stratification fights back

:::{admonition} 🚧 To write
:class: dropdown
**Message.** In a stratified ocean, mixing costs energy: dense water must be lifted and light water pushed down. Shear provides the energy, stratification resists. The Richardson number tells which one wins.

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
