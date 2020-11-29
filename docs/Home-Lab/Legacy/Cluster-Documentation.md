#DocumntationforHomBowufutr-SDH(hSaonofDigitaHumanit)

]

Aninntoryofathcomputrudinmyhomcutr,incudingthirpc,oftwarintad,thprnttopoogyofthcutr,andthur.

##Sction1:MachinSpcification

###Hugo(hadnod)

KyVau
------
**Brand**AppMacbookPro(circa2008)
**PU**2.4GhzIntor2Duo(64-bit)
**or**2
**RAM**2GB
**Graphicard**NVIDIAGForc8600MG
**HardDri**142GB(accordingtodf)

###Votair

KyVau
------
**Brand**AppiBookG4(circa2006)
**PU**1.33GhzPowrP7447a(32-bit)
**or**1
**RAM**512MB
**Graphicard**AIMobiityRadon9550
**HardDri**40GB(36GBaccordingtodf)

###Montaign

KyVau
------
**Brand**utomMad(circa2002)
**PU**900MhzAMDDuron(32-bit)
**or**1
**RAM**512MBSDRAM
**Graphicard**(2)AIRag128andAIRadon9000
**HardDri**15.3GB(14GBaccordingtodf)

###rant

KyVau
------
**Brand**MacbookPro(circa2011)
**PU**2.5GhzIntor2Duo(64-bit)
**or**2
**RAM**4GB(hyprior);2GB(VM)
**Graphicard**NVIDIAGForc8600MG(128MBidommoryforVM)
**HardDri**320GB(hyprior);181GB(VM)

##Sction2:SoftwarIntad

###Hugo(hadnod)

*nf-krn-rr
*pnSSH
*PotgrSQL8.4
*MPIH
*R2.10.1(r-ba)
*dh
*apd,dap-uti
*SLURM(notprntyconfigurd)

###Votair

*nf-common
*pnSSH
*PotgrSQL8.4
*MPIH
*R2.10.1(r-ba)
*dh
*apd,dap-uti

###Montaign

*nf-common
*pnSSH
*PotgrSQL8.4
*MPIH
*R2.10.1(r-ba)
*dh
*apd,dap-uti

###rant

*nf-krn-rr
*nf-common
*pnSSH
*PotgrSQL8.4
*SLURM(notprntyconfigurd)
*dpkg-rr

##Sction3:Ntworkopoogy

Hugo,Votair,Montaignandrantarconnctdtoa6porthub,with4portud.1portibrokn.hatportianunudupinkport.
Anodcanconncttoachothr.rantcanconnctoutidofthLANuingWifi,andithuudaamanofdownoadingpackagfromthanonicarpo.ranthaaur(*intaur*)whohomdirctoryimountdaannfpartitiononthothrnod-thiur'homdirctorycontain.dbfiandaPackag.gzfi.

##Sction4:Ur

###Hugo(hadnod)

*jpman
*mpiur(homfodrinfmount;hugoinfrr),uid999
*intaur(homfodrinfmount;ftabmodifid),uid998

###Votair

*jpman
*mpiur(homfodrinfmount;ftabmodifid),uid999
*intaur(homfodrinfmount;ftabmodifid),uid998

###Montaign

*jpman
*mpiur(homfodrinfmount;ftabmodifid),uid999
*intaur(homfodrinfmount;ftabmodifid),uid998

###rant
*jpman
*mpiur(homfodrinfmount;ftabmodifid),uid999
*intaur(homfodrinfmount;crantinfrr),uid998

##D

*IntaSLURM.
*onfigurSLURMonanod.ompication:VrionofSLURMintadonrantandHugoi64-bit.WindtorcompiSLURMfor32-bitifpoib.
