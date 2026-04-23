# Calculations

## System of Units

- Length: Kilometers (km)
- Mass: Solar Masses (M$_\odot$)
- Time: Seconds (s)
- Energy Density/Pressure: Megaelectronvolts per cubic femtometer (MeV $\cdot$ fm<sup>3</sup>)

## Relativistic Units

Many of the calculations utilize a relativistic system of units where the speed of light ($c$) is a dimensionless value equal to 1. This leads to the ability to express length as a unit of time. [Further reading](https://physicspages.com/pdf/Relativity/Relativistic%20units.pdf).

$$ c = L \cdot T^{-1} $$
$$ 1 = L \cdot T^{-1} $$
$$ T = L $$

where $L$ is a unit of length and $T$ is a unit of time. To convert an meters-kilograms-seconds (MKS) value to relativistic units, simply use the following.

$$ c = 1 = 2.99792458 \times 10^8 \space m \cdot s^{-1} $$
$$ 1 \space s = 2.99792458 \times 10^8 \space m $$

## Radius Scaling

The relativistic, dimensionless scaling for radius is ([see TOV.md](TOV.md#dimensionless-tov-equation))

$$ r = a \cdot r'$$
$$ [r] = [a] \cdot [r'] $$

Since $r'$ is dimensionless, $[r'] = 1$. Thus, $[r]=[a]$

$$ a = (G \cdot \varepsilon_0)^{-1/2} $$
$$ a = G^{-1/2} \cdot \varepsilon_0^{-1/2} $$
$$ [a] = [G]^{-1/2} \cdot [\varepsilon_0]^{-1/2} $$

$[G] = L^3 \cdot M^{-1} \cdot T^{-2}$ and
$[\varepsilon_0] = L^{-1} \cdot M \cdot T^{-2}$

$$ [a]= (L^3 \cdot M^{-1} \cdot T^{-2})^{-1/2} \cdot (L^{-1} \cdot M \cdot T^{-2})^{-1/2} $$
$$ [a] = L^{-3/2} \cdot M^{1/2} \cdot T \cdot L^{1/2} \cdot M^{-1/2} \cdot T $$
$$ [a] =  L^{-1} \cdot T^{2} $$

Since a has the same dimension as radius, it should be a unit of length ($[a] = L$). However

$$[a] = L \cdot (L^{-2} \cdot T^2) $$

For $a$ to represent a physical quantity, it must be multiplied by a quantity with a dimension of $L^2 \cdot T^{-2}$. In this case, that quantity is $c$, specifically $c^2$ (since that's what everything is scaled by).

$$ r_{rel} = a_{rel} \cdot r'$$
$$ r_{phys} = r_{rel} \cdot c^2$$

## Mass Rescaling

The process for rescaling mass is almost identical to the process for [rescaling radius](#radius-scaling).

$$ m_r = b \cdot m_r' $$
$$ [m_r] = [b] $$

By definition

$$ b = (G^3 \cdot \varepsilon_0)^{-1/2} $$
$$ b = G^{-3/2} \cdot \varepsilon_0^{-1/2} $$

Therefore

$$ [b] = (L^3 \cdot M^{-1} \cdot T^{-2})^{-3/2} \cdot (L^{-1} \cdot M \cdot T^{-2})^{-1/2}$$
$$ [b] = L^{-9/2} \cdot M^{3/2} \cdot T^{3} \cdot L^{1/2} \cdot M^{-1/2} \cdot T $$
$$ [b] = L^{-4} \cdot M \cdot T^4  $$

$b$ should have a dimension of mass, so it must be multiplied by $c^4$.

$$ m_{rel} = b \cdot m_r' $$
$$ m_{phys} = m_{rel} \cdot c^4 $$
