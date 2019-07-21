import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
      name='hot-sequence',
      version='0.1.0',
      description="Like Emacs Key Sequences",
      long_description_content_type="text/markdown",
      long_description=long_description,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
      ],
      url='http://github.com/buckley-w-david/hot-sequence',
      author='David Buckley',
      author_email='buckley.w.david@gmail.com',
      license='MIT',
      packages=['hot_sequence'],
      install_requires=[],
)
