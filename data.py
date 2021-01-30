from dataclasses import dataclass
import requests


class Data:
    """ Stores all data in a single class """

    def __init__(self):
        # Get data
        self.covidData = requests.get(
            "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=statusBar_external_data"
        )
        self.dosesData = requests.get(
            "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data"
        )
        self.popData = requests.get(
            "https://www.census.gov/popclock/data/population.php/us?date=20210128&_=1611954842611"
        )

    def getHerd(self):
        # Process data
        pop = self.popData.json()["us"]["population"]
        doses = self.dosesData.json()["vaccination_data"][63]["Doses_Administered"]
        recovered = (
            self.covidData.json()["statusBar"][0]["us_total_cases"]
            - self.covidData.json()["statusBar"][0]["us_total_deaths"]
        )

        # Format herd
        herd = doses + recovered
        herdRaw = (herd / pop) * 100
        return "{0:.4}".format(herdRaw)

    def getVacc(self):
        return self.dosesData.json()["vaccination_data"][63]["Doses_Administered"]

    def getCasesDeaths(self):
        casesDeaths = [
            self.covidData.json()["statusBar"][0]["us_total_cases"],
            self.covidData.json()["statusBar"][0]["us_total_deaths"],
        ]
        return casesDeaths
