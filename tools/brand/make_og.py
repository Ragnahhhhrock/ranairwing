#!/usr/bin/env python3
"""Compose og.png (1200x630) from tools/brand/og-base.png: adds the Australian White Ensign, 'Royal Australian Navy'
and the ship's motto. Needs rsvg-convert and a bold monospace (JetBrains Mono Bold; set OG_FONT)."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
FONT=os.environ.get("OG_FONT","/home/claude/promo/fonts/JBMono-Bold.ttf")
subprocess.run(["rsvg-convert","-w","300","assets/ensign.svg","-o","/tmp/ensign300.png"],check=True)
im=Image.open("tools/brand/og-base.png").convert("RGBA"); d=ImageDraw.Draw(im)
fw,fh=150,75; x,y=66,52
flag=Image.open("/tmp/ensign300.png").convert("RGBA").resize((fw,fh),Image.LANCZOS)
d.rectangle([x-2,y-2,x+fw+1,y+fh+1],outline=(200,220,235,150),width=2)
im.alpha_composite(flag,(x,y))
def track(xy,t,f,fill,tr):
    px,py=xy
    for ch in t: d.text((px,py),ch,font=f,fill=fill); px+=f.getlength(ch)+tr
f1=ImageFont.truetype(FONT,22); f2=ImageFont.truetype(FONT,17)
track((x+fw+26,y+10),"ROYAL AUSTRALIAN NAVY",f1,(232,238,242,255),4)
track((x+fw+26,y+44),"AUSTRALIAN WHITE ENSIGN",f2,(159,180,194,255),3)
track((66,578),"VIRES ACQUIRIT EUNDO",f2,(232,197,71,255),5)
im.convert("RGB").save("og.png",optimize=True); print("wrote og.png")
