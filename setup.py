from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='mcrpy',
      version='0.2.0',
      description='Microstructure characterization and reconstruction in Python',
      url='https://github.com/NEFM-TUDresden/MCRpy',
      author='NEFM-TUDresden',
      author_email='paul.seibert@tu-dresden.de',
      license='Apache2.0',
      packages=find_packages(),
      install_requires=[
          'numpy>=1.20.1',
          'tensorflow>=2.7.1',
          'matplotlib>=3.3.4',
          'scipy>=1.6.2',
          'pyevtk',
          'pyYAML',
      ],
      extras_require={
          'animations': ['imageio-ffmpeg>=0.4.5'],
          'GUI': ['Gooey>=1.0.8.1']
          },
      package_data={'': ['*.pkl', '*.npy', '*.pickle', '*.png']},
      zip_safe=False)