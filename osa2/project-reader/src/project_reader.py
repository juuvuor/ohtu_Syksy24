from urllib import request
# pylint: disable=import-error
import toml
# pylint: enable=import-error
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta
        # Project-olio sen tietojen perusteella
        data = toml.loads(content)


        poetry = data.get('tool', '').get('poetry','')
        name = poetry.get('name', '')
        description = poetry.get('description', '')
        license = poetry.get('license', '')
        authors = poetry.get('authors', [])
        dependencies = poetry.get('dependencies', [])
        dev_dependencies = poetry.get('group', {}).get('dev', {}).get('dependencies', [])

        # Create and return a Project object
        return Project(name, description, license, authors, dependencies, dev_dependencies)



# {
#     'tool': {
#         'poetry': {
#             'name': 'Ohtutesting app',
#             'version': '0.0.1',
#             'description': 'Sovellus joka toimii testisyötteenä ohtun viikon 2 laskareihin',
#             'authors': ['Matti Luukkainen', 'Kalle Ilves'],
#             'license': 'MIT',
#             'dependencies': {
#                 'python': '^3.10',
#                 'Flask': '^3.0.0',
#                 'editdistance': '^0.6.2'
#             },
#             'group': {
#                 'dev': {
#                     'dependencies': {
#                         'coverage': '^7.3.2',
#                         'robotframework': '^6.1.1',
#                         'robotframework-seleniumlibrary': '^6.1.3',
#                         'requests': '^2.31.0'
#                     }
#                 }
#             }
#         }
#     },
#     'build-system': {
#         'requires': ['poetry-core'],
#         'build-backend': 'poetry.core.masonry.api'
#     }
# }