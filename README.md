jk_trioping
==========

Introduction
------------

This python module provides an asynchroneous version of ping. It is based on the trio framework.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_trioping)

Why this module?
----------------

It is not too difficult to perform a ping to multiple hosts in parallel. Suprisingly modules, examples or even binaries to do exactly that are hard to find. This modules now offers a simple solution to that problem.

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import trio
import jk_trioping
```

### Perform single ping

```python
async def main(hostAddress):
	ret = await jk_trioping.ping(
		host = hostAddress,
		timeout = 2,
		repeats = 1
	)
	print(ret)

trio.run(main, "127.0.0.1")
```

This will perform a single ping to a single host. The result will look something like this:

```
0.063
```

### Perform multiple pings

```python
async def main(hostAddresses):
	ret = await jk_trioping.multiPing(
		hosts = hostAddresses,
		timeout = 2,
		repeats = 1
	)
	print(ret)

trio.run(main, [ "127.0.0.1", "localhost" ])
```

This will perform a ping to two hosts (addressing one by IP address, one by name) and print something like this:

```
{'localhost': 0.071, '127.0.0.1': 0.073}
```

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



