import requests
from bs4 import BeautifulSoup
import json

def get_match_data():
    url = "https://www.promiedos.com.ar"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    dateInfo = []

    fixtures = soup.find_all('div', {'id': 'fixturein'})
    for fixture in fixtures:
        matches_in_fixture = []
        partidos = fixture.findAll("tr", { "name" : "nvp" })
        title = fixture.find("tr", {"class": "tituloin"}).text

        for partido in partidos:
            try:
                teams = partido.findAll("td", { "class": "game-t1"})
                team1 = teams[0].text
                team2 = teams[1].text
                res1  = partido.find("td", { "class": "game-r1"}).text
                res2  = partido.find("td", { "class": "game-r2"}).text
                match_info = {
                    "t1": team1,
                    "t2": team2,
                    "r1": res1,
                    "r2": res2
                }
                
                matches_in_fixture.append(match_info)
            except Exception as e:
                continue
        
        fixture_data = {
            "liga": title,
            "partidos": matches_in_fixture
        }
        dateInfo.append(fixture_data)
        
    return json.dumps(dateInfo)


result = get_match_data()
print(result)

