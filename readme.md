# my first synth

i have:

- a raspberry pi zero 2, 
- a midi keyboard, 
- a waveshare 1.3" IPS LCD Display Module for Raspberry Pi Pico (240x240)
- an usb hub 4 way,
- an otg adapter
- usb sound card
- usb midi adapter

i installed pios 64bit as it will do bluetooth almost reliably with pipewire

installed pipewire-jack a d wireplumber was already there

i installed supercollider which does work headlessly but will crash trying to boot the server in scide

command to start supercollider

`
QT_QPA_PLATFORM=offscreen pw-jack sclang sc.scd
`

where I am using my own sc.scd which may move to startup

still learning supercollider but with scide did manage a vox continental
alike with sliders as ui components

was about to adapt to headless when realised would have no way of
 controlling it

have a waveshare display which was going to make a game with but 
never got around to it

first thing was to add a bunch of auto connect stuff for pipewire 
(see pdf for part of the story made under my limited instructions by chat-gpt)


also had a go at making a final img for flashing pizero2 but no where 
to put it really


pattern will be this

- pizero2:
 - runs supercollider
 - runs a osc sender (to itself) which reads and writes over uart/usb to pico
 - has pico and screen with buttons 

- will need a sc startup.scd which initiates midi and any bus
collections. in development will create and add synthdefs, for 
real the synthdef compilation will be separate (?). midi set up here

- will need a service which communicates with pico

- will need a service to send osc messages

## misc.

where the synthdefs are written to: `.local/share/SuperCollider/synthdefs/`
startup file: `.config/SuperCollider/startup.scd`


## image related

/boot/ssh - empty
make a hotspot `sudo nmcli device wifi hotspot ssid <example-network-name> password <example-password>`
apparently wpa_supplicant is no longer used so `/boot/wpa_supplicant.conf`
doesn't work


## log

created the 50-supercollider-routing.lua and had a go
at shrinking the services using service_strip.sh


got tony goodhew's micropython driver from pihut (where i got the 
display) and renamed to ws.py for (my) convenience and 


made `yellow.py` which seems slow but works and will be 
fine for menus etc.

