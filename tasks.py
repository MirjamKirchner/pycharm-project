from invoke import task
from invoke.context import Context


@task
def setup(context: Context):  # tasks are not allowed to have underscores
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
    # TODO check whether project is already set up and abort if so
    _initialize_poetry(context)
    _install_dependencies(context)
    _activate_venv(context)
    _activate_precommit_hooks(context)


def _initialize_poetry(context: Context):
    context.run("poetry init")
    context.run("git add pyproject.toml")


def _install_dependencies(context: Context):
    dependencies = (
        "black --group coding",  # Code formatting (PEP-8)
        "isort --group coding",  # Code formatting (order imports)
        "pylint --group coding",  # Code style
        "mypy --group coding",  # Type hints
        "pytest --group testing",  # Tests
        "pre-commit --group cicd",  # Pre-commit hooks
        "invoke --group cicd",  # CLI-invokable tasks
    )
    for dependency in dependencies:
        context.run("poetry add " + dependency)


def _activate_precommit_hooks(context: Context):
    context.run("pre-commit install")
    context.run("pre-commit autoupdate")
    context.run("git add .pre-commit-config.yaml")  # This has no effect


def _activate_file_watchers(context: Context):
    print("I will activate file watchers")


def _activate_venv(context: Context):
    context.run("poetry shell")


if __name__ == "__main__":
    pass
