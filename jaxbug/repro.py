import importlib

importlib.import_module("jax")

from jax import __version__

assert __version__.startswith("0.3")
