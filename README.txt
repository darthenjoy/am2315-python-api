Copyright 2013 Jörg Ehrsam <joerg@ehrsam.de> / <ehrsam.de>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

http://www.gnu.org/licenses/

Python Unterstützung für den Temperatur und Feuchtesensor AM2315
Jörg Ehrsam 2013

Änderungshistorie:

Version 1.0:
Erste Version


Installation:

#tar -xvzf AM.tar.gz
#cd AM2315
#python3 setup.py install 

Example: 
#python3
>>> import AM2315
>>> sensor=AM2315()
>>> sensor.temp()
24.5
>>> sensor.hum
65.3
