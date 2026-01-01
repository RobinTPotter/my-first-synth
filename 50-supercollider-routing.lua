rule = {
 matches = {
    {
      { "application.name", "matches", "SuperCollider" },
    },
 },
 apply_properties = {
   ["node.autoconnect"] = true,
   ["target.object"] = {
      "bluez_output.*a2dp-sink", -- Bluetooth headphones
      "alsa_output.*hdmi.*", -- HDMI output
      "alsa_output.usb-USB_Audio_Device.playback_FL", -- USB left playback
      "alsa_output.usb-USB_Audio_Device.playback_FR" 
   }
 }
}

table.insert(alsa_monitor.rules, rule)

input_rule = {
  matches = {
    {
      { "application.name", "matches", "SuperCollider" },
    },
  },
  apply_properties = {
    ["node.autoconnect"] = true,
    ["target.object"] = {
      "alsa_input.usb-USB_Audio_Device.capture_MONO"
    }
  }
}

table.insert(alsa_monitor.rules, input_rule)
