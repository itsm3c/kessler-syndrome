from tkinter import *
from random import *
from math import *
from time import *
root=Tk()

tkoef = 1
nmax=400 #number of objects in space
sto=[0 for sto in range(0,nmax)]
h=[0 for h in range(0,nmax)]
r=6400000#radius of the Earth in meters
g=(6.67408*(10**-11))#gravity constant
mzem=(5.9742*(10**24))#mass of the Earth
k=int(50000) #scale
beta=[0 for beta in range(0,nmax)]
t=int(0)
fi=[randint(0,314)/100 for fi in range(0,nmax)]
clr=['#'+str(hex(randint(16,255)))[2:4]+str(hex(randint(16,255)))[2:4]+str(hex(randint(16,255)))[2:4] for clr in range(0,nmax)]
maxX = 1200
maxY = 600
xz=maxX//2 #centre X of the Earth
yz=maxY//2 #centre Y of the Earth
canv=Canvas(root,width=maxX,height=maxY,bg="white")
seed()
Rst=[randint(66,120)*100000 for Rst in range(0,nmax)]
ksi=[randint(0,628)/100 for ksi in range(0,nmax)]
#x0=[((-1)**randint(0,5))*randint(65,150)*100000 for x0 in range(0,nmax)] #start height of satellite
#y0=[((-1)**randint(0,5))*randint(65,150)*100000 for y0 in range(0,nmax)] #start height of satellite
x0=[0 for x0 in range(0,nmax)]
y0=[0 for y0 in range(0,nmax)]

for ii in range(0,nmax,1):
    x0[ii] = Rst[ii]*cos(ksi[ii])
    y0[ii] = Rst[ii]*sin(ksi[ii])

x1=[0 for x1 in range(0,nmax)]
y1=[0 for y1 in range(0,nmax)]
sz = 10 #size of trash
for i in range(0,nmax-1,1):
    x1[i]=x0[i]
    y1[i]=y0[i]

print('x1=',x1)
print('y1=',y1)
a=[0 for a in range(0,nmax)]
ax=[0 for ax in range(0,nmax)]
ay=[0 for ay in range(0,nmax)]
vx=[0 for vx in range(0,nmax)]
vy=[0 for vy in range(0,nmax)]
px=[0 for px in range(0,nmax)]
py=[0 for py in range(0,nmax)]
v0=[randint(3000,9000) for v0 in range(0,nmax)]#start velocity meter per second
canv.create_oval(xz-r//k, yz-r//k, xz+r//k, yz+r//k, outline="green")
m=[randint(100,1000) for m in range(0,nmax)]
gama=[0 for gama in range(0,nmax)]
schet=0
for i in range(0,nmax,1):
    h[i]=((y1[i])**2 + (x1[i])**2)**0.5 - r
print('h=',h)
print('clr=',clr)

while t<100*tkoef:
    print('t=',t)
    for i in range(0,nmax-1,1):
        if h[i]<0:
            h[i] = h[i]*1
            #print(h[i])
            continue
        if (x1[i]!= 0):
            beta[i]=(atan((y1[i])/(x1[i])))
        elif (x1[i]==0 and y1[i]>0):
            beta[i]=pi/2
        elif(x1[i]==0 and y1[i]<0):
            beta[i]=3*pi/2
        if(x1[i]>0):
            beta[i]=beta[i]+pi
        #canv.create_line(xz, yz, xz + x1//k, yz + y1//k)
        a[i]=g*(mzem/((r+h[i])**2)) #metr per second**2
        #print('a=',a[0])
        ax[i]=(a[i]*cos(beta[i])) #metr per second**2
        ay[i]=(a[i]*sin(beta[i])) #metr per second**2
        vx[i]=(v0[i]*cos(fi[i])+ax[i]*t) #metr per second
        vy[i]=(v0[i]*sin(fi[i])+ay[i]*t) #metr per second
        if (vx[i]!= 0):
            fi[i]=(atan(vy[i]/vx[i])) #radian
        elif (vx[i]==0 and vy[i]>0):
            fi[i]=pi/2
        elif (vx[i]==0 and vy[i]<0):
            fi[i]=3*pi/2
        if(vx[i]<0):
            fi[i]=fi[i]+pi
        x1[i]=(x0[i]+vx[i]*t) #metr
        y1[i]=(y0[i]+vy[i]*t) #metr
        #print('t=',t,'x1=',x1,'y1=',y1,'v0=',v0,'vx=',vx,'vy=',vy,'ax=',ax,'ay=',ay,'h=',h, 'beta=',beta)
        if (h[i] > 0):
            canv.create_oval(x1[i]//k + xz,y1[i]//k + yz,x1[i]//k +4 +xz ,y1[i]//k +4 +yz, outline=clr[i])
            #print('h=', h[i])
        else:
            #paint wrong objects
            #canv.create_oval(x1[i] // k + xz, y1[i] // k + yz, x1[i] // k + 4 + xz, y1[i] // k + 4 + yz, outline="red")
            print('wrong h=', h[i])
        x0[i]=x1[i] #metr
        y0[i]=y1[i] #metr
        h[i]=((y1[i])**2 + (x1[i])**2)**0.5 - r
        canv.pack()
        root.update()


        for i in range(0,nmax,1):
            for j in range (0,nmax-1,1):
                if i!=j:
                    if (abs(x1[i]-x1[j])<sz) and (abs(y1[i]-y1[j])<sz) and (sto[i]==0) and (sto[j]==0) and (t>2):
                        beta[i]=2*pi/3
                        beta[j]=7*pi/6
                        #fi[i]=randint(0,314)/100
                        #fi[j]=randint(0,314)/100
                        gama[i]=randint(0,314)/100
                        gama[j]=randint(0,314)/100
                        u1ch=m[i]*vx[i]*sin(gama[j])+m[j]*vx[j]*sin(gama[j])-m[i]*vy[i]*cos(gama[j])-m[j]*vy[j]*cos(gama[j])
                        u1zn=m[i]*cos(gama[j])*sin(gama[j])-cos(gama[j])*m[i]*sin(gama[i])
                        u2ch=m[i]*vx[i]*sin(gama[i])+m[j]*vx[j]*sin(gama[i])-m[i]*vy[i]*cos(gama[i])-m[j]*vy[j]*cos(gama[j])
                        u2zn=m[i]*cos(gama[j])*sin(gama[i])-cos(gama[i])*m[i]*sin(gama[j])

                        if u1zn != 0:
                            u1=u1ch/u1zn
                        else:
                            u1=v0[j]

                        if u2zn != 0:
                            u2=u2ch/u2zn
                        else:
                            u2=v0[i]
                        v0[i]=u1
                        v0[j]=u2
                        beta[i]=gama[i]
                        beta[j]=gama[j]
                        schet=5
                        sto[i]=3
                        sto[j]=3
                        print('STOLKNOVENIE: i=',i,'j=',j)
                        print('t=',t,'x1[i]=',x1[i],'x1[j]=',x1[j],'y1[i]=',y1[i],'y1[j]=',y1[j])
                    else:
                        schet=0
                        #print('i=', i)
                        #print('j=', j)
                        if sto[i]>0:
                            sto[i]=sto[i]-1
                        if sto[j]>0:
                            #print('j=',j)
                            sto[j]=sto[j]-1
                        #print('No crash =) i=',i,'j=',j)
                #else:
                    #continue
        #sleep(0.01)
        #canv.pack()
        #root.update()
    t=t+tkoef
canv.pack()
root.mainloop()
