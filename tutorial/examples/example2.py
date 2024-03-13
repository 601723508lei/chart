interface GigabitEthernet0/1
  description Connection to LAN
  bandwidth 10000
  service-policy output QoS-Policy

class-map match-all VOICE
  match access-group 101

policy-map QoS-Policy
  class VOICE
    priority percent 30
  class class-default
    fair-queue
