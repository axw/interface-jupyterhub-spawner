import json

from charmhelpers.core import hookenv
from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes


class JupyterHubSpawnerProvides(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:jupyterhub-spawner}-relation-{joined,changed}')
    def changed(self):
        if self.get_remote('spawner-class'):
            self.set_state('{relation_name}.available')

    @hook('{provides:jupyterhub-spawner}-relation-{broken,departed}')
    def broken(self):
        self.remove_state('{relation_name}.available')

    def config(self):
        spawner_class = self.get_remote('spawner-class')
        spawner_config = self.get_remote('spawner-config')
        if spawner_config:
            spawner_config = json.loads(spawner_config)
        else:
            spawner_config = {}
        return spawner_class, spawner_config

