# -1 define pre-requisites: poetry, python3
# 0. set up virtual environment as venv
# 1. install requirements and install into venv
# Enable pre-commit hooks
# Setup file watchers
# In pycharm, set Tools --> Python integrated tools --> Doc String format --> NumPy
from warnings import warn
from invoke import task
from invoke.exceptions import UnexpectedExit
from typing import Final

POETRY_BOOLS: Final = {
    True: "true",
    False: "false"
}

@task
def setup(context):  # tasks are not allowed to have underscores
    """
    Prints 'Hello, world!'

    Parameters
    ----------
    context:
        invoke APi context

    Returns
    -------
    None
    """
    _setup_pvenv(context)
    _install_dependencies(context)


def _setup_venv(
        context,
        python_version: str = "system",
        option: str = True
):
    cmd_poetry_version = "poetry --version"
    try:
        print("-----------------------------------------------------------------------------------------------------\n"
              "Tools:\n"
              "Dependency management and packaging tool:")
        context.run(cmd_poetry_version)
        print("-----------------------------------------------------------------------------------------------------\n")
    except UnexpectedExit:
        raise(
            "Failed to execute command '{command}'.\n"
            "This indicates that the required dependency management and packaging tool 'Poetry' is not installed.\n"
            "Check out 'https://python-poetry.org/' for installation instructions.".format(
                command=cmd_poetry_version
            )
        )
    # Update pyproject.toml using information from git
    # Add black, pylint, ...
    # Enable options https://python-poetry.org/docs/cli/?ref=serpapi.com#install
    cmd_setup_venv = "poetry install" + option
    print("I will setup the virtual environment using poetry!")


def _install_dependencies(context):
    # black -- formatting
    # pytest -- testing
    # pre-commit -- pre-commit hooks
    # mypy -- type hints
    # pylint(, flake8 ?) -- code linter
    print("I will install all project requirements!")


def _activate_precommit_hooks():
    print("I will activate pre-commit hooks!")


def _activate_file_watchers():
    print("I will activate file watchers")


if __name__ == "__main__":
    pass
