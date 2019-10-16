from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='Nmspc',
        version='1.2.3',
        packages=find_packages(),
        install_requires=['NmspcPing', 'NmspcPong', ],
    )
