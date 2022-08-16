import importlib


def has_package(package_name: str):
    try:
        importlib.import_module(package_name)
    except ImportError:
        return False
    return True


def get_jax_version() -> str:
    if has_package("jax"):
        import jax

        return jax.__version__
    else:
        return 0.0
