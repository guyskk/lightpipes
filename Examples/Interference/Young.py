from LightPipes import *
import matplotlib.pyplot as plt

wavelength=5*um
size=20.0*mm
N=500

F=Begin(size,wavelength,N)
F1=CircAperture(0.15*mm,-0.6*mm, 0, F)
F2=CircAperture(0.15*mm, 0.6*mm, 0, F)    
F=BeamMix(F1,F2)
F=Fresnel(50*cm,F)
I=Intensity(2,F)
plt.imshow(I); plt.axis('off');plt.title('intensity pattern')
plt.show()

version()

#try:
	#import LightPipes
#except ImportError:
	#print ("LightPipes not present")
	#exit()

#import matplotlib.pyplot as plt
#m=1
#nm=1e-9*m
#um=1e-6*m
#mm=1e-3*m
#cm=1e-2*m

#LP=LightPipes.Init()

#wavelength=5*um
#size=20.0*mm
#N=500

#F=LP.Begin(size,wavelength,N)
#F1=LP.CircAperture(0.15*mm,-0.6*mm, 0, F)
#F2=LP.CircAperture(0.15*mm, 0.6*mm, 0, F)    
#F=LP.BeamMix(F1,F2)
#F=LP.Fresnel(50*cm,F)
#I=LP.Intensity(2,F)
#plt.imshow(I); plt.axis('off');plt.title('intensity pattern')
#plt.show()
