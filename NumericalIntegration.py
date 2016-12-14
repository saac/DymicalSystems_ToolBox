
from numpy import *


def Euler1D(f,x0,t0,tf,dt):
  T=[]
  X=[]
  
  T.append(t0)
  X.append(x0)

  t=t0
  x=x0
  
  while (t<tf):
    x = x + f(x)*dt
    t = t + dt
    X.append(x)
    T.append(t)
  
  return X


def Euler(f,x0,t0,tf,dt):
  T=[]
  X=[]
  
  for i in range(len(x0)):
    a=[]
    X.append(a)
    X[i].append(x0[i])
  
  T.append(t0)

  t=t0
  x=x0
  
  while (t<tf):
    x = x + f(x)*dt
    t = t + dt
    for i in range(len(x0)):
      X[i].append(x[i])
    T.append(t)
  
  return X,T
 
 
 
def RungeKutta1D(f,x0,t0,tf,dt):

  T=[]
  X=[]
      
  T.append(t0)
  X.append(x0)

  t=t0
  x=x0
  
  while (t<tf):
    
    k1=f(x)
    k2=f(x+(k1)*float(dt/2))
    k3=f(x+(k2*float(dt/2)))
    k4=f(x+k3*float(dt))
   
    x = x + ((k1/6) + (k2/3) + (k3/3) + (k4/6))*dt
    t = t + dt
    
    X.append(x)
    T.append(t)
  
  
  return X,T  
   
 
 
  
def RungeKutta(f,x0,t0,tf,dt):
  T=[]
  X=[]
  
  for i in range(len(x0)):
    a=[]
    X.append(a)
    X[i].append(x0[i])
  
  T.append(t0)

  t=t0
  x=x0
  dt=float(dt)
  
  while (t<tf):
    
    k1=f(x)
    k2=f(x+(k1)*float(dt/2))
    k3=f(x+(k2*float(dt/2)))
    k4=f(x+k3*float(dt))
   
    x = x + ((k1/6) + (k2/3) + (k3/3) + (k4/6))*dt
    t = t + dt
    
    for i in range(len(x0)):
      X[i].append(x[i])
    T.append(t)

  return X,T  
  
  