HBar=1.0545716818*10**(-34)
Pi=3.1415926535
UnitMass=1.6605388628*10**(-27)
UnitElectro=1.6021765314*10**(-19)
SpeedLight=299792458
MassElectro=9.109535*10**(-31)
MassProton=1.672651*10**(-27)
MassNetron=1.674951*10**(-27)
KBBolziman=1.380664*10**(-23)
NaAlfgadeLuo=6.022053*10**(23)
EpsionInVacuum=8.854187817*10**(-12)
ConsMeV=10**6*UnitElectro
ConsAngstorm=10**(-10)
ConsFermi=10**(-15)

ConsHmc=HBar/UnitMass/SpeedLight*10**15
print('ConsHmc(fm)\n'+str(ConsHmc)+'\n')

ConsAlpha=UnitElectro**2/(4.0*Pi*EpsionInVacuum*HBar*SpeedLight)
print('ConsAlpha(精细结构常数):\n'+str(ConsAlpha)+'\n')

ConsEE=UnitElectro*UnitElectro/(4.0*Pi*EpsionInVacuum)/ConsMeV*10**(15)
print('ConsEE(MeV·fm):\n'+str(ConsEE)+'\n')

ConsWaveLengthElectro=HBar*SpeedLight/(MassElectro*SpeedLight**2)*10**(12)
print('ConsWaveLengthElectro(pm):\n'+str(ConsWaveLengthElectro)+'\n')

ConsHHumev=(HBar**2/UnitMass/ConsMeV)**(0.5)*10**(15)
print('ConsHHumev(fm):\n'+str(ConsHHumev)+'\n')

temp=HBar*SpeedLight/(10**(-7))/UnitElectro
print('可见光能量(eV)\n'+str(temp))
