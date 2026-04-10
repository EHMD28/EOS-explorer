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

Since the unit of length for this project is kilometers, I'm instead using the following conversion factor.

$$ 1 \space s = 2.99792458 \times 10^8 \space m $$
$$ 1 \space s = 2.99792458 \times 10^5 \space (10^3 \space m) $$
$$ 1 \space s = 2.99792458 \times 10^5 \space km $$

## Gravitational Constant

Starting from non-relativistic units ([source](https://en.wikipedia.org/wiki/Gravitational_constant)):

$$ G = 1.3271244002 \times 10^{11} \space \frac{km^3}{M_\odot \cdot s^2} $$
$$ G = 1.3271244002 \times 10^{11} \space \frac{km^3}{M_\odot \cdot (2.99792458 \times 10^5 \space km)^2} $$
$$ G = \frac{1.3271244002 \times 10^{11}}{2.99792458 \times 10^{10}} \space \frac{km^3}{M_\odot \cdot km^2} $$
$$ G = 4.426810498 \space \frac{km}{M_\odot} $$
