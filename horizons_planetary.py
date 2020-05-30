#!/usr/bin/env python

import numpy as n
import scipy.constants as c
from astroquery.jplhorizons import Horizons
#import neo_snr
import matplotlib.pyplot as plt

def get_ephemeris(obj_id="2020 DA4",
                        obs_lat=69.3908,
                        obs_lon=20.2673,
                        obs_el=0.0,
                        start="2029-01-01",
                        stop="2030-01-01",
                        step="2h",
                        min_el=30.0,
                        id_type="majorbody",
                        debug=True):
    
    e3d = {'lon': obs_lon, 'lat': obs_lat, 'elevation': obs_el}
    obj = Horizons(id=obj_id,
                   location=e3d,
                   epochs={"start":start,
                           "stop":stop,
                           "step":step},
                   id_type=id_type)
#    print(obj)
    t0=obj.ephemerides(quantities="4,20,14",get_raw_response=True)
    
    t=obj.ephemerides(get_raw_response=True)
#    print(t)
    
    lines=t.split("\n")
    soe=False
    eoe=False
    dates=[]
    azs=[]
    els=[]
    sublon=[]
    sublat=[]
    r=[]
    rdot=[]
    for l in lines:
        if l.strip() == "$$EOE":
            eoe=True
        if soe and eoe == False:
            items=l.split(",")
            dates.append(items[0])
            azs.append(float(items[10]))
            els.append(float(items[11]))
            sublon.append(float(items[27]))
            sublat.append(float(items[28]))
            r.append(float(items[39])*c.au)
            rdot.append(float(items[40]))
            
#            print(l)
        if l.strip() == "$$SOE":
            soe=True
    r=n.array(r)
    rdot=n.array(rdot)
    azs=n.array(azs)
    els=n.array(els)
    sublon=n.array(sublon)
    sublat=n.array(sublat)
    # convert to +/- lon
    sublon[sublon>180.0]=(360-sublon[sublon>180.0])*-1.0
    return({"r":r,"rdot":rdot,"az":azs,"el":els,"sublon":sublon,"sublat":sublat})

def plot_lines(lon,lat,gidx):
    ranges=[]
    i0=gidx[0]
    i1=gidx[0]
    for i in range(len(gidx)-1):
        if gidx[i+1]-gidx[i] == 1:
            i1=gidx[i+1]
        else:
            ranges.append((i0,i1))
            i0=gidx[i+1]
        
    for r in ranges:
        print("%d-%d"%(r[0],r[1]))
        plt.plot(lon[r[0]:r[1]],lat[r[0]:r[1]],color="green")
    

def moon_observability():

    plt.figure(figsize=(10,10))
    
    plt.subplot(331)
    eph=get_ephemeris(obj_id="301",
                      start="2022-01-01",
                      stop="2023-01-01")
    
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    #plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")
    plt.title("2022")
    
    eph=get_ephemeris(obj_id="301",
                      start="2023-01-01",
                      stop="2024-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.subplot(332)
    plt.title("2023")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)    
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
#    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")
    

    plt.subplot(333)
    eph=get_ephemeris(obj_id="301",
                      start="2024-01-01",
                      stop="2025-01-01")
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.title("2024")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)    
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
#    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")
    

    plt.subplot(334)
    eph=get_ephemeris(obj_id="301",
                      start="2025-01-01",
                      stop="2026-01-01")
    gidx=n.where(eph["el"]>30.0)[0]
    
    plt.title("2025")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    #   plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(335)
    eph=get_ephemeris(obj_id="301",
                      start="2026-01-01",
                      stop="2027-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2026")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
 #   plt.xlabel("Sub-radar lunar longitude (deg)")
  #  plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(336)
    eph=get_ephemeris(obj_id="301",
                      start="2027-01-01",
                      stop="2028-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2027")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
   # plt.xlabel("Sub-radar lunar longitude (deg)")
   # plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(337)
    eph=get_ephemeris(obj_id="301",
                      start="2028-01-01",
                      stop="2029-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2028")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
    plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(338)
    eph=get_ephemeris(obj_id="301",
                      start="2029-01-01",
                      stop="2030-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2029")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
 #   plt.ylabel("Sub-radar lunar latitude (deg)")

    plt.subplot(339)
    eph=get_ephemeris(obj_id="301",
                      start="2030-01-01",
                      stop="2031-01-01")
    gidx=n.where(eph["el"]>30.0)[0]

    plt.title("2030")
    plt.plot(eph["sublon"],eph["sublat"],color="lightgray")
    plot_lines(eph["sublon"],eph["sublat"],gidx)
#    plt.plot(eph["sublon"][gidx],eph["sublat"][gidx],".",color="green")
    plt.xlabel("Sub-radar lunar longitude (deg)")
#    plt.ylabel("Sub-radar lunar latitude (deg)")

    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
#    eph=check_detectability(obj_id="301",debug=True)
    moon_observability()

    
    



