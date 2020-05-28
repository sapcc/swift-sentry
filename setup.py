from setuptools import setup, find_packages

setup(
    name="sapcc-swift-sentry",
    version="0.1.0",
    license="Apache License 2.0",
    description="Openstack Swift Custom Log Handler for Sentry",
    author="Muhammad Talal Anwar",
    url="https://github.com/sapcc/swift-sentry",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: OpenStack",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["sentry-sdk==0.14.4"],
)
