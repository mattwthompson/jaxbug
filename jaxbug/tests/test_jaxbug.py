from jaxbug.repro import get_jax_version


def test_jaxbug_imported():
    assert get_jax_version() == "0.3.16"
