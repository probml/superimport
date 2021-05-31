from distutils.core import setup

setup(
    name="superimport",
    packages=["superimport"],
    version="0.1c",
    license="MIT",
    description="Simple reverse lookup for the current python file missing packages",
    author="Mahmoud Soliman",
    author_email="mjs@aucegypt.edu",
    url="https://github.com/probml/superimport",
    download_url="https://github.com/probml/superimport/archive/refs/tags/v_01c.tar.gz",
    keywords=["setup", "runtime", "automation"],
    install_requires=[
        "pipreqs",
        "requests",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
