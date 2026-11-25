from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
W,H,N=1400,20,32
# ESSYRA's forest/sage/brass/ivory, kept soft to match the reference hairline.
stops=[(0.00,(80,96,75)),(.25,(125,139,109)),(.49,(193,174,132)),(.5,(245,239,223)),(.51,(193,174,132)),(.75,(125,139,109)),(1.00,(80,96,75))]
def sample(t):
 for i in range(len(stops)-1):
  a,ca=stops[i]; b,cb=stops[i+1]
  if t<=b:
   q=(t-a)/(b-a); return tuple(round(ca[k]*(1-q)+cb[k]*q) for k in range(3))
 return stops[-1][1]
frames=[]
for f in range(N):
 canvas=Image.new('RGBA',(W,H),(255,0,255,255))
 # diffuse 3D glow beneath a very fine gradient rail
 glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
 for x in range(24,W-24):
  t=(x-24)/(W-49); c=sample(t); fade=min(1,t/.16,(1-t)/.16)
  gd.line((x,9,x,11),fill=(*c,int(72*fade)),width=1)
 glow=glow.filter(ImageFilter.GaussianBlur(2.5)); canvas.alpha_composite(glow)
 # slim underside and the 1px colored beam
 d=ImageDraw.Draw(canvas)
 for x in range(24,W-24):
  t=(x-24)/(W-49); fade=max(0,min(1,t/.12,(1-t)/.12)); c=sample(t)
  d.point((x,10),fill=(31,42,32,int(155*fade)))
  d.point((x,9),fill=(*c,int(255*fade)))
 # a small animated highlight glides across the rail without making it bulky
 px=24+round((W-49)*f/N)
 beam=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(beam)
 bd.ellipse((px-26,7,px+26,13),fill=(243,236,218,90))
 bd.ellipse((px-8,7,px+8,12),fill=(247,241,227,210))
 bd.ellipse((px-2,7,px+2,11),fill=(255,253,244,255))
 beam=beam.filter(ImageFilter.GaussianBlur(1.2)); canvas.alpha_composite(beam)
 rgb=canvas.convert('RGB').quantize(colors=127,method=Image.Quantize.MEDIANCUT)
 frames.append(rgb)
out=Path('docs/readme-color-divider.gif')
frames[0].save(out,save_all=True,append_images=frames[1:],duration=65,loop=0,optimize=True,disposal=2,transparency=frames[0].getpixel((0,0)))
print(f'Updated to a soft, thin, flowing 3D hairline: {out.stat().st_size:,} bytes')
