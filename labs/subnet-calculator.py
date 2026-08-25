#!/usr/bin/env python3
"""Small vendor-neutral IPv4 subnet calculation verifier for Project 002."""

import ipaddress

NETWORKS = [
    "10.10.10.0/24",
    "10.10.20.0/24",
    "10.10.30.0/24",
    "10.10.40.0/24",
]

for value in NETWORKS:
    net = ipaddress.ip_network(value)
    hosts = list(net.hosts())
    print(f"{net}: hosts={net.num_addresses - 2}, first={hosts[0]}, last={hosts[-1]}, broadcast={net.broadcast_address}")
