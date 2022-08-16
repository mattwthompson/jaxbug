import sys

from jaxbug.repro import get_jax_version


def test_jaxbug_imported():
    import jax

    assert "jax" in sys.modules

    assert get_jax_version() == "0.3.16"
