from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math, os
from pathlib import Path
root=Path('.')
out=root/'docs/essyra-portfolio-motion.gif'
shots=[Image.open(root/'docs/screenshots/home-navigation.png').convert('RGB'),Image.open(root/'docs/screenshots/design-studio.png').convert('RGB'),Image.open(root/'docs/screenshots/essyra-care.png').convert('RGB')]
W,H=1200,680
frames=[]
# Render the vignette once at low resolution, then enlarge it for speed.
grad=Image.new('RGB',(120,68)); gp=grad.load()
for yy in range(68):
 for xx in range(120):
  g=max(0,1-math.sqrt(((xx*10-850)/680)**2+((yy*10-350)/520)**2))
  gp[xx,yy]=(int(25+22*g),int(34+22*g),int(28+13*g))
grad=grad.resize((W,H),Image.Resampling.BILINEAR)
font_paths=['C:/Windows/Fonts/georgia.ttf','C:/Windows/Fonts/arial.ttf']
def font(path,size):
 try:return ImageFont.truetype(path,size)
 except:return ImageFont.load_default()
serif=font(font_paths[0],58); sans=font(font_paths[1],14); tiny=font(font_paths[1],12)
for f in range(32):
 t=2*math.pi*f/32
 bg=grad.copy()
 d=ImageDraw.Draw(bg)
 d.text((58,42),'CONSIDERED FURNITURE  ·  PERSONAL SPACES',font=sans,fill=(210,198,154))
 d.text((54,74),'ESSYRA',font=serif,fill=(247,242,230),stroke_width=0)
 d.text((60,145),'FIND THE SOUL OF YOUR PLACE',font=tiny,fill=(203,198,182))
 d.line((60,177,360,177),fill=(169,151,105),width=2)
 d.text((60,192),'A digital home for considered living.',font=font(font_paths[0],22),fill=(235,229,215))
 d.text((60,634),'DISCOVER     DESIGN     MAKE YOUR SPACE YOURS',font=tiny,fill=(177,183,168))
 # gently moving floor glow
 floor=Image.new('RGBA',(W,H),(0,0,0,0)); fd=ImageDraw.Draw(floor)
 fd.ellipse((230,440,1150,710),fill=(4,8,5,105)); floor=floor.filter(ImageFilter.GaussianBlur(42)); bg=Image.alpha_composite(bg.convert('RGBA'),floor)
 # cards float at different phases; center panel comes forward in scale
 configs=[(0,210,318,.72,-8),(1,466,236,.87,1),(2,762,310,.73,8)]
 for idx,x,y,scale,angle in configs:
  phase=t + idx*2.0
  bob=math.sin(phase)*8
  turn=angle+math.sin(phase)*1.2
  sw,sh=780,445
  screen=Image.new('RGB',(sw,sh),(17,23,19)); sd=ImageDraw.Draw(screen)
  sd.rounded_rectangle((0,0,sw-1,sh-1),radius=19,fill=(12,17,14),outline=(181,163,117),width=3)
  content=shots[idx].resize((sw-22,sh-44),Image.Resampling.LANCZOS)
  screen.paste(content,(11,31))
  sd.rounded_rectangle((9,8,sw-9,25),radius=6,fill=(239,235,225))
  for k,c in enumerate([(187,93,79),(203,165,88),(111,144,107)]): sd.ellipse((18+k*15,14,25+k*15,21),fill=c)
  # right-side thickness gives the panels a visible dimensional edge
  base=Image.new('RGBA',(sw+15,sh+13),(0,0,0,0)); base.alpha_composite(screen.convert('RGBA'),(0,0)); bd=ImageDraw.Draw(base)
  bd.polygon([(sw,10),(sw+14,18),(sw+14,sh+5),(sw,sh)],fill=(110,102,78,255))
  bd.polygon([(0,sh),(sw,sh),(sw+14,sh+5),(16,sh+12)],fill=(201,190,162,255))
  panel=base.resize((int((sw+15)*scale),int((sh+13)*scale)),Image.Resampling.LANCZOS).rotate(turn,resample=Image.Resampling.BICUBIC,expand=True)
  # soft cast shadow, offset slightly downward
  shadow=Image.new('RGBA',panel.size,(0,0,0,0)); shadow.putalpha(panel.getchannel('A')); shadow=shadow.filter(ImageFilter.GaussianBlur(19)); shadow=ImageEnhance.Brightness(shadow).enhance(.40)
  px=int(x + math.cos(phase)*5); py=int(y+bob)
  sx=max(0,min(W-shadow.width,px+10)); sy=max(0,min(H-shadow.height,py+19))
  bg.alpha_composite(shadow,(sx,sy)); bg.alpha_composite(panel,(px,py))
 frames.append(bg.convert('RGB').quantize(colors=128,method=Image.Quantize.MEDIANCUT))
frames[0].save(out,save_all=True,append_images=frames[1:],duration=65,loop=0,optimize=True,disposal=2)
print(f'Created {out} ({out.stat().st_size:,} bytes; {len(frames)} frames)')
