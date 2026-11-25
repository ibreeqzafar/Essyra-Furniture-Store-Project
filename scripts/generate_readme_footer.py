from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
W,H=1200,360
frames=[]
serif='C:/Windows/Fonts/georgia.ttf'; sans='C:/Windows/Fonts/arial.ttf'
try: logo=ImageFont.truetype(serif,62); tagline=ImageFont.truetype(sans,14); label=ImageFont.truetype(sans,16); small=ImageFont.truetype(sans,12)
except: logo=tagline=label=small=ImageFont.load_default()
steps=['DISCOVER','IMAGINE','CHOOSE','MAKE IT YOURS']
xs=[105,360,615,870]
for frame in range(24):
 t=frame/24
 im=Image.new('RGB',(W,H),(25,34,28)); px=im.load()
 for y in range(H):
  shade=int(5*(1-y/H))
  for x in range(W): px[x,y]=(25+shade,34+shade,28+shade)
 d=ImageDraw.Draw(im)
 d.text((W//2+3,78+4),'ESSYRA',font=logo,fill=(91,82,58),anchor='mm')
 d.text((W//2+1,78+2),'ESSYRA',font=logo,fill=(154,135,90),anchor='mm')
 d.text((W//2,78),'ESSYRA',font=logo,fill=(246,241,229),anchor='mm')
 d.text((W//2,128),'FIND THE SOUL OF YOUR PLACE',font=tagline,fill=(191,190,177),anchor='mm')
 # shallow perspective rail and moving light tracer
 y0=222
 d.line((102,y0+7,1097,y0-7),fill=(103,111,93),width=4)
 d.line((102,y0+4,1097,y0-10),fill=(172,151,102),width=1)
 for i,(x,word) in enumerate(zip(xs,steps)):
  cx=x+105; cy=y0+int((x-100)*-.014)
  active=(int(t*4)%4)==i
  fill=(51,62,49) if active else (31,42,34)
  border=(214,190,126) if active else (104,111,94)
  # subtle offset gives each typographic tile a raised, dimensional edge
  d.rounded_rectangle((x+5,cy-22+7,x+215+5,cy+24+7),radius=13,fill=(12,18,14))
  d.rounded_rectangle((x,cy-22,x+215,cy+24),radius=13,fill=fill,outline=border,width=2)
  d.line((x+15,cy-17,x+200,cy-17),fill=(105,111,96),width=1)
  d.text((cx,cy+1),word,font=label,fill=(245,239,222) if active else (202,201,188),anchor='mm')
 # animated glint travels along the path between stages
 pos=102+((frame/24)*995)
 gy=y0+4-(pos-102)*.014
 d.ellipse((pos-8,gy-8,pos+8,gy+8),fill=(217,190,124))
 d.ellipse((pos-3,gy-3,pos+3,gy+3),fill=(255,248,221))
 d.text((W//2,315),'EXPLORE  ·  DESIGN  ·  MAKE IT YOURS',font=small,fill=(164,174,158),anchor='mm')
 frames.append(im.quantize(colors=96,method=Image.Quantize.MEDIANCUT))
out=Path('docs/essyra-footer-motion.gif')
frames[0].save(out,save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True,disposal=2)
print(f'{out}: {out.stat().st_size} bytes, {len(frames)} frames')
