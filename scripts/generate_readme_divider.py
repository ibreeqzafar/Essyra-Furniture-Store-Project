from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import math
W,H,N=1400,24,24
# ESSYRA palette: deep forest, muted sage, warm brass, ivory.
stops=[(0.00,(42,55,43)),(0.23,(83,101,79)),(0.46,(174,153,105)),(0.50,(244,239,224)),(0.54,(174,153,105)),(0.77,(83,101,79)),(1.00,(42,55,43))]
def color_at(t):
 for i in range(len(stops)-1):
  a,ca=stops[i]; b,cb=stops[i+1]
  if t<=b:
   q=(t-a)/(b-a)
   return tuple(round(ca[k]*(1-q)+cb[k]*q) for k in range(3))
 return stops[-1][1]
frames=[]
for f in range(N):
 bg=(255,0,255,255)
 im=Image.new('RGBA',(W,H),bg)
 # soft diffused glow follows the reference line while staying in the brand palette
 glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
 for x in range(W):
  t=x/(W-1); c=color_at(t)
  fade=min(1,t/.12,(1-t)/.12)
  gd.line((x,10,x,14),fill=(*c,int(115*fade)),width=1)
 glow=glow.filter(ImageFilter.GaussianBlur(3.2)); im.alpha_composite(glow)
 d=ImageDraw.Draw(im)
 # inset dark bevel plus luminous fine core emulate a raised, drawn 3D rail
 for x in range(W):
  t=x/(W-1); c=color_at(t); fade=max(0,min(1,t/.07,(1-t)/.07))
  d.line((x,10,x,13),fill=(17,25,19,150),width=1)
  d.line((x,9,x,11),fill=(*c,int(245*fade)),width=1)
 # traveling ivory glint over the fixed brand gradient
 phase=(f/N)
 pos=round(35+phase*(W-70))
 d.ellipse((pos-10,5,pos+10,17),fill=(199,177,124,65))
 d.ellipse((pos-4,6,pos+4,14),fill=(242,237,222,255))
 d.ellipse((pos-1,7,pos+1,10),fill=(255,255,248,255))
 # magenta is a unique transparency key, never part of the ESSYRA palette
 p=im.convert('RGB').quantize(colors=127,method=Image.Quantize.MEDIANCUT)
 p.info['transparency']=p.getpixel((0,0))
 frames.append(p)
out=Path('docs/readme-color-divider.gif')
frames[0].save(out,save_all=True,append_images=frames[1:],duration=75,loop=0,optimize=True,disposal=2,transparency=frames[0].info['transparency'])
print(f'{out}: {out.stat().st_size:,} bytes; ESSYRA forest/sage/brass/ivory palette')
