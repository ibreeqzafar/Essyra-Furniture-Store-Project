from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
text='Considered furniture. Personal spaces.'
W,H,N=1000,72,48
key=(255,0,255)
cream=(244,239,225); brass=(190,169,121); shadow=(72,82,67); forest=(48,62,50)
palette=[key,cream,brass,shadow,forest]
# Repeat available palette values to build a stable transparency-safe GIF palette.
flat=[]
for i in range(256): flat.extend(palette[i%len(palette)])
pal=Image.new('P',(1,1)); pal.putpalette(flat)
try: font=ImageFont.truetype('C:/Windows/Fonts/georgia.ttf',30)
except: font=ImageFont.load_default()
tmp=Image.new('RGB',(1,1)); measure=ImageDraw.Draw(tmp); width=measure.textbbox((0,0),text,font=font)[2]
x=max(18,(W-width)//2); y=17
frames=[]
for f in range(N):
 im=Image.new('RGB',(W,H),key); d=ImageDraw.Draw(im)
 # Type the line on, then hold it briefly before the loop starts again.
 shown=min(len(text),max(0,f-1))
 part=text[:shown]
 # Small offset brass extrusion creates a restrained raised-letter effect.
 d.text((x+2,y+2),part,font=font,fill=shadow)
 d.text((x+1,y+1),part,font=font,fill=brass)
 d.text((x,y),part,font=font,fill=cream)
 cursor_x=x+measure.textbbox((0,0),part,font=font)[2]
 if shown<len(text) or f>=len(text)+4:
  if (f//3)%2==0:
   d.rounded_rectangle((cursor_x+3,y+2,cursor_x+5,y+39),radius=1,fill=brass)
 p=im.quantize(palette=pal,dither=Image.Dither.NONE)
 frames.append(p)
out=Path('docs/essyra-tagline-typewriter.gif')
frames[0].save(out,save_all=True,append_images=frames[1:],duration=85,loop=0,optimize=False,disposal=2,transparency=0,include_color_table=False)
print(f'Created {out}: {len(text)} characters, typewriter loop, embossed shadow, no background art.')
