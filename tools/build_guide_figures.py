#!/usr/bin/env python3
"""Build SVG documentation diagrams; embedded source PNG remains unchanged."""
from pathlib import Path
from html import escape
import base64
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/assets/images'
DATA=base64.b64encode((OUT/'board-top-source.png').read_bytes()).decode()
INK='#14243b'; BLUE='#245bcc'; TEAL='#087f8c'; AMBER='#a55300'; MUTED='#516176'
class Figure:
 def __init__(self,title,subtitle,h=1000):
  self.h=h;self.items=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="{h}" viewBox="0 0 1400 {h}" role="img"><title>{escape(title)}</title><desc>{escape(subtitle)}</desc><rect width="1400" height="{h}" fill="#fff"/>']
  self.text(40,54,title,34,bold=True);self.text(40,90,subtitle,20,color=MUTED)
 def text(self,x,y,s,size=23,color=INK,bold=False,anchor='start'):
  self.items.append(f'<text x="{x}" y="{y}" font-family="Arial,Helvetica,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}" text-anchor="{anchor}">{escape(str(s))}</text>')
 def box(self,x,y,w,h,color='#edf3fc',stroke='none',radius=12):
  self.items.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{color}" stroke="{stroke}" stroke-width="3"/>')
 def line(self,x1,y1,x2,y2,color=BLUE,width=3):
  self.items.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"/>')
 def dot(self,x,y,label,color=BLUE,r=17):
  self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="white" stroke-width="3"/>');self.text(x,y+6,label,18,'white',True,'middle')
 def ring(self,x,y,r=15,color=BLUE):
  self.items.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{color}" stroke-width="4"/>')
 def board(self,x,y,w,h,crop=(0,0,934,1146)):
  a,b,c,d=crop
  self.items.append(f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="{a} {b} {c} {d}" preserveAspectRatio="xMidYMid meet"><image width="934" height="1146" href="data:image/png;base64,{DATA}"/></svg>')
 def card(self,x,y,num,title,lines,w=620,color=BLUE):
  self.box(x,y,w,86+max(0,len(lines)-1)*26);self.dot(x+28,y+29,num,color);self.text(x+57,y+36,title,25,bold=True)
  for i,s in enumerate(lines):self.text(x+57,y+65+i*26,s,20,color=MUTED)
 def footer(self,s='V2 socketed DIP • CAD rendering, not a photograph • Power off before changing wiring.'):
  self.text(40,self.h-24,s,18,color=MUTED)
 def save(self,name):
  (OUT/name).write_text(''.join(self.items)+'</svg>\n')
# Overview: one unchanged board render with numbered landmarks.
f=Figure('Meet your DMC Lite Shield','Top view • Camera at upper left; DB37 at the bottom.',1100)
f.board(25,125,650,798)
for x,y,n in [(101,86,1),(383,286,2),(845,268,3),(450,557,4),(450,1038,5),(289,72,6)]: f.dot(25+x*650/934,125+y*798/1146,n)
for y,n,t,ls in [(135,1,'Camera remote release',['J6 • Separate meter and shutter contacts.']), (250,2,'Four replaceable line drivers',['U1 / U2 / U5 / U6 • Two axes per IC.']), (365,3,'Controls and triggers',['J5 • Relay, LOG2, SWITCH and E-stop.']), (480,4,'Eight motor-signal ports',['CH1–4 in upper row; CH5–8 below.','RJ45 motion outputs — never Ethernet.']), (620,5,'DB37 motor-signal output',['Same eight axes, single-ended STEP/DIR.']), (735,6,'Status and activity lights',['Power, STEP activity and control inputs.'])]:f.card(725,y,n,t,ls)
f.box(40,950,1320,72);f.text(65,981,'The shield sends signals. External drivers and a separate supply power the motors.',24,bold=True);f.text(65,1009,'Click any illustration in the manual to open the full-size version.',20,color=MUTED)
f.footer();f.save('board-tour.svg')
# LEDs: physical locations checked against CAD component origins; badges offset from LED bodies.
f=Figure('Read the indicator lights','Numbered rings identify the LEDs; highlight colors are annotations, not simulated illumination.',1180)
f.board(20,135,700,859)
leds=[('P',289,72,'D11 · POWER','Indicator circuit has power.'),('E',706,60,'D1 · E-STOP INPUT','Terminal grounded; not proof of a stop.'),('S',564,90,'D28 · SWITCH','Input is low / contact asserted.'),('R',730,247,'D26 · RELAY DRIVE','Coil drive active; contacts not verified.'),('L',755,392,'D27 · LOG2','Buffer active, before output resistor.'),('1',92,688,'D3 · CH1 STEP',''),('2',284,689,'D18 · CH2 STEP',''),('3',484,688,'D19 · CH3 STEP',''),('4',692,684,'D20 · CH4 STEP',''),('5',192,960,'D21 · CH5 STEP',''),('6',422,960,'D22 · CH6 STEP',''),('7',624,959,'D23 · CH7 STEP',''),('8',847,957,'D24 · CH8 STEP','')]
for label,x,y,_,__ in leds:
 px=20+x*700/934;py=135+y*859/1146
 f.ring(px,py,12,TEAL if label.isdigit() else BLUE);f.line(px,py-12,px,py-27);f.dot(px,py-40,label,TEAL if label.isdigit() else BLUE,14)
for i,(n,x,y,t,d) in enumerate(leds[:5]): f.card(760,135+i*105,n,t,[d],590)
f.box(760,675,590,310);f.text(785,712,'1–8 · Blue STEP indicators',25,bold=True)
for i,(_,x,y,t,d) in enumerate(leds[5:]):f.text(785+(i%2)*285,754+(i//2)*40,t,22)
f.text(785,937,'Activity ≠ position or successful motion.',21,color=TEAL,bold=True);f.text(785,966,'Fast pulses may look continuously lit.',20,color=MUTED)
f.box(40,1020,1320,96,'#fff3df');f.text(65,1054,'Normally-closed E-stop: red may be ON in the normal state.',25,bold=True);f.text(65,1087,'The LED follows contact grounding. Confirm the firmware mode and actual stop behavior.',22)
f.footer();f.save('led-map.svg')
# Terminal crop + exact vertical pin numbering. J5 R90 means pin7 top, pin1 bottom.
f=Figure('J5: the seven control terminals','Same top-view orientation as the board tour. Count from the bottom: pin 1 is the lower GND.',820)
f.board(40,140,470,570,(640,125,260,315))
rows=[(7,'GND','Logic and switch common'),(6,'E-STOP','Contact to GND → D48 low'),(5,'SWITCH','Normally open button → GND'),(4,'RELAY−','Floating relay contact B'),(3,'RELAY+','Floating relay contact A'),(2,'LOGIC','LOG2 output + GND reference'),(1,'GND','Logic and switch common')]
for i,(n,t,d) in enumerate(rows):
 y=185+i*71;f.dot(548,y,n);f.line(408,y,528,y);f.text(585,y+7,t,26,bold=True);f.text(810,y+7,d,23)
f.box(565,688,790,65,'#fff3df');f.text(585,716,'RELAY+ / RELAY− do not supply voltage.',24,bold=True);f.text(585,742,'LOG1 drives this contact pair. LOG2 is a separate output.',20)
f.footer('J5 pin numbering verified against V2 CAD • No external voltage into SWITCH or E-stop.');f.save('control-terminal.svg')
# Driver sockets and pin1.
f=Figure('Replace the right driver','TI AM26C31INE4 / AM26C31IN • 16-pin PDIP, package N • Socketed V2 only.',870)
f.board(65,180,1260,500,(75,160,570,270))
for x,ref,chs in [(145,'U1','Channels 1 + 2'),(286,'U2','Channels 3 + 4'),(432,'U5','Channels 5 + 6'),(574,'U6','Channels 7 + 8')]:
 px=65+(1260-570*(500/270))/2+(x-75)*(500/270)
 f.text(px,137,ref,30,bold=True,anchor='middle');f.text(px,167,chs,22,anchor='middle')
 # nested view fits with vertical letterboxing: image width1140 at factor1.852, centered
# Actual scaling is min(1260/570,500/270); x offset centers the crop.
scale=500/270;left=65+(1260-570*scale)/2
for x,y in [(101,191),(243,190),(389,192),(532,191)]:
 f.dot(left+(x-75)*scale,180+(y-160)*scale,'1',AMBER)
f.box(40,708,1320,95);f.text(65,744,'Pin 1 is at the upper-left contact of each socket in this view.',25,bold=True);f.text(65,778,'Align IC pin 1 with the PCB mark. Disconnect all power; fix the original fault before replacing.',22)
f.footer('CAD socket/IC models are illustrative • Confirm PCB pin 1 on the physical board before insertion.');f.save('driver-map.svg')
# RJ45 functional pin graphic, deliberately no invented mating view.
f=Figure('RJ45: one axis per connector','Signal assignments apply to every CH1–CH8 port. This is a pin table, not a mating-face drawing.',810)
f.board(35,145,430,450,(60,455,195,210))
labels=[('1','STEP+','Positive step'),('2','STEP−','Complementary step'),('3','DIR+','Positive direction'),('4','+5 V','Accessory supply'),('5','GND','Common'),('6','DIR−','Complementary direction'),('7','+5 V','Accessory supply'),('8','GND','Common')]
for i,(n,t,d) in enumerate(labels):
 y=160+i*62;f.box(520,y-25,825,54,'#edf3fc' if i%2==0 else '#f5f7fa');f.dot(550,y,n);f.text(590,y+8,t,25,bold=True);f.text(815,y+8,d,23)
f.text(65,625,'Twisted pairs: 1 + 2 and 3 + 6.',22,bold=True);f.text(65,657,'STEP− / DIR− are NOT ground.',22,color=AMBER,bold=True)
f.box(40,697,1320,65,'#fff3df');f.text(65,736,'Never connect to Ethernet / PoE. Accessory +5 V is not motor power; load budget unqualified.',22,bold=True)
f.footer();f.save('rj45-pinout.svg')
# DB37 bank mapping with real connector crop.
f=Figure('DB37: the same eight axes','Single-ended positive STEP/DIR outputs • CAD view above; logical mapping below.',800)
f.board(80,125,1240,215,(75,970,785,145))
for i in range(8):
 x=45+i*165;f.box(x,385,150,170);f.text(x+75,424,f'CH{i+1}',27,bold=True,anchor='middle');f.text(x+75,470,f'STEP {i+2}',23,anchor='middle');f.text(x+75,510,f'DIR {i+21}',23,anchor='middle')
f.text(45,360,'Connector pin numbers — not physical pin positions',21,color=MUTED)
f.box(40,590,1320,115);f.text(65,627,'GND: 1, 18, 19       +5 V accessory: 20, 37',26,bold=True);f.text(65,668,'Unconnected: 10–17 and 29–36. No negative STEP/DIR signals on DB37.',24)
f.footer('Use embossed pin numbers or a connector drawing; mating and solder views are mirrored.');f.save('db37-pinout.svg')
# Three practical wiring diagrams, explicit terminal numbers.
f=Figure('Three ways to connect J5','Conceptual wiring • Locate numbered terminals using the J5 close-up • Power off before wiring.',1050)
for y,title,left,right in [(145,'A · Button requests a Dragonframe action','J5 SWITCH · pin 5','J5 GND · pin 1 or 7'),(425,'B · Relay closes a receiver’s contact input','J5 RELAY+ · pin 3','J5 RELAY− · pin 4'),(705,'C · LOG2 drives a logic-trigger input','J5 LOGIC · pin 2','J5 GND · pin 1 or 7')]:
 f.box(40,y,1320,245);f.text(65,y+38,title,27,bold=True);f.text(65,y+94,left,23);f.text(65,y+157,right,23)
 f.line(370,y+87,785,y+87);f.line(370,y+150,785,y+150)
 f.box(785,y+62,525,112,'white',TEAL)
 if y==145:
  f.text(810,y+98,'Normally open pushbutton',25,bold=True);f.text(810,y+140,'Press connects SWITCH to GND.',21);f.text(65,y+214,'Enable D49 in M7 firmware; assign Shoot in Scene → Triggers.',23)
 elif y==425:
  f.text(810,y+98,'Receiver dry-contact input',25,bold=True);f.text(810,y+140,'Connect across its two input terminals.',21);f.text(65,y+214,'LOG1 controls relay. Floating contacts; no voltage supplied. Low-voltage control use only.',22)
 else:
  f.text(810,y+98,'Compatible logic receiver',25,bold=True);f.text(810,y+140,'Top wire: signal. Bottom: common.',21);f.text(65,y+214,'Nominal 5 V stage, with 1 kΩ series resistor. Verify input thresholds and loading.',22)
f.footer('Wiring blocks show functions, not internal circuitry. Never connect a lamp or motor directly to LOG2.');f.save('trigger-wiring.svg')
# Stop state visual.
f=Figure('E-stop: match wiring and firmware','J5 pin 6 → stop contact → J5 GND (pin 1 or 7). The contact must not apply an external voltage.',730)
for x,title,states in [(40,'Normally open (NO)',[('Released','OPEN','No stop request'),('Pressed','CLOSED','Stop requested'),('Broken wire','OPEN','Not detected as a stop')]),(720,'Normally closed (NC)',[('Released','CLOSED','No stop request'),('Pressed','OPEN','Stop requested'),('Broken wire','OPEN','Stop requested')])]:
 f.box(x,140,640,405);f.text(x+25,185,title,29,bold=True)
 for i,(a,b,c) in enumerate(states):
  y=245+i*95;f.text(x+25,y,a,24,bold=True);f.text(x+270,y,b,24,color=TEAL,bold=True);f.text(x+25,y+34,c,23)
f.box(40,575,1320,85,'#fff3df');f.text(65,608,'Enable D48. NC operation also requires firmware that implements NC mode.',24,bold=True);f.text(65,641,'Red LED = grounded input. This input requests a firmware stop; it does not cut motor power.',22)
f.footer('Test released, pressed and disconnected states before motion. This is not a safety-rated stop circuit.');f.save('estop-states.svg')
# Firmware visual workflow, not a fake UI screenshot.
f=Figure('Flash BOTH Arduino cores','Use the matching dmc_m7 and dmc_m4 folders supplied with your Dragonframe installation.',790)
f.box(40,140,1320,120);f.text(65,181,'Find the sketches',28,bold=True);f.text(65,222,'Dragonframe installation → Resources → Arc Motion Control → dmc',27)
f.card(40,295,'1','Main core: M7',['Open dmc_m7/dmc_m7.ino','Target core: Main core','Flash split: 1.5MB M7 + 0.5MB M4','Click Upload; wait for success.'],640)
f.card(720,295,'2','Co-processor: M4',['Open dmc_m4/dmc_m4.ino','Target core: M4 Co-processor','Same flash split as M7','Click Upload; wait for success.'],640)
f.box(40,520,1320,150);f.text(65,561,'Then connect Dragonframe',28,bold=True);f.text(65,603,'Scene → Connections → Add Connection → dmc-lite',27);f.text(65,640,'Select an ArcMoco slot and the GIGA USB port. Connect and test one axis.',23)
f.footer('Instruction diagram, not an IDE screenshot • Verify compiles only; Upload writes the firmware.');f.save('flashing-workflow.svg')
# System signal/power view.
f=Figure('How the system connects','The shield controls external drivers. It does not drive motor windings.',680)
for x,w,t,sub in [(40,280,'Computer','Dragonframe'),(440,360,'GIGA + shield','dmc-lite firmware'),(930,420,'External motor driver','One per axis')]:
 f.box(x,175,w,150);f.text(x+w/2,230,t,27,bold=True,anchor='middle');f.text(x+w/2,276,sub,24,anchor='middle')
f.line(320,250,440,250);f.text(345,220,'USB',22)
f.line(800,250,930,250);f.text(811,210,'STEP / DIR',19)
f.box(930,435,420,120,'#e6f5f0');f.text(1140,478,'Motor',29,bold=True,anchor='middle');f.text(1140,518,'Driver supplies winding current',21,anchor='middle');f.line(1140,325,1140,435,TEAL);f.text(1160,386,'Motor cable',20)
f.box(40,435,760,120,'#fff3df');f.text(65,479,'Separate motor power supply',27,bold=True);f.text(65,520,'Connect to the external driver, per its manual.',23);f.line(800,495,865,495,AMBER);f.line(865,495,865,300,AMBER);f.line(865,300,930,300,AMBER)
f.footer('Conceptual system diagram • Check receiver input requirements before connecting RJ45 or DB37.');f.save('system-connections.svg')
# Camera: do not invent TRS assignment.
f=Figure('Camera: meter and shutter contacts','J6 is a remote-release interface, separate from camera USB/live view.',650)
f.board(30,145,570,330,(20,30,190,130))
f.card(680,145,'1','Camera common',['J6 PCB pad 1'],670)
f.card(680,245,'2','Shutter',['J6 PCB pad 2 → contact to common'],670)
f.card(680,345,'3','Meter / pre-shutter',['J6 PCB pad 3 → contact to common'],670)
f.box(40,510,1320,75,'#fff3df');f.text(65,542,'PCB pad numbers are NOT tip / ring / sleeve assignments.',25,bold=True);f.text(65,572,'Verify the jack and camera cable by continuity before wiring. No plug-pin diagram is asserted here.',21)
f.footer();f.save('camera-contacts.svg')
# Large-component focus plates: retain source pixels, wash out only the context.
# Coordinates are in the unchanged 934 x 1146 top-view screenshot.
focuses = [
 ('focus-rj45.svg', 'Eight RJ45 motor ports', 'CH1–4 above • CH5–8 below',
  [(70,464,174,206),(275,464,173,206),(481,464,174,206),(687,464,174,206),
   (73,737,174,206),(277,737,174,206),(484,737,174,206),(688,737,174,206)],
  'STEP / DIR signals to external drivers. Not Ethernet.'),
 ('focus-db37.svg', 'DB37 motor output', 'Same eight channels • Single-ended signals',
  [(79,973,774,142)], 'Alternative motor-signal connection; not extra axes.'),
 ('focus-drivers.svg', 'Four replaceable driver ICs', 'U1 · U2 · U5 · U6',
  [(88,174,112,230),(229,174,113,230),(375,174,113,230),(518,174,113,230)],
  'Two axes per IC • AM26C31IN / AM26C31INE4, PDIP-16.'),
 ('focus-terminal.svg', 'Seven screw terminals', 'J5 • Controls and triggers',
  [(803,127,83,279)], 'GND, E-stop, SWITCH, relay contacts and LOG2.'),
]
for name,title,sub,regions,note in focuses:
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="700" height="1040" viewBox="0 0 700 1040" role="img"><title>{escape(title)}</title><desc>{escape(sub)}. Original components remain visible while surrounding board is faded white.</desc><rect width="700" height="1040" fill="white"/>',
  f'<text x="30" y="48" font-family="Arial,Helvetica,sans-serif" font-size="29" font-weight="700" fill="{INK}">{escape(title)}</text>',
  f'<text x="30" y="82" font-family="Arial,Helvetica,sans-serif" font-size="21" fill="{MUTED}">{escape(sub)}</text>',
  '<svg x="25" y="115" width="650" height="798" viewBox="0 0 934 1146">',
  '<defs><mask id="context-wash"><rect width="934" height="1146" fill="white"/>']
 for x,y,w,h in regions:
  parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="black"/>')
 parts += ['</mask></defs>',f'<image width="934" height="1146" href="data:image/png;base64,{DATA}"/>',
  '<rect width="934" height="1146" fill="white" opacity="0.30" mask="url(#context-wash)"/>']
 for x,y,w,h in regions:
  parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="none" stroke="{BLUE}" stroke-width="2"/>')
 parts += ['</svg>',f'<text x="30" y="956" font-family="Arial,Helvetica,sans-serif" font-size="21" fill="{INK}">{escape(note)}</text>',
  f'<text x="30" y="1008" font-family="Arial,Helvetica,sans-serif" font-size="17" fill="{MUTED}">V2 top-view CAD • Fading indicates focus, not part color.</text></svg>']
 (OUT/name).write_text(''.join(parts)+'\n')
print('Built 15 SVG figures; original source image remains unchanged.')

# Mobile viewport crops keep the same source coordinates and annotations.
import re
mobile_regions = {
 'board-tour': [(0,120,700,810)],
 'led-map': [(180,130,410,115),(520,245,110,215),(50,480,320,390),(370,480,320,390)],
 'control-terminal': [(25,135,540,580)],
 'driver-map': [(65,180,630,500),(695,180,630,500)],
 'rj45-pinout': [(25,140,460,470)],
 'db37-pinout': [(75,120,1250,230)],
 'camera-contacts': [(20,135,595,345)],
}
for name, boxes in mobile_regions.items():
    original = (OUT / (name + '.svg')).read_text()
    for i, (x,y,w,h) in enumerate(boxes):
        cropped = re.sub(r'<svg\b[^>]*>', f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="{x} {y} {w} {h}" role="img">', original, count=1)
        (OUT / f'{name}-detail-{i+1}.svg').write_text(cropped)
