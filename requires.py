import json

from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class JupyterHubSpawnerRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:jupyterhub-spawner}-relation-{joined,changed}')
    def changed(self):
        self.set_state('{relation_name}.available')

    @hook('{requires:jupyterhub-spawner}-relation-{departed,broken}')
    def broken(self):
        self.remove_state('{relation_name}.available')

    def set_spawner(self, spawner_class, config=None):
        self.set_remote('spawner-class', spawner_class)
        if config:
            self.set_remote('spawner-config', json.dumps(config))
