#!/bin/bash
# Audio-optimized Pi Zero 2 setup
# Disables unnecessary services, tunes memory, swap, logs

set -e

echo "=== 1. Disabling unnecessary services ==="
SERVICES=(
  cups
  cups-browsed
  ModemManager
  avahi-daemon
  triggerhappy
  packagekit
  rsyslog
)

for svc in "${SERVICES[@]}"; do
  if systemctl list-unit-files | grep -q "^$svc"; then
    echo "Disabling $svc..."
    sudo systemctl disable --now "$svc"
  fi
done

echo "=== 2. Keeping essential services enabled ==="
ESSENTIAL_SERVICES=(
  bluetooth
  ssh
  pipewire
  pipewire-pulse
  wayvnc.service
  dbus
  systemd
)
#  vncserver-x11-serviced

for svc in "${ESSENTIAL_SERVICES[@]}"; do
  echo "Ensuring $svc is enabled..."
  sudo systemctl enable --now "$svc" || true
done

echo "=== 3. Reducing GPU memory ==="
CONFIG_FILE="/boot/config.txt"
if ! grep -q "^gpu_mem=16" "$CONFIG_FILE"; then
  echo "gpu_mem=16" | sudo tee -a "$CONFIG_FILE"
  echo "GPU memory set to 16MB (reboot required to take effect)"
fi

#echo "=== 4. Configuring swap (1GB) ==="
#SWAPFILE="/etc/dphys-swapfile"
#sudo sed -i 's/^CONF_SWAPSIZE=.*/CONF_SWAPSIZE=1024/' "$SWAPFILE"
#sudo systemctl restart dphys-swapfile
#echo "Swap set to 1GB"

echo "=== 5. Limiting journal size ==="
JOURNAL_CONF="/etc/systemd/journald.conf"
sudo sed -i '/^SystemMaxUse=/d' "$JOURNAL_CONF"
sudo sed -i '/^RuntimeMaxUse=/d' "$JOURNAL_CONF"
echo -e "SystemMaxUse=50M\nRuntimeMaxUse=20M" | sudo tee -a "$JOURNAL_CONF"
sudo systemctl restart systemd-journald
echo "Journal size limited"

echo "=== 6. Sync filesystem and trim unused blocks ==="
sudo sync
sudo fstrim -av || true

echo "=== Setup complete ==="
echo "Reboot recommended for GPU memory changes to take effect."

