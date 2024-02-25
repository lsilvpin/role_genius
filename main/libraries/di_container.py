from dependency_injector import providers, containers
from main.libraries.tools.core.log_tool import LogTool
from main.libraries.adapters.integrators.core.role_interpreter import RoleInterpreter


class Container(containers.DeclarativeContainer):
    """
    Container class for dependency injection.

    This class extends the `containers.DeclarativeContainer` class from the `dependency_injector` module.
    It provides instances for each services of the system.
    """

    # Tools
    log_tool = providers.Factory(LogTool)

    # Adapters
    role_interpreter = providers.Factory(RoleInterpreter, logger=log_tool)

    # Wiring
    wiring_config = containers.WiringConfiguration(
        modules=[
            "main.apps.microservice.controllers.character_controller",
        ]
    )
