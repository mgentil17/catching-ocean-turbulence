"""Idealized profiles of temperature, nitrate and oxygen in a stratified tropical ocean.
Shapes are illustrative only (not data)."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
z=np.linspace(0,300,600); mld=40; zt=80
T=11+(27.5-11)*0.5*(1-np.tanh((z-zt)/35))
T=np.where(z<mld,T[np.argmin(abs(z-mld))],T)
NO3=25*0.5*(1+np.tanh((z-zt-15)/30)); NO3=np.where(z<mld,NO3[np.argmin(abs(z-mld))],NO3)
O2=200-110*0.5*(1+np.tanh((z-zt-20)/40)); O2=np.where(z<mld,O2[np.argmin(abs(z-mld))],O2)
INK="#0b0b0b"; INK2="#52514e"; BG="#fcfcfb"
plt.rcParams.update({"font.size":11,"axes.edgecolor":INK2,"xtick.color":INK2,"ytick.color":INK2,"axes.labelcolor":INK})
fig,axs=plt.subplots(1,3,figsize=(8.6,4.4),sharey=True,dpi=150); fig.patch.set_facecolor(BG)
data=[(T,"Temperature (°C)","#e34948","heat","down"),(NO3,"Nitrate (µmol kg$^{-1}$)","#1baf7a","nutrients","up"),(O2,"Oxygen (µmol kg$^{-1}$)","#2a78d6","oxygen","down")]
for ax,(v,lab,c,name,d) in zip(axs,data):
    ax.set_facecolor(BG); ax.axhspan(0,mld,color="#f0efec"); ax.axhspan(mld,140,color="#e6e5e1",alpha=0.6)
    ax.plot(v,z,color=c,lw=2.2); ax.set_xlabel(lab)
    for s in ["top","right"]: ax.spines[s].set_visible(False)
    x0=np.interp(mld+25,z,v)+0.08*(v.max()-v.min())
    y1,y2=(mld-5,mld+55) if d=="down" else (mld+55,mld-5)
    ax.annotate("",xy=(x0,y2),xytext=(x0,y1),arrowprops=dict(arrowstyle="-|>",lw=2,color=INK))
    ax.text(x0+0.03*(v.max()-v.min()),mld+28,name+"\n"+d,fontsize=10,color=INK,va="center")
axs[0].set_ylim(300,0); axs[0].set_ylabel("Depth (m)")
axs[0].text(axs[0].get_xlim()[0]+0.3,20,"surface mixed layer",fontsize=9.5,color=INK2,va="center")
axs[0].text(axs[0].get_xlim()[1]-0.3,125,"thermocline",fontsize=9.5,color=INK2,va="center",ha="right")
axs[0].text(axs[0].get_xlim()[1]-0.3,220,"interior",ha="right",fontsize=9.5,color=INK2,va="center")
fig.tight_layout(); fig.savefig("vertical_exchange.png",facecolor=BG)
