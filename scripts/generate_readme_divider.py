from PIL import Image, ImageDraw
from pathlib import Path
W,H,N=1400,8,24
stops=[(0.0,(48,62,50)),(.28,(92,108,85)),(.5,(177,157,112)),(.72,(92,108,85)),(1.0,(48,62,50))]
def color(t):
 for i in range(len(stops)-1):
  a,ca=stops[i]; b,cb=stops[i+1]
  if t<=b:
   q=(t-a)/(b-a); return tuple(round(ca[k]*(1-q)+cb[k]*q) for k in range(3))
 return stops[-1][1]
frames=[]
for f in range(N):
 im=Image.new('RGB',(W,H),(255,0,255)); d=ImageDraw.Draw(im)
 # Hairline shadow and 1 px muted brand gradient.
 d.line((28,4,W-28,4),fill=(15,22,17),width=2)
 for x in range(28,W-28):
  c=color(x/(W-1)); d.point((x,3),fill=c)
 # A restrained ivory glint travels along the single-pixel line.
 x=28+round((W-56)*f/N)
 d.point((x,3),fill=(243,238,223))
 p=im.quantize(colors=127,method=Image.Quantize.MEDIANCUT)
 frames.append(p)
out=Path('docs/readme-color-divider.gif')
frames[0].save(out,save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True,disposal=2,transparency=frames[0].getpixel((0,0)))
print(f'{out}: {out.stat().st_size:,} bytes, {W}x{H}, 1px line')
