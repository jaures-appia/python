from requests import get
from bs4 import BeautifulSoup

def scrapFoot():

    url = 'https://www.matchendirect.fr/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs = {'id':'livescore'}) 
    compt = 0

    mydata = []
    matchs = []
    

    for row in table.findAll('div', attrs = {'class':'panel panel-info'}): 
        
        
        a_desc = row.find('h3', attrs = {'class':'panel-title'}).get_text() 
        matchs_ctg = {}

        for pi_b in row.findAll('div', class_ = 'panel-body'):
            grp = []

            for el in row.findAll('tr'):
                resultat = {}
                
                j = el.find('td', attrs = {'class':'lm2'}).get_text()
                s = el.find('span', attrs = {'class':'lm3_score'}).get_text()
                if "'" in j or "Mi" in j or "-" in s:
                    pass
                else:
                    heure = el.find('td', attrs = {'class':'lm1'}).get_text() 
                    time = el.find('span', attrs = {'class':'lm2_time'}).get_text()
                    eqA = el.find('span', attrs = {'class':'lm3_eq1'}).get_text()
                    eqB =  el.find('span', attrs = {'class':'lm3_eq2'}).get_text()

                    scors =  el.find('span', attrs = {'class':'lm3_score'}).get_text()

                    resultat['heure'] = heure
                    resultat['time'] = time
                    resultat['eqa'] = eqA
                    resultat['eqb'] = eqB
                    resultat['scors'] = scors
                    grp.append(resultat)
					
                
        matchs_ctg['ctgo'] = a_desc
        matchs_ctg['match'] = grp
        mydata.append(matchs_ctg)

    data = mydata
    return data

def nbrDirect():
    url = 'https://www.matchendirect.fr/live-score/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs = {'id':'livescore'}) 
    compt = 0

    mydata = []
    matchs = []
    m_direct = 0
    

    for row in table.findAll('div', attrs = {'class':'panel panel-info'}): 
        
        
        a_desc = row.find('h3', attrs = {'class':'panel-title'}).get_text() 
        matchs_ctg = {}

        for pi_b in row.findAll('div', class_ = 'panel-body'):
            grp = []

            for el in row.findAll('tr'):
                resultat = {}
                
                heure = el.find('td', attrs = {'class':'lm1'}).get_text() 
                time = el.find('td', attrs = {'class':'lm2 lm2_1'}).get_text()
                if "Mi" in time:
                    time = time[-6:]
                else:
                    time = time[-3:]

                eqA = el.find('span', attrs = {'class':'lm3_eq1'}).get_text()
                eqB =  el.find('span', attrs = {'class':'lm3_eq2'}).get_text()

                scors =  el.find('span', attrs = {'class':'lm3_score'}).get_text()

                resultat['heure'] = heure
                resultat['time'] = time
                resultat['eqa'] = eqA
                resultat['eqb'] = eqB
                resultat['scors'] = scors

                grp.append(resultat)

                m_direct += 1
                
        matchs_ctg['ctgo'] = a_desc
        matchs_ctg['match'] = grp
        mydata.append(matchs_ctg)

    data = mydata
    return m_direct