from setuptools import setup, find_packages

setup(
    name="pyxmb",
    version="0.1.0",
    description="A desktop launcher that emulates the XMB (XrossMediaBar) user experience",
    author="ImFenyx",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.5.0",
    ],
    entry_points={
        'console_scripts': [
            'pyxmb=pyxmb.main:main',
        ],
    },
    python_requires='>=3.8',
)
