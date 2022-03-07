# scrapper.py
Para ejecutar se requiere indicar la ruta de chromedriver
``` 
python3 scrapper.py ./chromedriver
```
Esto ejecutará con los valores por defecto indicados en el reto

Para cambiar los argumentos utilizar 
``` 
python3 scrapper.py ./chromedriver --contenido 'Dataset' --categoria 'Finanzas' --formato 'csv' --reporte 'Donaciones'
```
No utilizar tildes o caracteres especiales

Se descarga por defecto en descargas

# filter_region.py

Para ejecutar requiere pasar el nombre del archivo por argumento
``` 
python3 filter_region.py pcm_donaciones.csv
```
el resultado se almacerá en una nueva carpeta 'regiones', si esta no existe se creará automaticamente.
