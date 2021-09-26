"""This file contains shared fixtures and pytest hooks.

https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files
"""

from _pytest.config import Config
from _pytest.nodes import Item
from typeguard import typechecked
from typeguard.importhook import install_import_hook


def pytest_configure(config: Config) -> None:
    """Initial pytest configuration hook.

    Note:
        We cannot use --typeguard-packages=tests since we currently get the
        following error:

        typeguard cannot check these packages because they are already imported

        When trying to install an import hook for the 'tests' pacakge (i.e.
        install_import_hook('tests')), it breaks pytest's assertion rewriting.
        See the following URL for more information:

        https://docs.pytest.org/en/stable/writing_plugins.html#assertion-rewriting

    See the following URL for more information on this pytest hook:
        https://docs.pytest.org/en/6.2.x/reference.html#pytest.hookspec.pytest_configure
    """
    del config

    install_import_hook("result")


def pytest_runtest_call(item: Item) -> None:
    """Called once for each test function.

    See the following URL for more information on this pytest hook:
        https://docs.pytest.org/en/6.2.x/reference.html#pytest.hookspec.pytest_runtest_call
    """
    # Decorate every test function [e.g. test_foo()] with typeguard's
    # typechecked() decorator.
    test_func = getattr(item, "obj", None)
    if test_func is not None:
        setattr(item, "obj", typechecked(test_func))
