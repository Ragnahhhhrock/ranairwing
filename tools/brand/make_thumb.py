#!/usr/bin/env python3
"""YouTube thumbnail (1280x720) from tools/brand/og-base.png (the Open Graph sim render): the baked-in OG text is
inpainted away, then a new headline, the Australian White Ensign and the URL are added.
Needs rsvg-convert, opencv, Anton + JetBrains Mono Bold (set FONT_DIR)."""
import os, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont
FD=os.environ.get("FONT_DIR","/home/claude/promo/fonts")
base=cv2.imread("tools/brand/og-base.png")
B,G,R=[base[...,i].astype(int) for i in range(3)]
m=np.zeros(B.shape,np.uint8)
txt=((np.minimum(np.minimum(R,G),B)>150)|((R>170)&(G>140)&(B<130)))
for (y0,y1,x0,x1) in [(155,250,95,785),(262,310,95,585),(335,378,95,550),(404,472,95,410),(150,472,58,74)]:
    m[y0:y1,x0:x1]=txt[y0:y1,x0:x1].astype(np.uint8)*255
m=cv2.dilate(m,np.ones((13,13),np.uint8))
clean=cv2.inpaint(base,m,9,cv2.INPAINT_TELEA)
# smooth out inpaint ghosting right of the title: clone clean water from just below
src=clean[255:335,540:790].copy(); mk=np.full(src.shape[:2],255,np.uint8)
clean=cv2.seamlessClone(src,clean,mk,(665,205),cv2.NORMAL_CLONE)
im=Image.fromarray(cv2.cvtColor(clean,cv2.COLOR_BGR2RGB)).resize((1371,720),Image.LANCZOS).crop((91,0,1371,720)).convert("RGBA")
# darken the left for type
W,H=1280,720; gr=np.zeros((H,W,4),np.uint8); gr[...,:3]=(8,16,26)
a=np.clip(1-(np.arange(W)-420)/560,0,1)**1.2*0.88; gr[...,3]=(a[None,:]*255).astype(np.uint8)
im.alpha_composite(Image.fromarray(gr,"RGBA"))
d=ImageDraw.Draw(im)
def text(xy,t,f,fill,tr=0,stroke=0):
    x,y=xy
    for ch in t:
        d.text((x,y),ch,font=f,fill=fill,stroke_width=stroke,stroke_fill=(5,10,16)); x+=f.getlength(ch)+tr
A=os.path.join(FD,"Anton.ttf"); M=os.path.join(FD,"JBMono-Bold.ttf")
text((60,125),"FLY THE",ImageFont.truetype(A,170),(244,247,250),2,3)
text((60,285),"CARRIER",ImageFont.truetype(A,205),(232,197,71),2,3)
text((66,562),"HMAS MELBOURNE  ·  A-4G SKYHAWK",ImageFont.truetype(M,30),(232,238,242),3,2)
subprocess.run(["rsvg-convert","-w","420","assets/ensign.svg","-o","/tmp/ens.png"],check=True)
fw,fh=190,95; flag=Image.open("/tmp/ens.png").convert("RGBA").resize((fw,fh),Image.LANCZOS)
d.rectangle([58,48,58+fw+3,48+fh+3],outline=(200,220,235,200),width=3); im.alpha_composite(flag,(60,50))
text((278,64),"ROYAL AUSTRALIAN NAVY",ImageFont.truetype(M,24),(232,238,242),4,2)
text((278,102),"RANAIRWING.COM",ImageFont.truetype(M,24),(232,197,71),4,2)
im.convert("RGB").save("tools/brand/thumb-youtube.png",optimize=True); print("wrote thumb-youtube.png")
