# Slide 4

The continuously compounded return for one period is $\ln(1+r)$, where the simple return satisfies $r>-1$. For small returns, a Taylor expansion around $r=0$ gives the second-order approximation

$$
\ln(1+r) \approx r - \frac{1}{2}r^2.
$$

Taking expectations gives

$$
\mathbb{E}[\ln(1+r)] \approx \mathbb{E}[r] - \frac{1}{2}\mathbb{E}[r^2].
$$

This is an approximation, not an equality: the Taylor remainder is of order $r^3$ near zero, so the approximation is useful when returns are small and the omitted terms are negligible. Assuming the relevant expectations exist, and since $\mathbb{E}[r^2]=\operatorname{Var}(r)+\mathbb{E}[r]^2$, it can also be written

$$
\mathbb{E}[\ln(1+r)] \approx \mathbb{E}[r]
- \frac{1}{2}\operatorname{Var}(r)
- \frac{1}{2}\mathbb{E}[r]^2.
$$

To express this expected log return as a simple geometric return, exponentiate and subtract 1:

$$
\exp\!\left(\mathbb{E}[\ln(1+r)]\right)-1
\approx
\exp\!\left(\mathbb{E}[r]
- \frac{1}{2}\operatorname{Var}(r)
- \frac{1}{2}\mathbb{E}[r]^2\right)-1.
$$

When the exponent is small, use $\exp(x)-1\approx x$. This gives

$$
\exp\!\left(\mathbb{E}[\ln(1+r)]\right)-1
\approx \mathbb{E}[r]
- \frac{1}{2}\operatorname{Var}(r)
- \frac{1}{2}\mathbb{E}[r]^2
\approx \mathbb{E}[r]-\frac{1}{2}\operatorname{Var}(r),
$$

where the last approximation drops the squared-mean term when it is small. This is the familiar mean-minus-half-variance approximation to the simple geometric return.

# Slide 15

Assume the investor can lend or borrow at a risk-free rate $r_f$, and can combine that asset with any portfolio of risky assets. For a risky portfolio $p$, let $\mu_p$ be its expected return and $\sigma_p>0$ its standard deviation. Its Sharpe ratio is

$$
SR(p) \equiv \frac{\mu_p-r_f}{\sigma_p}.
$$

Write a complete portfolio as a fraction $y\geq 0$ invested in $p$ and $1-y$ in the risk-free asset. Its expected return and standard deviation are

$$
\mu_c = r_f + y(\mu_p-r_f),
\qquad
\sigma_c = y\sigma_p.
$$

For any target risk level $\sigma_c>0$, the fraction invested in $p$ must be $y=\sigma_c/\sigma_p$. Substituting this into expected return gives

$$
\mu_c = r_f + \sigma_c\frac{\mu_p-r_f}{\sigma_p}
      = r_f + \sigma_c SR(p).
$$

Thus, at the same risk level, a portfolio with a higher Sharpe ratio delivers a higher expected return. Since a mean-variance investor prefers higher expected return at a given risk level, any complete portfolio using a lower-Sharpe risky portfolio is dominated by one using the risky portfolio with the highest possible Sharpe ratio. The investor chooses that tangency portfolio for the risky part of their investment, then chooses $y$ (and hence their overall risk) according to their risk preferences.

For example, with mean-variance utility $U(\mu_c,\sigma_c)=\mu_c-\frac{\lambda}{2}\sigma_c^2$, where $\lambda>0$, the best utility attainable using $p$ is

$$
\max_{y\geq 0}\left[r_f+y(\mu_p-r_f)-\frac{\lambda}{2}y^2\sigma_p^2\right]
= r_f+\frac{SR(p)^2}{2\lambda},
$$

when $\mu_p>r_f$. This is maximized by the risky portfolio with the largest positive Sharpe ratio. If no risky portfolio has a positive excess return, the investor instead holds the risk-free asset (unless required to hold risky assets).

# Slide 39

## First inequality

Let $\mu_i$ and $\mu_p$ denote expected excess returns over the risk-free rate, and let $\sigma_i,\sigma_p>0$ denote standard deviations. Suppose we allocate weight $w$ to some new investment $i$ and $1-w$ to our existing portfolio $p$. The portfolio excess return and standard deviation are

$$
\mu(w)=w\mu_i+(1-w)\mu_p,
\qquad
\sigma(w)=\sqrt{w^2\sigma_i^2+(1-w)^2\sigma_p^2+2w(1-w)\sigma_i\sigma_p\rho_{ip}}.
$$

Its Sharpe ratio is $\mu(w)/\sigma(w)$. The right-hand derivative of this ratio at $w=0$ is positive if and only if

$$
\left[\sigma(w) (\mu_i - \mu_p) > \mu(w) \frac{d}{dw} \sigma(w)\right]_{w=0}
$$

At that point, the portfolio is $p$, so

$$
\sigma_p (\mu_i - \mu_p) > \mu_p \frac{d}{dw} \sigma(w) \big|_{w=0}
$$

Write out the general expression

$$
\frac{d}{dw}\sigma(w) = \frac{d}{dw} \sigma^2(w)^{1/2} = \frac{1}{2 \sigma(w)} [ 2w\sigma_i^2 - 2(1-w)\sigma_p^2 + 2(1-2w)\sigma_i\sigma_p\rho_{ip}]
$$

and evaluate this at $w=0$

$$
\frac{d}{dw}\sigma(w)\big|_{w=0} = \sigma_i\rho_{ip} - \sigma_p
$$

so a marginal allocation to $i$ improves our Sharpe ratio if and only if

$$
\sigma_p (\mu_i - \mu_p) > \mu_p ( \sigma_i \rho_{ip} - \sigma_p )
$$

$$
\sigma_p \, \mu_i \, > \, \mu_p \, \sigma_i \, \rho_{ip}
$$

$$
\frac{\mu_i}{\sigma_i} > \rho_{ip} \times \frac{\mu_p}{\sigma_p}
$$

This is a local condition: it says whether shifting a small amount from $p$ into $i$ raises the Sharpe ratio, not whether $i$ alone has a higher Sharpe ratio or whether a large allocation will improve it.

## Second inequality

Multiplying the last line by $\sigma_i>0$ rearranges it as

$$
\mu_i > \rho_{ip} \times \frac{\sigma_i}{\sigma_p} \times \mu_p
$$

The multiplier is the beta of $i$ with respect to $p$, $\beta_{ip}\equiv\frac{\operatorname{Cov}(i,p)}{\sigma_p^2}=\rho_{ip}\frac{\sigma_i}{\sigma_p}$. Thus the condition is $\mu_i>\beta_{ip}\mu_p$.

# Slide 42

Let $B$ and $A$ be any two assets.
For intuition, we should imagine that $B$ is a benchmark and $A$ is an "active" portfolio that attempts to beat the benchmark.
For any portfolio $p$ of $B$ and $A$, define:

- Sharpe ratio $SR(p) \equiv \mu_p / \sigma_p$
- Alpha $\alpha_{pB}$ and beta $\beta_{pB}$ are the constant and slope terms from a regression of $r_{p,t}$ on $r_{B,t}$, and $\varepsilon_{pB,t}$ are the residuals from that regression.
- Information ratio $IR(p) \equiv \frac{\alpha_{pB}}{\sigma(\varepsilon_{pB,t})}$.

Let $\ast$ denote the portfolio of $A$ and $B$ that attains the maximal Sharpe ratio.

**Proposition**

$$
SR(*)^2 = SR(B)^2 + IR(A)^2
$$

See BKM (chapter 7) and GK (p137-139, their item 10).

**Proof**

Define the following:

$$
\alpha \equiv \left[\begin{matrix} 0 \\ \alpha_{AB} \end{matrix} \right]
\quad , \quad
\beta \equiv \left[\begin{matrix} 1 \\ \beta_{AB} \end{matrix} \right]
\quad , \quad
f \equiv \left[ \begin{matrix} \mu_B \\ \mu_A \end{matrix} \right]
\quad , \quad
V \equiv \left[ \begin{matrix} \sigma_B^2 & \sigma_{AB} \\ \sigma_{AB} & \sigma_A^2 \end{matrix} \right]
$$

Grinold and Kahn (Prop 2, part 1, p32) set up explicitly the Lagrangian solved by portfolio $\ast$ and show that its holdings are proportional to $\frac{V^{-1}f}{f^{\prime}V^{-1}f}$.
When the expected return of $\ast$ is 1, its variance is

$$
\left(\frac{1}{f'V^{-1}f}\right)^2 (V^{-1}f)' V (V^{-1}f)
=
\left(\frac{1}{f'V^{-1}f}\right)^2 f' V^{-1} V V^{-1} f
=
\frac{1}{f'V^{-1}f}
$$

So $SR(\ast) = f^{\prime}V^{-1}f$.
Substitute the projection $f = \alpha + \mu_B \beta$ and distribute:

$$
SR(*)^2 \quad = \quad
\underbrace{ \alpha' V^{-1} \alpha }_{IR(A)^2}
\quad + \quad
\underbrace{ \mu_B^2 \times \beta'V^{-1}\beta }_{SR(B)^2}
\quad + \quad
\underbrace{ \beta' V^{-1} \alpha }_{=0} + \underbrace{ (\beta' V^{-1} \alpha)' }_{=0}
$$

To complete the proof we can explicitly write out and verify the identities above.
