const express = require("express");
const app = express();

const { exec } = require("child_process");

//Common modules
const path = require("path")
const fs = require("fs");

// Scripts & files paths
const matchesScript = path.resolve(__dirname, "./src/scripts/getMatches.py")
const tablesScript = path.resolve(__dirname, "./src/scripts/getTables.py")
const matchesData = path.resolve(__dirname, "./src/data/fixtures_data.json")
const tablesData = path.resolve(__dirname, "./src/data/tables_data.json")

app.use(express.urlencoded())
app.use(express.json())

app.use(express.static("public"))

app.set("view engine", "ejs")
app.set("views", path.resolve(__dirname, "./src/views"))

//Recogida de datos
// setInterval(() => {
//     //Ejectuar script para traer las tablas y guaradarlas en tables_data.json
//     exec(matchesScript, (error, stdout, stderr) => {  
//         if (error) {
//         console.error(`Error al ejecutar el script: ${error.message}`);
//         return res.send("Hubo un error");
//         }
//         if (stderr) {
//             console.error(`Error en la salida estándar: ${stderr}`);
//             return res.send("Hubo un error");
//         }
//         console.log("Datos de Partidos actualizados correctamente")
//     });
//     //Ejectuar script para traer las tablas y guaradarlas en tables_data.json
//     exec(tablesScript, (error, stdout, stderr) => {  
//         if (error) {
//         console.error(`Error al ejecutar el script: ${error.message}`);
//         return res.send("Hubo un error");
//         }
//         if (stderr) {
//             console.error(`Error en la salida estándar: ${stderr}`);
//             return res.send("Hubo un error");
//         }
//         console.log("Datos de Tablas actualizados correctamente")
//     });
// }, 600000) //Tiempo que pasará entre cada petición a promiedos para buscar los datos


app.get("/", (req, res) => res.redirect("/inglaterra"))

app.get("/:ligue", (req, res) => {
    const matches = JSON.parse(fs.readFileSync(matchesData, "utf-8"));
    const tables = JSON.parse(fs.readFileSync(tablesData, "utf-8"));
    const tableNames = []
    tables.forEach(ligue => tableNames.push(ligue.paisLiga))
    const ligue = req.params.ligue;

    res.render("home", {
        view:{
            matches,
            table: tables.find(li => li.paisLiga.toLowerCase() == ligue.toLowerCase()),
            tableNames
        }
    })
})



const PORT = 3005;

app.listen(PORT, () => console.log(`Servidor corriendo en http://localhost:${PORT}`))