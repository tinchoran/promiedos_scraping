[![Promiedos](https://www.promiedos.com.ar/images/menu/logo2.jpg)](https://www.promiedos.com.ar/)

# ⚽🚀Live Football results & tables

### Proyecto de WebScraping a  [Promiedos](https://www.promiedos.com.ar/) utilizando python para traer, parsear y almacenar los datos en archivos .json para luego manipularlos con Node.

## ⚙Lenguajes & tecnologías utilizadas
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)](https://expressjs.com/)
[![EJS](https://img.shields.io/badge/EJS-2D2D2D?style=for-the-badge&logo=ejs&logoColor=white)](https://ejs.co/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![Beautiful Soup](https://img.shields.io/badge/BS4-000000?style=for-the-badge)](https://www.crummy.com/software/BeautifulSoup/)

* ### Front end
    * Html  
    * CSS
        * Flex
        * Grid
    * Javascript

* ### Back End
    * NodeJS
        * Express
        * child_process
        * EJS view Engine
        * fs
    * Python
        * beautifulsoup4
        * requests
        * json
    * JSON

## 💡Funcionamiento
El proyecto cuenta con dos scripts hechos en python que se encargan de llevar a cabo el scraping:
* getMatches.py: Se encarga de hacer una request a la [página principal de PROMIEDOS](https://www.promiedos.com.ar/) para rescatar los datos del fixture del día.
* getTables.py: Cuenta con un arreglo de paises que recorre para rescatar las tablas de la liga de cada país.

Ambos archivos parsean los datos recibidos y guardan la información obtenida en los archivos ubicados en /src/data.

Este proceso es ejecutado por index.js mediante un exec() de la biblioteca "child_process", y está diseñado para repetirse mediante un timer, de preferiblemente un minuto. Esta parte del código está comentada, para no saturar los servidores de Promiedos. Para que funcione solo debe descomentarla.

Cuando un cliente hace una request al servidor, éste se encarga de obtener los datos de los archivos json mediante la función fs.readFileSync() del módulo "fs", rescatando el fixture y la liga que haya elegido el usuario. Posteriormente se hace un render dinámico con la información obtenida haciendo uso del motor de vistas "ejs".

Cabe aclarar que aunque se actualicen los json cada 60 segundos, la página no ofrece un servicio 100% "live", ya que no existe una conexión persistente entre el servidor y el cliente. Por eso, si hay algún gol de un partido en vivo, el cliente no se enterará a menos que recargue la página.

## 📋Requerimientos
Debe tener instalado el intérprete de [python](https://www.python.org/) y las bibliotecas **requests** y **beautifulsoup4**

Una vez instalado python, correr:
```
pip install beautifulsoup4
pip install requests
```
O, si usas un entorno virtual:
```
python -m pip install beautifulsoup4
python -m pip install requests
```

Posteriormente, ejecutar una terminal en la carpeta del proyecto y ejecutar:
```
npm install
```

Para levantar el servidor, correr en la terminal:
```
npm run start
```

Luego de esto se levantará el servidor en el puerto 3005, que puedes cambiar a tu antojo.

##  📂Estructura
```
├──index.js     # Entrypoint
├──package.json
├──package-lock.json
├──README.md
├──.gitignore
├──node_modules
├──public
    ├──styles
        ├──index.css
├──src
    ├──data
        ├──tables_data.json
        ├──matches_data.json
    ├──scripts
        ├──getMatches.py
        ├──getTables.py
    ├──views
        ├──home.ejs
```

## **Aclaración**
- Toda la información que recopila este proyecto pertenece a [promiedos]("https://www.promiedos.com.ar).
- Este proyecto no tiene la intención de infringir derechos de autor ni violar los términos de servicio del sitio web mencionado.
- La información obtenida se utiliza exclusivamente para fines personales y no será utilizada con fines comerciales.


## 🖼️View
![Captura de pantalla de la página ](/public/screenshot.png "This is a sample image.")
