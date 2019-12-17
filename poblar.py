import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import camion, objeto, ruta
from django.core.exceptions import ObjectDoesNotExist

def poblar():
	c1 = addCamion('camion1')
	c2 = addCamion('camion2')
	c3 = addCamion('camion3')

	print ("Añadidos camiones")	

	o1 = addObjeto('objeto1')
	o2 = addObjeto('objeto2')
	o3 = addObjeto('objeto3')
	o4 = addObjeto('objeto4')

	print ("Añadidos objetos")	

	r1 = addRuta(c1, o1)
	r2 = addRuta(c2, o2)
	r3 = addRuta(c2, o3)
	r4 = addRuta(c2, o4)

	print ("Añadidas rutas")

def addCamion(nombreC):
	c = camion(nombreC=nombreC)
	c.save()	

	return c

def addObjeto(nombreO):
	o = objeto(nombreO=nombreO)
	o.save()	

	return o

def addRuta(camion_id, objeto_id):
	r = ruta(camion=camion_id, objeto=objeto_id)
	r.save()	

	return r

def inicializar():
	c=camion.objects.all()
	c.delete()

	o=objeto.objects.all()
	o.delete()

	r=ruta.objects.all()
	r.delete()

# Start execution here!
if __name__ == '__main__':
	print("Starting aplicacion population script...")
	inicializar()
	poblar()
