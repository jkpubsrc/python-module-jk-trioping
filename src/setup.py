################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Framework :: Trio",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This python module provides an asynchroneous version of ping. It is based on the trio framework.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-trioping/tarball/0.2020.4.1",
	include_package_data = False,
	install_requires = [
		"trio",
		"jk_console",
		"jk_argparsing",
		"jk_json",
	],
	keywords = [
		"trio",
		"ping",
	],
	license = "Apache 2.0",
	name = "jk_trioping",
	packages = [
		"jk_trioping",
	],
	scripts = [
		"bin/multiping.py",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-trioping",
	version = "0.2020.4.1",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
