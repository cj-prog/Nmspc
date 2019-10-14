from setuptools import setup

if __name__ == "__main__":
    setup(
        name='Nmspc',
        version='1.2.3',
        packages=['nmspc._nmspc', ],
        install_requires=['NmspcPing', 'NmspcPong', ],
    )
k