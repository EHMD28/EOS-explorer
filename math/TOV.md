# Tolman-Oppenheimer-Volkoff Equation

The general relativistic form of the TOV equation is as follows [1].

$$
\frac{dP(r)}{dr} = 
-\frac{G m_r(r) \varepsilon(r)}{r^2}
\left(1 + \frac{P(r)}{\varepsilon(r)}\right)
\left(1 + \frac{4\pi r^3 P(r)}{m_r(r)}\right)
\left(1 - \frac{2 G m_r(r)}{r}\right)^{-1}
$$

$r$ = Radius

$P$ = Pressure

$\varepsilon$ = Energy Density

$m_r$ = Enclosed Mass

$G$ = Gravitational Constant

## Dimensionless TOV Equation

By introducing the following scaling constants, it's possible to convert the TOV equation to a dimensionless form.

$$ P = \varepsilon_0 \cdot P' $$
$$ \varepsilon = \varepsilon_0 \cdot \varepsilon' $$
$$ r = a \cdot r' $$
$$ m_r = b \cdot m_r' $$

All of the primed variables represent dimensionless quantities of the corresponding value. $\varepsilon_0$ has units of energy density/pressure, $a$ has units of length, and $b$ has units of mass.

After plugging into the [TOV](#tolman-oppenheimer-volkoff-equation) equation, there are still some dimensional quantities left. To cancel those, the following equations must be true.

$$ G \cdot b = a $$
$$ a^3 \cdot \varepsilon_0  = b $$

These equations hold true for 

$$ a = (G \cdot \varepsilon_0)^{-1/2} $$
$$ b =  (G^3 \cdot \varepsilon_0)^{-1/2} $$

The fully dimensionless TOV equation reads

$$
\frac{dP'}{dr'} =
-\frac{m_r' \varepsilon'}{r'^2}
\left(1 + \frac{P'}{\varepsilon'} \right)
\left(1 + \frac{4\pi r'^3 P'}{m_r'} \right)
\left(1 - \frac{2 m_r'}{r'} \right)^{-1}
$$

The mass-conservation equation scales as one would expect

$$ \frac{d m_r'}{dr'} = 4\pi r'^2 \varepsilon' $$

Note that the equations are now reliant on an EoS of the form $P'(\varepsilon')$.

## Sources

1. Compact Star Physics by Jürgen Schaffner-Bielich
