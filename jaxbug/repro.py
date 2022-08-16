from openff.utilities import has_package


if has_package("jax"):
    print("maybe this worked")
else:
    print("maybe not")
