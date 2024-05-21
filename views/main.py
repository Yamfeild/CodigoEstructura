import sys
sys.path.append('../')
from controls.RegistroDaoControl import RegistroDaoControl

rdc = RegistroDaoControl()

try:
    rdc._ServidorPublico._numVentanilla = 3
    rdc._ServidorPublico._nombre=  "David Alexander"
    rdc._ServidorPublico._fecha = "20/12/2020"
    rdc._ServidorPublico._calificacion = "Mala"
    rdc.save

except Exception as e:
    print("ptmdre no puedes")
    print(e)