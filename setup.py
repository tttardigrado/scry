from setuptools import setup
setup(
    name='scry',
    version='0.1.0',
    packages=['scry'],
    install_requires=[
        "prompt_toolkit",
        "click",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'scry = scry.__main__:main'
        ]
    })
