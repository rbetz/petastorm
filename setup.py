#
# Uber, Inc. (c) 2018
#
"""This setup script should be launched by running
source/python/av/ml/dataset_toolkit/setup/package.sh"""

import setuptools
from setuptools import setup
from dataset_toolkit import __version__

REQUIRED_PACKAGES = [
    'numpy>=1.13.3',
    'Pillow>=3.0',
    'pyspark>=2.1.2',
    'pyzmq>=14.0.0',
    # 'pyarrow>=0.8',  # Temporarary removing dependency on pyarrow - we'll pick up whatever we have in ATG repo
                       # Once there is 0.10, we'll be able to use stock, non-atg version.
    'pandas>=0.19.0',
    'diskcache>=3.0.0',
]

EXTRA_REQUIRE = {
    'tf': ['tensorflow>=1.4.0'],
    'tf_gpu': ['tensorflow-gpu>=1.4.0'],
    'tf_atg': ['atg-tensorflow-gpu>=1.4.0'],
    'pyarrow': ['pyarrow>=0.8'],  # TODO(yevgeni): once ATG goes to stock 0.10 (instead of atg-pyarrow=0.9.0.1), we
                                  # make the require mandatory.
}

packages = setuptools.find_packages()

setup(
    name='dataset_toolkit',
    version=__version__,
    install_requires=REQUIRED_PACKAGES,
    packages=packages,
    description='Dataset toolkit',
    license='TBD',
    extras_require=EXTRA_REQUIRE,
)
