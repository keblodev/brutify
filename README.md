# wifi-bruteforce
proof that bruteforcing wifi networks is completely unreasonable -> it's just too slow

# Requirements
 - osx
 - python > 3.x
 
# Approach:
 - given an alphabeth of `01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*` and an `CoreWLAN` interface try bruteforcing a password for a targeted network.
 
# Result:
 bruteforcing even a simple passwork takes days just because the `CoreWLAN` interface's response is just too slow
