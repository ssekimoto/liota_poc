from liota.core.package_manager import LiotaPackage
from liota.lib.utilities.utility import read_user_config

config = read_user_config('/tmp/cti_Prop.conf')

class PackageClass(LiotaPackage):

    def run(self, registry):

        from liota.entities.edge_systems.general_edge_system import GeneralEdgeSystem

        edge_system = GeneralEdgeSystem(config['EdgeSystemName'])
        registry.register("edge_system", edge_system)

    def clean_up(self):
        pass
