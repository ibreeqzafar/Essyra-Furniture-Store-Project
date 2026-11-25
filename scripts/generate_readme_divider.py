from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import colorsys, math
W,H,N=1200,58,24
frames=[]
for f in range(N):
 im=Image.new('RGBA',(W,H),(255,0,255,255))
 d=ImageDraw.Draw(im)
 # cast shadow and a beveled rail make the divider read as raised from the page
 d.rounded_rectangle((44,27,W-44,40),radius=7,fill=(0,0,0,95))
 d.rounded_rectangle((44,22,W-44,35),radius=7,fill=(78,80,67,255))
 # animated jewel-toned light flows through a segmented, perspective rail
 for x in range(48,W-48):
  hue=((x/(W-96))*0.72 + f/N) % 1
  r,g,b=colorsys.hsv_to_rgb(hue,0.72,0.95)
  d.line((x,24,x,32),fill=(int(r*255),int(g*255),int(b*255),255),width=1)
 # bevel highlight, tapered ends and traveling glint
 d.line((58,23,W-58,23),fill=(255,245,215,210),width=1)
 pos=58+((f/N)*(W-116))
 d.ellipse((pos-22,19,pos+22,37),fill=(255,255,255,40))
 d.ellipse((pos-6,21,pos+6,33),fill=(255,255,234,245))
 d.ellipse((pos-2,23,pos+2,29),fill=(255,255,255,255))
 # tapered rails suggest depth at both ends
 d.polygon([(44,22),(58,24),(58,33),(44,35)],fill=(228,209,154,255))
 d.polygon([(W-44,22),(W-58,24),(W-58,33),(W-44,35)],fill=(124,112,80,255))
 # GIF transparency uses the unique magenta canvas key
 rgb=im.convert('RGB').quantize(colors=127,method=Image.Quantize.MEDIANCUT)
 key=rgb.getpixel((0,0)); rgb.info['transparency']=key; rgb.info['duration']=85
 frames.append(rgb)
out=Path('docs/readme-color-divider.gif')
frames[0].save(out,save_all=True,append_images=frames[1:],duration=85,loop=0,optimize=True,disposal=2,transparency=frames[0].info['transparency'])
print(f'{out}: {out.stat().st_size:,} bytes · {N} frames')
