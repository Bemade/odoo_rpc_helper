from setuptools import setup, find_packages

setup(
    name='odoo_rpc_helpers',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'xmlrpc.client',
        'typing',
    ],
    author='Marc Durepos',
    author_email='marc@bemade.org',
    description='A simple wrapper for more easily running Odoo RPC commands.',
    license='MIT',
    keywords='odoo rpc xmlrpc',
)

