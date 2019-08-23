#!/usr/bin/python3


import trio

import jk_trioping

async def main():

	# single ping with host not answering

	print("Pinging:", "7.7.7.7", "1 time")
	t = trio.current_time()
	duration = await jk_trioping.ping("7.7.7.7")
	dt = trio.current_time() - t
	print("Duration (1 ping):", duration, "ms")
	print("Total time:", 1000*dt, "ms")

	print()

	# single ping with host answering

	print("Pinging:", "8.8.8.8", "1 time")
	t = trio.current_time()
	duration = await jk_trioping.ping("8.8.8.8")
	dt = trio.current_time() - t
	print("Duration (1 ping):", duration, "ms")
	print("Total time:", 1000*dt, "ms")

	print()

	# multiple pings with host answering

	print("Pinging:", "8.8.8.8", "5 times")
	t = trio.current_time()
	duration = await jk_trioping.ping("8.8.8.8", repeats=5)
	dt = trio.current_time() - t
	print("Duration (5 pings):", duration, "ms")
	print("Total time:", 1000*dt, "ms")
	print("Avg time spent per ping:", 1000*dt/3, "ms")

	print()

	# single pings with hosts answering

	print("Pinging:", ["8.8.8.8", "9.9.9.9", "google.com", "yahoo.com"], "1 time")
	t = trio.current_time()
	durations = await jk_trioping.multiPing(["8.8.8.8", "9.9.9.9", "google.com", "yahoo.com"])
	dt = trio.current_time() - t
	print("Durations (4 pings):", durations)
	print("Total time:", 1000*dt, "ms")
	print("Avg time spent per ping:", 1000*dt/4, "ms")
#

trio.run(main)

