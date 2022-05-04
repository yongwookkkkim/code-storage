from scipy import stats
import numpy as np

lnx=[np.log(z) for z in x]
res=stats.linregress(lnx,y)
print(f"R-squared: {res.rvalue**2:.6f}")
plt.scatter(lnx,y,s=4,label="experimental data")
regressy=[res.intercept+res.slope*k for k in lnx]
plt.plot(lnx, regressy, color='r', label=f"R-squared: {res.rvalue**2:.6f}")
plt.title("sqrt(x)")
plt.legend()
plt.show()