from setuptools import setup, find_packages

setup(
    name='pulp_deb_plugins',
    version='1.1.0a1',
    packages=find_packages(exclude=['test', 'test.*']),
    url='http://www.pulpproject.org',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    description='plugins for deb support in pulp',
    entry_points={
        'pulp.importers': [
            'importer = pulp_deb.plugins.importers.importer:entry_point',
        ],
        'pulp.distributors': [
            'distributor = pulp_deb.plugins.distributors.distributor:entry_point'  # noqa
        ],
        'pulp.server.db.migrations': [
            'pulp_deb = pulp_deb.plugins.migrations',
        ],
        'pulp.unit_models': [
            'deb=pulp_deb.plugins.db.models:DebPackage',
        ],
   },
   include_package_data=True,
    data_files=[
        ('/etc/httpd/conf.d', ['etc/httpd/conf.d/pulp_deb.conf']),
        ('/usr/lib/pulp/plugins/types', ['types/deb.json']),
    ],
    install_requires=[
    ],
)
