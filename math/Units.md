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

As long as $G$ and $\varepsilon_0$ are using the same system of units, $r_{phys}$ will be in the base unit of length. For the sake of simplicity, the project just uses SI units. Therefore, $r_{phys}$ is in units of meters. To conver to kilometers, simply divide by 1000: $r_{km} = r_{phys} \div 1000$.

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

As long as $G$ and $\varepsilon_0$ are using the same system of units, $m_{phys}$ will be in the base unit of mass. For the sake of simplicity, the project just uses SI units. Therefore, $m_{phys}$ is in units of meters. To conver to solar masses, simply divide by by the [mass of the sun](https://en.wikipedia.org/wiki/Solar_mass). $m_{M \odot} = m_{kg} \div (1.988416 \times 10^{30})$.
