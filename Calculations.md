# Calculations

## System of Units

- Length: Kilometers ($km$)
- Mass: Solar Masses ($M_\odot$)
- Time: Seconds ($s$)

## Relativistic Units

Many of the calculations utilize a relativistic system of units where the speed of light ($c$) is a dimensionless value equal to 1. This leads to the ability to express length as a unit of time. [Further reading](https://physicspages.com/pdf/Relativity/Relativistic%20units.pdf).

$$ c = L \cdot T^{-1} $$
$$ 1 = L \cdot T^{-1} $$
$$ T = L $$

where $L$ is a unit of length and $T$ is a unit of time. To convert an meters-kilograms-seconds (MKS) value to relativistic units, simply use the following.

$$ c = 1 = 2.99792458 \times 10^8 \space m \cdot s^{-1} $$
$$ 1 \space s = 2.99792458 \times 10^8 \space m $$

### Time Conversion Factor

Since the unit of length for this project is kilometers, I'm instead using the following conversion factor.

$$ 1 \space s = 2.99792458 \times 10^8 \space m $$
$$ 1 \space s = 2.99792458 \times 10^5 \space (10^3 \space m) $$
$$ 1 \space s = 2.99792458 \times 10^5 \space km $$

## Energy Density Conversion Factor

Though the user interface has energy density and pressure in terms of $MeV \cdot fm^{-3}$, the solver expects [different units](#system-of-units). To accomodate this, it's necessary to convert to to $M_\odot \cdot km^-3$.

First, start with energy in terms of SI units.

$$ 1 \space J = 1 \space kg \space m^2 \space s^{-2} $$

Find 1 $kg$ in terms of $M_\odot$.

$$ 1 \space M_\odot = 1.988416 \times 10^{30} \space kg $$
$$ 1 \space kg = 5.02912871 \times 10^{-31} \space M_\odot $$

Find 1 $m$ in terms of $km$.

$$ 1 \space km = 10^3 \space m $$
$$ 1 \space m = 10^{-3} \space km $$ 

Using [time conversion factor](#time-conversion-factor), plug into the formula for a joule.

$$ 1 \space J = (5.02912871 \times 10^{-31} \space M_\odot) \cdot (10^{-3} \space km)^2 \cdot (2.99792458 \times 10^5 \space km)^{-2} $$
$$ 1 \space J = 5.59566034 \times 10^{-48} \space M_\odot $$

Given the [conversion factor](https://en.wikipedia.org/wiki/Electronvolt) between electronvolts and joules

$$ 1 \space eV = 1.602176634 \times 10^{-19} \space J $$
$$ 1 \space J = 6.241509074 \times 10^{18} \space eV $$

Therefore 

$$ 6.241509074 \times 10^{18} \space eV = 5.59566034 \times 10^{-48} \space M_\odot $$
$$ 1 \space eV = 8.96523625 \times 10^{-67} \space M_\odot $$
$$ 10^{-6} \space MeV = 8.96523625 \times 10^{-67} \space M_\odot $$
$$ 1 \space MeV = 8.96523625 \times 10^{-61} \space M_\odot $$

Next, find $km$ in terms of $fm$

$$ 1 \space m = 10^{15} \space fm = 10^{-3} \space km $$
$$ 1 \space fm = 10^{-18} \space km $$
$$ 1 \space fm^3 = 10^{-54} \space km^3 $$

Now, combine these two equations

$$ 1 \space \frac{MeV}{fm^3} = \frac{8.96523625 \times 10^{-61} \space M_\odot}{10^{-54} \space km^3} $$
$$ 1 \space \frac{MeV}{fm^3} = 8.96523625 \times 10^{-7} \space \frac{M_\odot}{km^3} $$

This gives the conversion factor beteween $MeV \cdot fm^{-3}$ and $M_\odot \cdot km^{-3}$

## Gravitational Constant

Starting from non-relativistic units ([source](https://en.wikipedia.org/wiki/Gravitational_constant)):

$$ G = 1.3271244002 \times 10^{11} \space \frac{km^3}{M_\odot \cdot s^2} $$
$$ G = 1.3271244002 \times 10^{11} \space \frac{km^3}{M_\odot \cdot (2.99792458 \times 10^5 \space km)^2} $$
$$ G = \frac{1.3271244002 \times 10^{11}}{2.99792458 \times 10^{10}} \space \frac{km^3}{M_\odot \cdot km^2} $$
$$ G = 4.426810498 \space \frac{km}{M_\odot} $$
