import pygame as pg
import numpy as n
from typing import *
from dataclasses import dataclass

@dataclass 
class C:
    W,H,F=800,600,60
    S={'k':(0,0,0),'w':(255,)*3,'r':(255,0,0),'b':(0,0,255)}
    
class P:
    def __init__(s,x,y,v,c):
        s.x,s.y,s.v,s.c,s.a=x,y,v,c,255
    def u(s):
        s.x+=s.v[0];s.y+=s.v[1];s.v=(s.v[0]*.99,s.v[1]+.1)
        s.a=max(0,s.a-2);return s.a>0
        
class G:
    def __init__(s,d=pg.display.set_mode((C.W,C.H))):
        s.d,s.r,s.c=d,1,pg.time.Clock()
        s.t=n.zeros(C.W);s.p=[];s.g()
        
    def g(s):
        s.t[0]=s.t[-1]=C.H*.6
        for i in range(1,C.W-1):
            s.t[i]=min(C.H*.8,max(C.H*.3,s.t[i-1]+n.random.uniform(-2,2)))
            
    def u(s):
        s.p=[p for p in s.p if p.u()]
        for e in pg.event.get():
            if e.type==pg.QUIT or(e.type==pg.KEYDOWN and e.key==pg.K_ESCAPE):s.r=0
            elif e.type==pg.MOUSEBUTTONDOWN:
                x,y=pg.mouse.get_pos()
                for _ in range(20):
                    a=n.random.uniform(0,6.28)
                    v=(n.cos(a)*2,n.sin(a)*2)
                    s.p.append(P(x,y,v,C.S['r']))
                    
    def d(s):
        s.d.fill(C.S['k'])
        pg.draw.polygon(s.d,(50,50,50),[(0,C.H)]+[(i,s.t[i])for i in range(C.W)]+[(C.W,C.H)])
        for p in s.p:
            pg.draw.circle(s.d,(*p.c,p.a),(int(p.x),int(p.y)),2)
        pg.display.flip()
        
    def run(s):
        while s.r:s.u();s.d();s.c.tick(C.F)