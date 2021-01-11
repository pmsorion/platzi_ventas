from setuptools import setuptools

setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requieres=[
        'Click',
    ],
    entry_points='''
        [console_scrips]
        pv=pv:cli
    ''',
)