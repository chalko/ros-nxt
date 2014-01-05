from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['nxt_controllers'],
    package_dir={'nxt_controllers': 'src'}
)

setup(**d)
