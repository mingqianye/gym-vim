from setuptools import setup

setup(
    name='gym_vim',
    version='0.0.7',
    url="https://github.com/mingqianye/gym_vim",
    author="Mingqian Ye",
    license="MIT",
    packages=["gym_vim", "gym_vim.envs"],
    install_requires=['gym', 'sklearn', 'numpy', 'pynvim']
)
