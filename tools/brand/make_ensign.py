#!/usr/bin/env python3
"""Generate assets/ensign.svg: the Australian White Ensign (RAN ensign, flown 1 March 1967 onward).
Construction follows the Australian national flag schedule (Flags Act 1953), colours inverted:
white field, Union Flag canton, blue Commonwealth Star in the lower hoist, blue Southern Cross in the fly.
Units: hoist = 600, fly = 1200. Star radii: Commonwealth 3/20 hoist, Southern Cross 1/14 hoist, Epsilon 1/24 hoist; inner radius 4/9 outer."""
import math
H=600; BLUE="#012169"; RED="#e4002b"
def star(cx,cy,R,n):
    r=R*4/9; pts=[]
    for i in range(2*n):
        a=-math.pi/2+i*math.pi/n; rad=R if i%2==0 else r
        pts.append(f"{cx+rad*math.cos(a):.2f},{cy+rad*math.sin(a):.2f}")
    return f'<polygon points="{" ".join(pts)}" fill="{BLUE}"/>'
fx,fy=1.5*H,.5*H           # centre of the square fly
stars=[star(.5*H,.75*H,.15*H,7),                        # Commonwealth Star, centred in lower hoist
       star(fx,5/6*H,H/14,7),                           # Alpha: below centre, 1/6 up from bottom edge
       star(fx+(-1/4)*H,fy-H/16,H/14,7),                # Beta: 1/4 left, 1/16 up
       star(fx,H/6,H/14,7),                             # Gamma: above centre, 1/6 down from top edge
       star(fx+2/9*H,fy-31/240*H,H/14,7),               # Delta: 2/9 right, 31/240 up
       star(fx+H/10,fy+H/24,H/24,5)]                    # Epsilon: 1/10 right, 1/24 down
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {2*H} {H}" width="{2*H}" height="{H}" role="img" aria-labelledby="t">
<title id="t">Australian White Ensign, the ensign of the Royal Australian Navy</title>
<rect width="{2*H}" height="{H}" fill="#ffffff"/>
<g transform="scale(10)">
<clipPath id="s"><path d="M0,0 v30 h60 v-30 z"/></clipPath>
<clipPath id="t2"><path d="M30,15 h30 v15 z v15 h-30 z h-30 v-15 z v-15 h30 z"/></clipPath>
<g clip-path="url(#s)"><path d="M0,0 v30 h60 v-30 z" fill="{BLUE}"/>
<path d="M0,0 L60,30 M60,0 L0,30" stroke="#fff" stroke-width="6"/>
<path d="M0,0 L60,30 M60,0 L0,30" clip-path="url(#t2)" stroke="{RED}" stroke-width="4"/>
<path d="M30,0 v30 M0,15 h60" stroke="#fff" stroke-width="10"/>
<path d="M30,0 v30 M0,15 h60" stroke="{RED}" stroke-width="6"/></g></g>
{chr(10).join(stars)}
</svg>
'''
open("assets/ensign.svg","w").write(svg); print("wrote assets/ensign.svg")
