"""Stirring vs mixing: a blob of tracer in a 'random sine flow' (alternating sinusoidal shears),
with weak and with stronger diffusion. Illustration made for this course."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates
n=384; x=np.arange(n)/n; X,Y=np.meshgrid(x,x)
c0=np.exp(-((X-0.5)**2+(Y-0.5)**2)/(2*0.07**2))
k=np.fft.fftfreq(n,1/n)*2*np.pi; KX,KY=np.meshgrid(k,k); K2=KX**2+KY**2
rng=np.random.default_rng(3); phases=rng.uniform(0,2*np.pi,(12,2)); A=0.3
def run(kappa,steps):
    c=c0.copy()
    for i in range(steps):
        ph=phases[i]
        # shear in x: x -> x + A sin(2pi y + ph0)  (semi-Lagrangian, backward)
        xs=(X - A*np.sin(2*np.pi*Y+ph[0]))%1; c=map_coordinates(c,[Y*n,xs*n],order=3,mode="grid-wrap")
        ys=(Y - A*np.sin(2*np.pi*X+ph[1]))%1; c=map_coordinates(c,[ys*n,X*n],order=3,mode="grid-wrap")
        c=np.real(np.fft.ifft2(np.fft.fft2(c)*np.exp(-kappa*K2)))
    return c
panels=[(c0,"Initial blob"),(run(1e-6,7),"Stirring\n(eddies stretch and fold)"),(run(1.2e-4,7),"Stirring + diffusion\n= mixing")]
fig,axs=plt.subplots(1,3,figsize=(8.6,3.3),dpi=150); BG="#fcfcfb"; fig.patch.set_facecolor(BG)
for ax,(c,t) in zip(axs,panels):
    ax.imshow(c,cmap="Blues",vmin=0,vmax=1,origin="lower"); ax.set_title(t,fontsize=10.5,color="#0b0b0b"); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color("#c3c2b7")
    ax.text(0.03,0.04,f"max = {c.max():.2f}",transform=ax.transAxes,fontsize=9,color="#52514e")
fig.tight_layout(); fig.savefig("stirring_mixing.png",facecolor=BG)
