from setuptools import setup

setup(
    name="cyber_components",
    version="1.0.0",
    packages=[
        "cyber_components",
        "cyber_components.db",
        "cyber_components.db.models",
        "cyber_components.db.associations"
    ],
    url="",
    license="",
    author="Meshulam Silk",
    author_email="",
    description="",
    install_requires=[
        "sqlalchemy",
        "sqlalchemy-utils",
    ],
)
