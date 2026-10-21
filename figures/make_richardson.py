"""Idealized equatorial profiles: zonal velocity with an undercurrent, N^2, S^2 and Ri.
Shapes are illustrative only (not data)."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
z=np.linspace(2,200,800); g=9.81; rho0=1025
u=-0.6*np.exp(-z/45)+1.1*np.exp(-((z-75)/24)**2)               # westward surface flow, eastward undercurrent core ~70 m
rho=1022.5+3.5*0.5*(1+np.tanh((z-80)/40))+0.004*z   # pycnocline around 75 m
N2=g/rho0*np.gradient(rho,z); S2=np.gradient(u,z)**2; Ri=N2/S2
INK="#0b0b0b"; INK2="#52514e"; BG="#fcfcfb"
plt.rcParams.update({"font.size":11,"axes.edgecolor":INK2,"xtick.color":INK2,"ytick.color":INK2,"axes.labelcolor":INK})
fig,axs=plt.subplots(1,3,figsize=(8.6,4.4),sharey=True,dpi=150); fig.patch.set_facecolor(BG)
low=Ri<0.25
for ax in axs:
    ax.set_facecolor(BG)
    for s in ["top","right"]: ax.spines[s].set_visible(False)
    # shade depths where Ri < 1/4
    edges=np.flatnonzero(np.diff(low.astype(int)))
    zs=z[edges]
    for a,b in zip(zs[::2],zs[1::2]): ax.axhspan(a,b,color="#fde7c2",zorder=0)
axs[0].plot(u,z,color="#2a78d6",lw=2.2); axs[0].axvline(0,color="#c3c2b7",lw=1)
axs[0].set_xlabel("Zonal velocity u (m s$^{-1}$)")
axs[0].text(0.62,70,"undercurrent\ncore",fontsize=9.5,color=INK2,va="center")
axs[1].semilogx(N2,z,color="#e34948",lw=2.2,label="N$^2$ (stratification)")
axs[1].semilogx(S2,z,color="#2a78d6",lw=2.2,label="S$^2$ (shear)")
axs[1].set_xlabel("N$^2$, S$^2$ (s$^{-2}$)"); axs[1].set_xlim(1e-6,1e-2)
axs[1].legend(frameon=False,fontsize=9.5,loc="lower left")
axs[2].semilogx(Ri,z,color=INK,lw=2.2); axs[2].axvline(0.25,color="#eb6834",lw=1.5,ls="--")
axs[2].text(0.27,190,"Ri = 1/4",color="#eb6834",fontsize=9.5)
axs[2].set_xlim(1e-2,1e2); axs[2].set_xlabel("Richardson number Ri = N$^2$/S$^2$")
axs[0].set_ylim(200,0); axs[0].set_ylabel("Depth (m)")
fig.tight_layout(); fig.savefig("richardson_idealized.png",facecolor=BG)
print(z[low].min() if low.any() else None, z[low].max() if low.any() else None)
