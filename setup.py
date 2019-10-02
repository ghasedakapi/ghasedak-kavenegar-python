from setuptools import setup
import sys

requires = ['requests>=0.10.8']
if sys.version_info < (2, 6):
    requires.append('simplejson')

setup(
    name = "ghasedakkavenegar",
    py_modules = ['ghasedakkavenegar'],
    version = "1.1.3",
    description = "Ghasedak-Kavenegar Migration Python library",
    author = "GhasedakBot",
    author_email = "support@ghasedak.io",
    url = "https://github.com/ghasedakapi/ghasedak-kavenegar-python",
    keywords = ["kavenegar", "sms", "ghasedak"],
    install_requires = requires,
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        ]
     )