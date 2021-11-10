from os import PathLike
import toml
from urllib import request
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        toml_string = {}
        toml_string = toml.loads(content)
        print(toml_string)
        print()
           
        #print(toml_string['poetry'])
        print()
        #print(toml_string['tool'])
        print()
        #print(toml_string[''])
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", toml_string['tool']['poetry']['dependencies'], toml_string['tool']['poetry']['dev-dependencies'])
