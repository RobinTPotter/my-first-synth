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

still learning supercollider but with scide did manage a vox continental alike with sliders as ui components

was about to adapt to headless when realised would have no way of controlling it

have a waveshare display which was going to make a game with but never got around to it

first thing was to add a bunch of auto connect stuff for pipewire (see pdf for part of the story made under my limited instructions by chat-gpt)


