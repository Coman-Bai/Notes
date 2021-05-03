### Oscillation

*Coman Bai, Department of Physics, HEBNU*

* Outline:
  1. Hooke's **Law** and the balance of oscillator
  2. Free oscillator
     * Vibrational Equation
     * Representation Method
     * Important Quantity in Oscillation
     * Superposition of Oscillations
     * Other Classical Model of Harmonic Oscillation
  3. Damping Oscillation
  4. Driven Oscillation
     * Resonance

#### Section 1: Hooke's Law and the balance of oscillation

$$
\vec{F} = -k\vec{x}\tag{1}
$$

$k$ is a constant here, means elasticity coefficient; $x$ is the displacement relative to the original point, as shown in *Figure 1*.

<div align = "center">
    <img src = 01.png width = 900px height = 200px>
</div>
As Eq. 1, elasticity only dependents on the position of the particle($\vec{F}$ is the one-variable function about $x$), so we think this force is conservative, and exist a potential energy corresponds to it.

Elastic potential energy:
$$
E_{p} = \frac{1}{2}kx^{2}\tag{2}
$$
the corresponding figure:

<div align = "center">
    <img src = 02.png width = 350px height = 270px>
</div>
To a system, the key to judge it's balance or not is calculating the resultant force and moment of this system, they correspond the momentum and the angle momentum depends on time or not. But another view is the system is at the stationary state if the state corresponds the extreme small point of the potential function. For this spring oscillator, origin point correspond the stationary state. 

#### Section 2: Free Oscillator

#### A. Vibrational Equation

Combining Newton’s second law and Hooke’s Law, we can get:
$$
\frac{d^{2}x}{dt^{2}}+ \frac{k}{m}x = 0\tag{3}
$$
The solution of Eq. 3 is $x = Ae^{i\omega_{0}t}$, $\omega_{0} = \sqrt{\frac{k}{m}}$ 

About how to obtain the solution of this differential equation, I will mention it in detail in the later lectures. Only the form of the solution is given here.

So we can use equation:
$$
x = Ae^{i\omega_{0}t}\tag{4}
$$
to express the movement of free oscillator.

From the definition, $\omega_{0}$ is always positive. So to another case $x_{1} = A_{1}e^{-i\omega_{0}t}$, it's easy to know all of $x(t)$，$x_{1}(t)$，$x(t)+x_{1}(t)$ are solutions of Eq. 3, that is **sum of  oscillations is also an oscillation**.

#### B. Representation Method

Three representation method are mentioned here, triangle function, Euler formula and phasor.

##### i) Triangle function

To a harmonic oscillator, its vibrational equation also can be expressed by the triangle function(generally, cosine function is used here, the difference between $\sin$ and $\cos$ is just a phase difference). 
$$
x(t) = \cos(\omega_{0}t - \phi_{0})\tag{5}
$$
(Eq.5 is also a solution of Eq 3., so it's also a wave.)

**Some important quantity is shown here:**

1. A : Amplitude
2. $\omega_{0}$: Angle Frequency(specially, $\omega_{0}$ for natural frequency here.)
3. $\phi$: Phase
4. $\phi_{0}$: Initial Phase
5. $T_{0}$: Cycle 

**ii) Euler Formula** 

As we see before, the solution of Eq.5 is an exponential function with a pure imaginary variable, so we can use Euler formula on it:
$$
e^{i\phi} = \cos \phi + i\sin \phi\tag{6}
$$
In our daily calculation, we only need to take the real part of Eq.6, that corresponds the real vibration of oscillator.

*Why explore function?*

In many cases, the operation of exponential functions is easier than that of the triangle equation, and in many aspects, both of them has the same effect(calculate the intensity of waves).

**iii) Phasor**

Expect above two methods, we also use a vector in **polar coordinate** to express an oscillation. called it **phasor**.

<div align = "center">
    <img src = 03.jpeg width = 700px height = 250px>
</div>

The **length(or model)** of the vector in polar coordinate system corresponds the amplitude of the oscillation, and the **argument** corresponds to the phase. As shown in figure, the phasor will rotate with the speed of $\omega$(angle frequency). 

#### C. Superposition Principle and Linear Response System

In experiment, if we give a system two oscillation respectively along $x$ axis and $y$ axis **(step by step)**, we will find the result is the same as give two oscillation to this system **together**, that is:
$$
S(1)+S(2) = S(1+2)\tag{7}
$$
$S(1)$ and $S(2)$ express two oscillations along two different directions respectively, $S(1+2)$ means two oscillations happen to a system **at the same time**.

With phasor representation:

<div align = "center">
    <img src = 04.png width = 270px height = 180px>
</div>

($a$ for $S(1)$, $b$ for $S(2)$ and $F$ for $S(1+2)$)

Promote to general case:

For a signal($S$) if satisfy below equation, we called this signal a **linear response system**.
$$
S(1)+S(2)+\cdots = S(1+2+\cdots)\tag{8}
$$

#### D. Other Classical Harmonic Oscillations

**i) Simple pendulum**

<div align = "center">
    <img src = 05.jpeg width = 250px height = 270px>
</div>

Suppose mass of the ball is $m$ and length of the rope is $l$, from the angle momentum form Newton second law, we can get:


$$
\frac{d\vec{L}}{dt} = -m\vec{g}l\sin \theta
$$
that is,
$$
\frac{d^{2}\theta}{dt^{2}} = -\sqrt{\frac{g}{l}}\sin \theta\tag{9}
$$
as $\theta$ is small, *from* the first order term of Talyor series: 
$$
\sin \theta \sim \theta
$$
so eq. 9 can be expressed by:
$$
\frac{d^{2}\theta}{dt^{2}} + \sqrt{\frac{g}{l}}\theta = 0\tag{10}
$$
Its solution is:
$$
\theta (t) = Ae^{i\omega t}, \omega = \sqrt{\frac{g}{l}}\tag{11}
$$
(P.S.: If we have the boundary condition, we can know its initial phase.)

**ii) Compound pendulum**

Same as the single pendulum, just take the position of centroid!

Skip here

#### Section 3: Damping Oscillation

On the basis of free oscillator, suppose the oscillator receive a resistance proportional to the speed, its feature equation:
$$
\vec{F} = -k\vec{x}-\gamma \vec{c}\tag{11}
$$
Combine with the Newton second law:
$$
\frac{d^{2}x}{dt^{2}} + \frac{\gamma}{m}\frac{dx}{dt}+\frac{k}{m}x = 0\tag{12}
$$
take the simpler notation:
$$
2\beta = \frac{\gamma}{m}; \omega_{0}^{2} = \frac{k}{m}\tag{13}
$$
that is, 
$$
\frac{d^{2}x}{dt^{2}} + 2\beta\frac{dx}{dt}+\omega_{0}x = 0\tag{12}
$$
Its solution:
$$
x(t) = e^{-\beta}e^{i\sqrt{\omega_{0}^{2}-\beta^{2}}t}\tag{13}
$$
**i) $\omega_{0} > \beta$: **

This oscillator do a reduced amplitude vibration;

The first part of Eq. 13($e^{-\beta}$) means a damping factor, that is, amplitude of the oscillator damps with time, the second part($e^{i\sqrt{\omega_{0}^{2}-\beta^{2}}t}$) means the harmonic oscillation, the figure is below:

<div align = "center">
    <img src = 06.jpeg width = 400px height = 270px>
</div>

**ii) $\omega_{0} = \beta$:**

In this case, angle frequency of the second part is 0, the displacement of oscillator is only an exponential relation with time, the correspond figure is:
<div align = "center">
    <img src = 07.jpeg width = 450px height = 270px>
</div>

**iii) $\omega_{0} < \beta$:**

The illstrated is above, the damping factor($\gamma$) is large in this case, so the displacement changed slowly.

#### Section 4: Driven Oscillation

Based on the damping oscillator, suppose the oscillator receive a driven force: $F = e^{i\omega't}$ 

Its feature equation:
$$
\vec{F} = -k\vec{x} - \gamma \vec{v} + F_{0}e^{i\omega't}\tag{14}
$$
take the simpler notation: 
$$
2\beta = \frac{\gamma}{m}; \omega_{0}^{2} = \frac{k}{m}; h = \frac{F_{0}}{m}
$$
that is, 
$$
\frac{d^{2}x}{dt^{2}} + 2\beta\frac{dx}{dt} + hx = 0\tag{15} 
$$
Its solution:
$$
x(t) = Ae^{i\omega' t-\phi}
$$
$A$ is the amplitude here, its value is:
$$
A = \frac{h}{\sqrt{(\omega_{0}^{2}-\omega'^{2})^{2}+4\beta^{2}\omega'^{2}}}
$$
$\phi$ is the initial phase of this oscillator:
$$
\phi = \arctan \frac{2\beta\omega'}{\omega_{0}^{2}-\omega^{2}}
$$
**An important thing: The frequency of the driven oscillator is the same as that of driven force.**

There is a phase difference between the displacement of oscillator with the driven force, $\phi = \arctan \frac{2\beta\omega'}{\omega_{0}^{2}-\omega^{2}}$, means there exits a "lag" between force and oscillator(exist a relaxation time when the driven force acts on the free or damping oscillator).

**Resonance**

The expression of amplitude of driven oscillator is:
$$
A = \frac{h}{\sqrt{(\omega_{0}^{2}-\omega'^{2})^{2}+4\beta^{2}\omega'^{2}}}
$$
as $\omega' = \omega_{0}$, the value of $A$ will be the maximum, and we call this phenomenon: **resonance**.

That is, when **the frequency of the driven force is the same as the natural frequency of that oscillator**, the amplitude of the oscillator will be **maximum**.