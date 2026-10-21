import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
# Model spectrum of Pope (2000), Turbulent Flows, eqs 6.246-6.248
nu=1.0e-6; L=1.0; C=1.5; p0=2; cL=6.78; beta=5.2; ceta=0.40
k=np.logspace(-1,5,800)
def E(eps):
    eta=(nu**3/eps)**0.25
    fL=(k*L/np.sqrt((k*L)**2+cL))**(5/3+p0)
    fe=np.exp(-beta*(((k*eta)**4+ceta**4)**0.25-ceta))
    return C*eps**(2/3)*k**(-5/3)*fL*fe, eta
cols={1e-10:"#6da7ec",1e-8:"#2a78d6",1e-6:"#104281"}
plt.rcParams.update({"font.size":11,"axes.edgecolor":"#52514e","axes.labelcolor":"#0b0b0b",
 "xtick.color":"#52514e","ytick.color":"#52514e"})
fig,ax=plt.subplots(figsize=(7.2,4.4),dpi=150); fig.patch.set_facecolor("#fcfcfb"); ax.set_facecolor("#fcfcfb")
for eps,c in cols.items():
    e,eta=E(eps); ax.loglog(k,e,color=c,lw=2)
    kk=1/eta; ax.plot([kk],[np.interp(kk,k,e)],"o",ms=8,color=c,mec="#fcfcfb",mew=2)
    exp=int(np.log10(eps)); lab={1e-10:"1 cm",1e-8:"3 mm",1e-6:"1 mm"}[eps]
    ax.text(0.12,np.interp(0.12,k,e)*3.5,f"ε = 10$^{{{exp}}}$ W kg$^{{-1}}$",fontsize=9.5,color="#0b0b0b")
    ax.annotate(f"η ≈ {lab}",(kk,np.interp(kk,k,e)),xytext=(10,-2),textcoords="offset points",fontsize=9.5,color="#0b0b0b",va="center")
kr=np.logspace(0.8,2.0,10); ax.loglog(kr,4e-4*kr**(-5/3),color="#52514e",lw=1.2,ls="--")
ax.text(30,1.2e-6,"k$^{-5/3}$",color="#52514e")
ax.set_xlim(1e-1,1e5); ax.set_ylim(1e-16,1e-3)
ax.set_xlabel("Wavenumber k (rad m$^{-1}$)   →   smaller eddies")
ax.set_ylabel("Kinetic energy spectrum E(k) (m$^3$ s$^{-2}$)")
for s in ["top","right"]: ax.spines[s].set_visible(False)
ax.grid(True,which="major",color="#e6e5e1",lw=0.6); ax.set_axisbelow(True)
ax.text(1.2,2e-4,"large eddies:\nenergy input",fontsize=9.5,color="#52514e",ha="center")
ax.text(2.2e2,1.5e-5,"inertial range:\nenergy passed to\nsmaller eddies",fontsize=9.5,color="#52514e")
ax.text(4e3,1e-9,"viscous range:\nenergy → heat",fontsize=9.5,color="#52514e")
fig.tight_layout(); fig.savefig("energy_cascade.png",facecolor=fig.get_facecolor())
for eps in cols: print(eps,(nu**3/eps)**0.25)
