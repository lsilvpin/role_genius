from main.libraries.tools.core.log_tool import LogTool


class RoleInterpreter:
    """
    The RoleInterpreter class is responsible for interpreting roles and handling role-specific settings.

    Attributes:
        __role (str): The current role being interpreted.
    """

    __role: str

    def __init__(self, logger: LogTool):
        """
        Initializes a new instance of the RoleInterpreter class.

        Args:
            logger (LogTool): An instance of the LogTool class.
        """
        self.logger = logger

    def load(self, role: str) -> None:
        """
        Loads the settings for the specified role.

        Args:
            role (str): The role to load settings for.
        """
        self.logger.info(f"Loading {role} settings...")
        self.__role = role

    def get_role(self) -> str:
        """
        Gets the current role being interpreted.

        Returns:
            str: The current role being interpreted.
        """
        return self.__role

    def prompt(self, msg: str) -> str:
        """
        Prompts the user with a message and returns a response specific to the current role.

        Args:
            msg (str): The message to prompt the user with.

        Returns:
            str: The response from the current role.
        """
        return f"Response from role {self.__role}"
