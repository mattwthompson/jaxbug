from openff.utilities import has_package


def get_jax_version() -> str:
    if has_package("jax"):
        import jax

        return jax.__version__
    else:
        return 0.0
