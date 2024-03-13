router bgp 65000
  network 192.168.0.0 mask 255.255.255.0
  neighbor 10.0.0.1 remote-as 65001
