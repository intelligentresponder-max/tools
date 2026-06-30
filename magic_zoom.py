#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
magic_zoom.py - Magischer Glow + Ken-Burns Zoom-Video (9:16)
ASGlobal / Sneakers4Seeker Tool

Macht aus einem Foto ein Reels-Video: gewaehlte Farbe leuchtet (Volt-Glow),
Kamera zoomt sanft auf einen Fokuspunkt rein und wieder raus.

NUTZUNG (interaktiv):
    python magic_zoom.py bild.jpg

OHNE FRAGEN:
    python magic_zoom.py bild.jpg --farbe weiss --glow volt --fokus auto --modus inout

Braucht: pillow, numpy  (pip install pillow numpy)
         ffmpeg          (pkg install ffmpeg)
"""
import sys, os, subprocess
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance, ImageChops, ImageDraw

GLOW = {"volt":(204,255,0),"gold":(255,200,40),"cyan":(0,220,255),
        "pink":(255,60,180),"weiss":(255,255,255),"rot":(255,50,40),"gruen":(60,255,120)}

TARGET = {
    "weiss":  dict(bmin=0.80,smax=0.14,hlo=None,hhi=None,label="Weiss (Sox/Sneaker/Swoosh-Umfeld)"),
    "schwarz":dict(bmin=0.00,smax=1.00,hlo=None,hhi=None,label="Schwarz/Dunkel",dark=True),
    "rot":    dict(bmin=0.30,smax=1.00,hlo=345,hhi=15,label="Rot"),
    "blau":   dict(bmin=0.25,smax=1.00,hlo=200,hhi=255,label="Blau"),
    "gruen":  dict(bmin=0.25,smax=1.00,hlo=80,hhi=160,label="Gruen"),
    "gelb":   dict(bmin=0.45,smax=1.00,hlo=40,hhi=70,label="Gelb"),
}

FOKUS = {"auto":"Auto (hellste Glow-Stelle)","mitte":"Mitte","oben":"Oben",
         "unten":"Unten","links":"Links","rechts":"Rechts"}
MODUS = {"inout":"Rein + Raus","in":"Nur rein","out":"Nur raus","parallax":"2.5D-Schwenk (Fake-Drehung)"}

def hsv_arrays(im):
    arr=np.asarray(im.convert("RGB")).astype(np.float32)/255.0
    r,g,b=arr[...,0],arr[...,1],arr[...,2]
    mx=np.max(arr,axis=2); mn=np.min(arr,axis=2); diff=mx-mn
    bright=mx; sat=np.where(mx>0,diff/(mx+1e-6),0); hue=np.zeros_like(mx)
    m=diff>1e-6
    idx=(mx==r)&m; hue[idx]=(60*((g[idx]-b[idx])/diff[idx])+360)%360
    idx=(mx==g)&m; hue[idx]=(60*((b[idx]-r[idx])/diff[idx])+120)%360
    idx=(mx==b)&m; hue[idx]=(60*((r[idx]-g[idx])/diff[idx])+240)%360
    return bright,sat,hue

def build_mask(im,t):
    bright,sat,hue=hsv_arrays(im)
    if t.get("dark"): m=(bright<0.25)
    else:
        m=(bright>=t["bmin"])&(sat<=t["smax"])
        if t["hlo"] is not None:
            if t["hlo"]<=t["hhi"]: m&=(hue>=t["hlo"])&(hue<=t["hhi"])
            else: m&=(hue>=t["hlo"])|(hue<=t["hhi"])
    return m

def magic_image(src,target_key,glow_key,out):
    im=Image.open(src).convert("RGB"); W,H=im.size
    t=TARGET[target_key]; glow_rgb=GLOW[glow_key]
    mask=build_mask(im,t)
    wm=Image.fromarray((mask.astype(np.float32)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(3))
    bg=ImageEnhance.Color(im).enhance(0.7); bg=ImageEnhance.Brightness(bg).enhance(0.62); bg=ImageEnhance.Contrast(bg).enhance(1.12)
    fg=Image.composite(im,Image.new("RGB",(W,H),(0,0,0)),wm); fg=ImageEnhance.Brightness(fg).enhance(1.45)
    base=Image.composite(fg,bg,wm.filter(ImageFilter.GaussianBlur(2)))
    bloom=fg.filter(ImageFilter.GaussianBlur(16)); base=ImageChops.screen(base,ImageEnhance.Brightness(bloom).enhance(0.8))
    gm=wm.filter(ImageFilter.GaussianBlur(22)); gl=Image.new("RGB",(W,H),glow_rgb)
    gl=ImageChops.multiply(gl,Image.merge("RGB",[gm]*3)); gl=ImageEnhance.Brightness(gl).enhance(0.6)
    base=ImageChops.screen(base,gl)
    vig=Image.new("L",(W,H),0); d=ImageDraw.Draw(vig); d.ellipse([-W*0.25,-H*0.25,W*1.25,H*1.25],fill=255)
    vig=vig.filter(ImageFilter.GaussianBlur(min(W,H)//3)); dark=ImageEnhance.Brightness(base).enhance(0.5)
    base=Image.composite(base,dark,vig)
    base.save(out,quality=92)
    return mask  # return raw mask for focus detection

def focus_point(mask, fokus, W, H):
    """Gibt (fx, fy) in 0..1 zurueck (relativ)."""
    if fokus=="mitte": return 0.5,0.5
    if fokus=="oben":  return 0.5,0.3
    if fokus=="unten": return 0.5,0.7
    if fokus=="links": return 0.3,0.5
    if fokus=="rechts":return 0.7,0.5
    # auto: Schwerpunkt der Maske (wo am meisten leuchtet)
    ys,xs=np.where(mask)
    if len(xs)<50: return 0.5,0.5
    fx=float(np.median(xs))/W; fy=float(np.median(ys))/H
    # leicht zur Mitte ziehen, damit Zoom nicht aus dem Bild faellt
    fx=0.5+(fx-0.5)*0.6; fy=0.5+(fy-0.5)*0.6
    return fx,fy

def build_916_frame(src, out):
    """Bild auf 1080x1920 mit blurred fill bringen."""
    im=Image.open(src).convert("RGB"); TW,TH=1080,1920
    bg=im.copy(); s=TW/bg.width; bg=bg.resize((TW,int(bg.height*s)))
    if bg.height<TH: s=TH/bg.height; bg=bg.resize((int(bg.width*s),TH))
    bx=(bg.width-TW)//2; by=(bg.height-TH)//2
    bg=bg.crop((bx,by,bx+TW,by+TH)).filter(ImageFilter.GaussianBlur(40))
    bg=ImageEnhance.Brightness(bg).enhance(0.45)
    fr=min(TW/im.width,TH/im.height); fw,fh=int(im.width*fr),int(im.height*fr)
    fg=im.resize((fw,fh)); canvas=bg.copy(); canvas.paste(fg,((TW-fw)//2,(TH-fh)//2))
    canvas.save(out,quality=94)

def make_video(frame_jpg, fx, fy, modus, out, secs=4):
    TW,TH=1080,1920; fps=30; d=int(secs*fps)
    cx=f"iw*{fx:.3f}"; cy=f"ih*{fy:.3f}"
    if modus=="parallax":
        # 2.5D-Schwenk: leichter Zoom + sinus-Schwenk in x/y = Fake-Drehung
        secs=5; d=int(secs*fps)
        x=f"iw/2-(iw/zoom/2)+sin(on/40)*260"
        y=f"ih/2-(ih/zoom/2)+cos(on/55)*120"
        z="1.25"
        vf=(f"scale=2700:4800,zoompan=z='{z}':x='{x}':y='{y}':d={d}:s={TW}x{TH}:fps={fps},format=yuv420p")
    else:
        x=f"{cx}-(iw/zoom/2)"; y=f"{cy}-(ih/zoom/2)"
        if modus=="in":
            z=f"min(zoom+0.0010,1.35)"
        elif modus=="out":
            z=f"if(eq(on,0),1.35,max(zoom-0.0010,1.0))"
        else:  # inout
            half=d//2
            z=f"if(lt(on,{half}),min(zoom+0.0016,1.35),max(zoom-0.0016,1.0))"
        vf=(f"scale=2160:3840,zoompan=z='{z}':x='{x}':y='{y}':d={d}:s={TW}x{TH}:fps={fps},format=yuv420p")
    cmd=["ffmpeg","-y","-loop","1","-i",frame_jpg,"-t",str(secs),"-r",str(fps),
         "-vf",vf,"-c:v","libx264","-preset","medium","-crf","23",out]
    r=subprocess.run(cmd,capture_output=True,text=True)
    return r.returncode==0, r.stderr[-400:] if r.returncode else ""

def ask(prompt,options,default_key):
    print("\n"+prompt); keys=list(options.keys())
    for i,k in enumerate(keys,1):
        lbl=options[k]["label"] if isinstance(options[k],dict) else options[k]
        star=" (Standard)" if k==default_key else ""
        print(f"  {i}) {k} - {lbl}{star}")
    raw=input(f"Zahl oder Name [Enter = {default_key}]: ").strip().lower()
    if raw=="": return default_key
    if raw.isdigit() and 1<=int(raw)<=len(keys): return keys[int(raw)-1]
    if raw in options: return raw
    print("  -> nicht erkannt, Standard."); return default_key

def main():
    args=sys.argv[1:]
    if not args:
        print("Nutzung: python magic_zoom.py <bild.jpg> [weitere ...]")
        print("Optional: --farbe weiss --glow volt --fokus auto --modus inout")
        return
    farbe=glow=fokus=modus=None; files=[]; i=0
    while i<len(args):
        a=args[i]
        if a=="--farbe": farbe=args[i+1].lower(); i+=2
        elif a=="--glow": glow=args[i+1].lower(); i+=2
        elif a=="--fokus": fokus=args[i+1].lower(); i+=2
        elif a=="--modus": modus=args[i+1].lower(); i+=2
        elif a in("--input",): files.append(args[i+1]); i+=2
        else: files.append(a); i+=1
    files=[f for f in files if os.path.isfile(f)]
    if not files: print("Keine gueltigen Bilder."); return

    if farbe is None: farbe=ask("Welche FARBE soll leuchten?",TARGET,"weiss")
    if glow  is None: glow =ask("Welche GLOW-Farbe?",{k:GLOW[k] and k for k in GLOW} if False else {k:k for k in GLOW},"volt")
    if fokus is None: fokus=ask("Wohin ZOOMEN (Fokus)?",FOKUS,"auto")
    if modus is None: modus=ask("Zoom-MODUS?",MODUS,"inout")

    print(f"\n-> Farbe:{farbe} Glow:{glow} Fokus:{fokus} Modus:{modus}\n")
    for f in files:
        b=os.path.splitext(os.path.basename(f))[0]
        mimg=f"magic-{b}.jpg"; frame=f"_frame-{b}.jpg"; vid=f"zoom-{b}.mp4"
        mask=magic_image(f,farbe,glow,mimg)
        W,H=Image.open(f).size; fx,fy=focus_point(mask,fokus,W,H)
        build_916_frame(mimg,frame)
        ok,err=make_video(frame,fx,fy,modus,vid)
        os.remove(frame)
        if ok: print(f"   OK: {vid}  (+ Bild {mimg})  Fokus@{fx:.2f},{fy:.2f}")
        else:  print(f"   FEHLER bei {f}: {err}")
    print("\nFertig. 🪄🎥")

if __name__=="__main__":
    main()
