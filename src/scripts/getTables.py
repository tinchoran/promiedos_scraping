import requests
from bs4 import BeautifulSoup
import json
import os

def get_match_data():
    fileRoute = os.getcwd() + "/src/data/tables_data.json"
    
    ligas = ["inglaterra", "espana", "italia", "alemania", "francia", "brasil", "mexico"]

    ligasData = []
    for liga in ligas:
        url = "https://www.promiedos.com.ar/" + liga
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        paisLiga = liga
        tituloLiga = soup.find("div", {'id': 'titulos'}).text.strip()
        tablaContainer = soup.find('div', {'id': 'tablapts'})
        tabla = tablaContainer.find("table", { "id": "posiciones"})
        tablaBody = tabla.find("tbody")
        teams = tablaBody.findAll("tr")
        
        teamsData = []
        for team in teams:
            attr = team.findAll("td")
            teamInfo = {
                "pos": attr[0].text,
                "name": attr[1].text,
                "img": "https://www.promiedos.com.ar/" + attr[1].find("img")["src"],
                "points": attr[2].text,
                "played": attr[3].text,
                "wins": attr[4].text,
                "draws": attr[5].text,
                "loses": attr[6].text,
                "golesAF": attr[7].text,
                "golesEC": attr[8].text,
                "difGoles": attr[9].text
            }
            teamsData.append(teamInfo)
        tableData = {
            "paisLiga": paisLiga,
            "ligaName": tituloLiga,
            "teamsData": teamsData
        }
        ligasData.append(tableData)
    with open(fileRoute, 'w') as json_file:
        json.dump(ligasData, json_file)
        

        # try:
        #     titulos = tablaContainer.find_all("div", {"class": "titulotabla2"}).text
        # except:
        #     pass


        # for fixture in fixtures:
        #     matches_in_fixture = []
        #     partidos = fixture.findAll("tr", { "name" : ["nvp", "vp"] })
        #     title = fixture.find("tr", {"class": "tituloin"}).text

            
        #     for partido in partidos:
        #         try:
        #             teams = partido.findAll("td", { "class": "game-t1"})
        #             team1 = teams[0].text
        #             img1  = url + "/" + teams[0].find("img")["src"]
        #             img2  = url + "/" + teams[1].find("img")["src"]
        #             team2 = teams[1].text
        #             res1  = partido.find("td", { "class": "game-r1"}).text
        #             res2  = partido.find("td", { "class": "game-r2"}).text
        #             try:
        #                 gameTime = partido.find("td", { "class": "game-time" }).text
        #             except:
        #                 gameTime = "Final"
        #             try:
        #                 gamePlay = partido.find("td", { "class": "game-play" }).text
        #             except:
        #                 gamePlay = ""
        #             match_info = {
        #                 "t1": team1,
        #                 "t2": team2,
        #                 "img1": img1,
        #                 "img2": img2,
        #                 "r1": res1 or "-",
        #                 "r2": res2 or "-",
        #                 "gametime": gameTime,
        #                 "gameplay": gamePlay
        #             }
                    
        #             matches_in_fixture.append(match_info)
        #         except Exception as e:
        #             continue
            
        #     fixture_data = {
        #         "liga": title,
        #         "partidos": matches_in_fixture,
        #     }
        #     dateInfo.append(fixture_data)
            
        # with open(fileRoute, 'w') as json_file:
        #     json.dump(dateInfo, json_file)

result = get_match_data()


