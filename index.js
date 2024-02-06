const express = require("express");

const app = express();

const { exec } = require("child_process");

const comandoPython = "getMatches.py"

app.get("/", (req, res) => {

    exec(comandoPython, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error al ejecutar el script: ${error.message}`);
            return res.send("Hubo un error");
        }
        if (stderr) {
            console.error(`Error en la salida estándar: ${stderr}`);
            return res.send("Hubo un error");
        }
    
        // Parsear la salida del script (suponiendo que es un JSON)
        const resultadoJson = JSON.parse(stdout);
    
        // Ahora puedes manipular el resultadoJson con JavaScript
        res.send(resultadoJson)
    });
    
})

const PORT = 3005;

app.listen(PORT, () => console.log(`Servidor corriendo en http://localhost:${PORT}`))