from setuptools import setup, find_packages

setup(
    name='DTreesDRules',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['datasets/DecisionRuleSystems/*.csv'],
    },
)
