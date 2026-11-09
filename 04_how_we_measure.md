---
numbering:
  enumerator: 4.%s
---
# 4. How do we measure turbulence?

In part 2, we saw that $\varepsilon$ is set by how the velocity changes over millimeters to centimeters. So how can a profiler falling through the ocean measure this? We first look at the two ways and the platforms used to catch turbulence, then follow our instrument, the vertical microstructure profiler (VMP), from the deck to $\varepsilon$.

% Time: ~30 min. 4.1 two ways (5 min), 4.2 the VMP (5 min), 4.3 at sea (10 min), 4.4 shear to eps (10 min).

## 4.1 Two ways to catch turbulence

Turbulence is measured at millimeter to centimeter scales, in two ways:

- **Shear probes** measure the fluctuations of velocity. From their gradients we get $\varepsilon$ (section 2.2):

$$
\varepsilon = \frac{15}{2}\,\nu \left\langle \left(\frac{\partial u'}{\partial z}\right)^2 \right\rangle
$$

- **Fast thermistors** measure the fluctuations of temperature. From their gradients we get $\chi$, the rate at which the temperature fluctuations are smoothed out by molecular diffusion, the equivalent of $\varepsilon$ for temperature (Osborn & Cox, 1972):

$$
\chi = 6\,\kappa_T \left\langle \left(\frac{\partial T'}{\partial z}\right)^2 \right\rangle
$$

$\chi$ can also give $\varepsilon$, and the eddy diffusivity of heat (Osborn & Cox, 1972). In this course, we use the shear probes, for which there is today a consensus on the processing (ATOMIX; Lueck et al., 2024). The brackets $\langle\;\rangle$ are averages over a few meters of profile; the factors 15/2 and 6 come from assuming that the small-scale turbulence has the same statistics in all directions (isotropy; Taylor, 1935).

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

:::{figure} figures/vmp_probes.png
:label: fig-vmp
:width: 70%
The nose of a VMP-250, with its two shear probes, a fast thermistor (FP07), the conductivity–temperature (CT) sensor, the fluorometer–turbidity sensor and the pressure sensor. The tilt and vibration sensors are inside the case. Image: Rockland Scientific (rocklandscientific.com).
:::

## 4.3 Operating a VMP at sea

Good data start on deck ({numref}`fig-deploy`). The points below follow the recommendations of Rockland Scientific, the manufacturer, and common practice at sea.

:::{figure} figures/vmp_deployment.png
:label: fig-deploy
:width: 90%
A VMP deployment during PIRATA FR-36. (a) Position of the ship during the profiles: the ship moves slowly (1 m s⁻¹ at most) into the surface current, so that the rope (red) streams away from the stern. (b) The VMP on deck, attached to the winch with a release; the rope is coiled on deck. (c) The VMP is lowered into the water. (d) Once released, it falls freely while the rope is paid out. Photos and schematic: courtesy of F. Gasparin (IRD/LEGOS).
:::

**Before the profile**
- Check the probes (state, calibration coefficients in the configuration file), the battery and the clock.
- Do one or two test profiles, and check the data before starting the survey.

**During the profile**
- The VMP is lowered into the water with a winch and a release, then falls freely while the rope, coiled on deck, is paid out (panels b–d).
- **Most important: the rope must stream away from the stern, never under the ship**, where the propellers can cut it (panel a).
- The ship moves slowly into the surface current, at 0.5–1 m s⁻¹ at most. The GPS may even show the ship going backwards over the ground: this is fine as long as the rope streams away from the ship.
- Pay out the rope generously, keeping only one or two coils of slack at the surface. At the equator, this matters even more: the Equatorial Undercurrent, below the surface, can carry the VMP towards the ship at depth (panel a).
- Aim for a fall speed of about 0.7 m s⁻¹ (standard VMP-250; 1 m s⁻¹ at most for the electronics). If the fall speed drops below 0.3 m s⁻¹ or the instrument tilts, add weight.

**After the profile**
- Recover the VMP without hitting the probes, rinse it with fresh water, and protect the probes. Keep spare probes on board: they are fragile.
- Note the time and position of each profile in the logbook.

## 4.4 From shear to $\varepsilon$

The processing of shear probe data follows the best practices of **ATOMIX**, an international working group that set common methods, quality checks and file formats, so that $\varepsilon$ from different instruments and groups can be compared (Lueck et al., 2024). It goes in two stages: a quick check on board, then the full processing ashore.

### On board: a quick check

Right after a profile, the raw file of the VMP (a binary `.p` file) is opened in **Zissou Essentials**, the free software of Rockland Scientific (a paid version, Zissou Premium, offers more). We select the free-fall descent and look at two things ({numref}`fig-check`):

- **Kinematics**: below the surface, the tilt should stay within a few degrees, and the fall speed should be steady, between about 0.3 and 1 m s⁻¹. Vibrations should stay low.
- **Microstructure**: a real turbulent patch shows up on **both** shear probes at the same depth. A spike on one probe only is probably an impact of a particle. The first metres are disturbed by the launch and the ship's wake, and are discarded.

The goal on board is only to decide: is the profile usable, does the VMP need more weight, is a probe damaged? Zissou can also compute a quick spectrum, but a reliable $\varepsilon$ requires the full processing.

:::{figure} figures/fig4_check.png
:label: fig-check
:width: 95%
Quick check of a VMP profile on board with Zissou Essentials. (a) Kinematics: vibrations, tilt and fall speed. (b) Microstructure: signals of the two shear probes (shifted for clarity), temperature gradients and background temperature.
:::

### Ashore: the four steps

1. **L1, converted**: the signals in physical units, with the software of Rockland Scientific (Zissou).
2. **L2, cleaned**: spikes removed, and the part of the shear signal caused by the vibrations of the instrument (measured by the accelerometers) subtracted.
3. **L3, spectra**: the shear spectrum computed over segments of a few metres.
4. **L4, dissipation**: $\varepsilon$, with its quality checks.

Steps 2 to 4 can be done with the toolbox of Vic et al., in prep (https://github.com/cvic29/py-ocean-microstructure/tree/main).

**The shear spectrum.** Over a segment of a few meters, the shear signal mixes eddies of all sizes. Like a prism that splits light into colours, the **shear spectrum** $\Psi(k)$ splits this signal into eddy sizes: it tells how much shear comes from each size. The size is given by the **wavenumber** $k$, the number of oscillations per metre (cpm): large eddies on the left, small eddies on the right. Adding up all sizes, that is, taking the area under the curve, gives back the total shear, and therefore $\varepsilon$ (section 4.1):

$$
\varepsilon = \frac{15}{2}\,\nu \left\langle \left(\frac{\partial u'}{\partial z}\right)^2 \right\rangle = \frac{15}{2}\,\nu \int_{k_1}^{k_2} \Psi(k)\,\mathrm{d}k
$$

where $\nu$ is the viscosity of seawater. We only add up the sizes where the probe sees turbulence and not noise, from $k_1$ to $k_2$. In {numref}`fig-processed`f, $k_1$ is about 0.5 cpm, and $k_2$ is about 30 cpm in the turbulent segment and about 10 cpm in the quiet one. The spectrum is averaged over a segment of a few meters, which gives one value of $\varepsilon$. This is a compromise: a longer segment gives a more stable estimate, a shorter one keeps more vertical detail. This length is chosen in the processing chain.

**Checking with the theory.** Theory tells us what the curve should look like for a given $\varepsilon$ (Nasmyth, 1970; Lueck, 2022). So we check that the measured spectrum has this shape. If it does, $\varepsilon$ is reliable; if it does not, because of noise or vibrations, the estimate is rejected. The theoretical curve is also used to add the smallest eddies, too small for the probe to see.

**Two limits.** When turbulence is very strong, the smallest eddies become smaller than the probe itself (about a centimeter), and it cannot see them all. When turbulence is very weak, the signal becomes smaller than the noise of the instrument, around $10^{-10}$ W kg⁻¹. Our profile, with $\varepsilon$ between $10^{-9}$ and $10^{-7}$ W kg⁻¹, lies well between these two limits.

Near the surface, the first meters are lost: the VMP is not yet falling freely, and the ship's wake disturbs the water. On our profile, the data start at about 13 dbar. To measure turbulence closer to the surface, other instruments are used, such as profilers that rise toward the surface.

:::{figure} figures/fig4_processed.png
:label: fig-processed
:width: 95%
The same profile (station 26) after processing with the toolbox of C. Vic. (d) $\varepsilon$ from each shear probe ($\varepsilon_1$, $\varepsilon_2$) and the final value $\varepsilon$ (white squares), as a function of time since the start of the record: the VMP goes deeper with time. (e) $\varepsilon_2$ against $\varepsilon_1$; rejected estimates are marked in red. (f) Cleaned shear spectra of the two probes ($\Psi_{1c}$, $\Psi_{2c}$) in two segments, with the model spectrum of Lueck (2022) in grey.
:::

How to read {numref}`fig-processed`:

- **(d)** Each probe gives its own $\varepsilon$ (blue and red). The final value (white squares) is the mean of the two when both pass the quality checks, or the value of the only probe that passes them. Here, $\varepsilon$ is high in the upper part of the profile and in a patch around 100–110 dbar (near 1310 s), as seen on board ({numref}`fig-check`).
- **(e)** Each point compares the two probes. Close to the diagonal, the two probes agree. But this is not enough: each estimate must also pass the quality checks. This is why some red points, rejected, lie close to the diagonal. When the two probes disagree, $\varepsilon$ can still come from the probe that passes the checks (panel d). The other labels ($\varepsilon_{isr}$, "isr kept") refer to another method, used only for very strong turbulence; it is not used here.
- **(f)** Each curve is the shear spectrum of one probe over one segment, after removing the vibrations. When it follows the grey model, $\varepsilon$ is well estimated. The upper pair comes from a turbulent segment: its spectrum is higher and extends to smaller eddies (larger $k$), as in the spectrum of section 2.2. The lower pair comes from a quiet segment. AAt the largest wavenumbers, the curves rise again: this is noise, not turbulence. So the upper limit $k_2$ is chosen in each segment, before this noise. In a quiet segment, the eddies that dissipate are larger (section 2.2): most of the spectrum lies before the noise, and $\varepsilon$ is still reliable.

The L4 level of our files gives $\varepsilon$ with pressure, temperature, salinity and oxygen. This is all we need for part 5: from these profiles we compute $N^2$, then $K_\rho = \Gamma\varepsilon/N^2$, then the fluxes.

:::{tip} Take-home
- **Turbulence is measured at centimeter scales**, with shear probes ($\varepsilon$) or fast thermistors ($\chi$), on many platforms.
- **Good $\varepsilon$ starts at sea** with a well-flying instrument, and continues with a standard processing (ATOMIX) from shear to $\varepsilon$.
:::

