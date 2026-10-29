---
numbering:
  enumerator: 4.%s
---
# 4. How do we measure turbulence?

In part 2, we saw that $\varepsilon$ is set by how the velocity changes over millimetres to centimetres. So how can a profiler falling through the ocean measure this? We first look at the two ways and the platforms used to catch turbulence, then follow our instrument, the vertical microstructure profiler (VMP), from the deck to $\varepsilon$.

% Time: ~30 min. 4.1 two ways (5 min), 4.2 the VMP (5 min), 4.3 at sea (10 min), 4.4 shear to eps (10 min).

## 4.1 Two ways to catch turbulence

Turbulence is measured at millimetre to centimetre scales, in two ways:

- **Shear probes** measure the fluctuations of velocity. From their gradients we get $\varepsilon$ (section 2.2):

$$
\varepsilon = \frac{15}{2}\,\nu \left\langle \left(\frac{\partial u'}{\partial z}\right)^2 \right\rangle
$$

- **Fast thermistors** measure the fluctuations of temperature. From their gradients we get $\chi$, the rate at which the temperature fluctuations are smoothed out by molecular diffusion, the equivalent of $\varepsilon$ for temperature (Osborn & Cox, 1972):

$$
\chi = 6\,\kappa_T \left\langle \left(\frac{\partial T'}{\partial z}\right)^2 \right\rangle
$$

$\chi$ can also give $\varepsilon$, and the eddy diffusivity of heat (Osborn & Cox, 1972). In this course, we use the shear probes, for which there is today a consensus on the processing (ATOMIX; Lueck et al., 2024). The brackets $\langle\;\rangle$ are averages over a few metres of profile; the factors 15/2 and 6 come from assuming that the small-scale turbulence has the same statistics in all directions (isotropy; Taylor, 1935).

These sensors are carried by many platforms ({numref}`fig-platforms`). This list is not exhaustive; other platforms include autonomous underwater vehicles or tethered profilers.

:::{figure} figures/platforms.png
:label: fig-platforms
:width: 95%
From the ship: the vertical microstructure profiler (VMP). Autonomous: a glider carrying a MicroRider, and a profiling float carrying a FloatRider (ArgoMix). On moorings: the $\chi$pod, with fast thermistors only. Images: Rockland Scientific (VMP-250, MicroRider and FloatRider; rocklandscientific.com) and Ocean Mixing Group, Oregon State University ($\chi$pod; mixing.ceoas.oregonstate.edu).
:::

## 4.2 The VMP and its probes

The VMP falls freely through the water, at about 0.7 m s⁻¹, attached to the ship by a slack rope so that the ship's motion does not reach it. Brushes at its tail keep the fall speed steady and the instrument vertical.

- **two shear probes**: the water flowing past the tip pushes it sideways, and a piezo-ceramic element turns this force into a signal proportional to the velocity fluctuation $u'$;
- **fast thermistors** (FP07), for $T'$;
- a **CTD** (here with oxygen and chlorophyll sensors), for the background profiles of part 1;
- **accelerometers**, to measure the vibrations of the instrument.

The probes record the signal in time. Because the VMP falls much faster than the eddies change, we can assume that it crosses a frozen pattern of eddies (Taylor's frozen turbulence hypothesis): a change in time is then a change in depth, $\partial u'/\partial z = (1/W)\,\partial u'/\partial t$, where $W$ is the fall speed.

:::{figure} figures/vmp_photos.png
:label: fig-vmp
:width: 90%
*To make (our photos).* Left: the VMP on deck during PIRATA FR-36. Right: its nose, with the two shear probes, the fast thermistors and the CTD sensors.
:::

## 4.3 Operating a VMP at sea

Good data start on deck ({numref}`fig-deploy`). The points below follow the recommendations of Rockland Scientific, the manufacturer, and common practice at sea.

**Before the profile**
- Check the probes (state, calibration coefficients in the configuration file), the battery and the clock.
- Do one or two test profiles, and check the data before starting the survey.

**During the profile**
- **Most important: the rope must stream away from the stern, never under the ship**, where the propellers can cut it.
- The ship moves slowly into the current, at 0.5–1 m s⁻¹ at most. The GPS may even show the ship going backwards over the ground: this is fine as long as the rope streams away from the ship.
- Pay out the rope generously, keeping only one or two coils of slack at the surface.
- Aim for a fall speed of about 0.7 m s⁻¹ (standard VMP-250; 1 m s⁻¹ at most for the electronics). If the fall speed drops below 0.3 m s⁻¹ or the instrument tilts, add weight.

**After the profile**
- Recover the VMP without hitting the probes, rinse it with fresh water, and protect the probes. Keep spare probes on board: they are fragile.
- Note the time and position of each profile in the logbook.

:::{figure} figures/vmp_deployment.png
:label: fig-deploy
:width: 90%
*To make (our photos).* A VMP deployment during PIRATA FR-36: the instrument and its rope on deck (left), and the VMP going into the water from the stern (right).
:::

## 4.4 From shear to $\varepsilon$

The processing of shear probe data follows the best practices of **ATOMIX**, an international working group that set common methods, quality checks and file formats, so that $\varepsilon$ from different instruments and groups can be compared (Lueck et al., 2024). Our files follow this format.

### Check the profile first

Right after a profile, a quick look tells whether it is usable ({numref}`fig-check`): a steady fall speed, a small tilt, low vibrations, two shear probes giving similar signals, and no spikes (impacts of particles or plankton on the probes). The first metres below the surface are discarded, because they are disturbed by the ship's wake.

:::{figure} figures/fig4_check.png
:label: fig-check
:width: 95%
*To make (our data).* Quick check of one VMP profile. From left to right: fall speed, tilt, vibrations (accelerometers), and the signals of the two shear probes, as a function of pressure.
:::

### The four steps

1. **L1, converted**: the signals in physical units.
2. **L2, cleaned**: spikes and vibrations removed, usable sections selected.
3. **L3, spectra**: the shear spectrum computed over segments of a few metres.
4. **L4, dissipation**: $\varepsilon$, obtained by integrating the spectrum, with its quality checks.

Step 3 is where the theory of part 2 is used ({numref}`fig-shear-spectrum`). In practice, $\varepsilon$ is computed from the shear spectrum $\Psi(k)$, which shows how the shear variance is spread over wavenumbers:

$$
\varepsilon = \frac{15}{2}\,\nu \int_{k_1}^{k_2} \Psi(k)\,\mathrm{d}k
$$

The integral is taken over the wavenumbers not affected by noise, typically between about 1 and 100 cpm. The measured spectrum is compared with a universal shape that depends only on $\varepsilon$ and $\nu$, the Nasmyth spectrum (Nasmyth, 1970; Lueck, 2022), which is also used to correct for the part of the spectrum that is not resolved.

Two limits follow. When $\varepsilon$ is very large, the smallest eddies become smaller than the probe can resolve (about a centimetre). When $\varepsilon$ is very small, the signal falls below the noise of the instrument, around $10^{-10}$ W kg⁻¹.

:::{figure} figures/fig4_spectrum.png
:label: fig-shear-spectrum
:width: 70%
*To make (our data).* Shear spectra from our profile, in a strongly turbulent layer (around 43 dbar) and a weakly turbulent one (around 80 dbar), with the Nasmyth spectrum for the estimated $\varepsilon$ (dashed). The wavenumber is in cycles per metre (cpm).
:::

The L4 level of our files gives $\varepsilon$ with pressure, temperature, salinity and oxygen. This is all we need for part 5: from these profiles we compute $N^2$, then $K_\rho = \Gamma\varepsilon/N^2$, then the fluxes.

:::{tip} Take-home
- **Turbulence is measured at millimetre scales**, with shear probes ($\varepsilon$) or fast thermistors ($\chi$), on many platforms.
- **Good $\varepsilon$ starts at sea** with a well-flying instrument, and continues with a standard processing (ATOMIX) from shear to $\varepsilon$.
:::
