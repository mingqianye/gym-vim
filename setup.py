from setuptools import setup, find_packages

setup(name='gym_vim',
    version='0.0.5',
    url="https://github.com/mingqianye/gym_vim",
    author="Mingqian Ye",
    license="MIT",
    find_packages=find_packages(),
    install_requires=['gym', 'sklearn', 'numpy', 'pynvim']
)
