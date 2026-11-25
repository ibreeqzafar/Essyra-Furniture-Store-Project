from PIL import Image, ImageDraw
from pathlib import Path
import math
W,H,N=1400,14,28
# One shared GIF palette avoids transparency flicker; index 0 is transparent.
key=(255,0,255)
stops=[(0.0,(67,82,67)),(.28,(101,118,93)),(.46,(155,150,116)),(.5,(222,211,181)),(.54,(155,150,116)),(.72,(101,118,93)),(1.0,(67,82,67))]
def sample(t):
 for i in range(len(stops)-1):
  a,ca=stops[i]; b,cb=stops[i+1]
  if t<=b:
   q=(t-a)/(b-a); return tuple(round(ca[k]*(1-q)+cb[k]*q) for k in range(3))
 return stops[-1][1]
colors=[key]
for i in range(255): colors.append(sample(i/254))
pal=Image.new('P',(1,1)); flat=[]
for c in colors: flat.extend(c)
pal.putpalette(flat)
frames=[]
for f in range(N):
 im=Image.new('RGB',(W,H),key); d=ImageDraw.Draw(im)
 # Fine 1 px rail and a faint lower edge for a small raised-line effect.
 for x in range(30,W-30):
  t=(x-30)/(W-60); c=sample(t)
  d.point((x,7),fill=(39,49,39))
  d.point((x,6),fill=c)
 # Narrow ivory glint travels along the rail; the line remains hair-thin.
 x0=30+round((W-60)*f/N)
 for dx,c in [(-2,(155,150,116)),(-1,(222,211,181)),(0,(250,245,231)),(1,(222,211,181)),(2,(155,150,116))]:
  d.point((x0+dx,6),fill=c)
 p=im.quantize(palette=pal,dither=Image.Dither.NONE)
 frames.append(p)
out=Path('docs/readme-color-divider.gif')
frames[0].save(out,save_all=True,append_images=frames[1:],duration=80,loop=0,optimize=False,disposal=2,transparency=0,include_color_table=False)
print(f'Updated neutral ESSYRA hairline: {W}x{H}, 1 px stroke, fixed palette, no purple.')
