# menuconfig
# ---------------------
	git clone --recurse-submodules https://github.com/profmarcondes/emb22109_20191.git
	emb22109_20191/projects/ ./create.sh gateway raspberrypi3
	emb22109_20191/projects/gateway/  make menuconfig

		Build options > Enable complier cache [*]
		Toolchain > Toolchain type > External toolchain
		System configuration >  Root password > gateway
		System configuration >  System hostname > rpi_gateway
		System configuration > after  $(BR2_EXTERNAL_EMB22109_PATH)/board/scripts/tar-boot.sh
		Target package > Network applications > dropbear
		Target package > Network applications > mosquitto
		Target package > Library/Graphics  > opencv3
		Target package > System tools  > htop
		Target package > Text editor  > nano
		Target interpreter language > python3
		Target interpreter language > external python > pip
		Target real time > xenomai
		Host utilities > cmake
		Host utilities > opkg-utils
		Host utilities > python-cython


		Target package > Network applications > hostapd
													Enable hostap driver
													Enable nl80211 driver
													Enable ACS
													Enable EAP
													Enable WPS

		Target package > Network applications > wpa_supplicant
													Enable nl80211 support
													Enable WPS
													Install wpa_cli
													Install wpa_pass
		Target package > Network applications > wireless tools
		Target package > Network applications > iptables
		Target package > Network applications > dhcpcd  # ADD
		Target package > Network applications > dnsmasq # ADD
		Target packages > Networking applications > iw   # ADD
		Target packages > Hand ... > Firmware > RPi_BT   # ADD, driver module bluetooth
		Target packages > Hand ... > Firmware > RPi_Wifi # ADD, driver module wifi

		Filesystem images > tar the root filesystem: Compression method (gzip)
		[save]
		make savedefconfig

	emb22109_20191/projects/Gateway make 2>&1 | tell build.log

# preparar SD Card ----
# ---------------------
	# remover todas as partições existentes
	# criar 2 novas partições: boot, rootfs
	# boot: 50MB, Fat32
	# rootfs: o retante, EXT4

	# montar partições para utilizar o cartão SD
	mkdir /media/boot
	mkdir /media/rootfs
	mount /dev/mm..p1 /media/boot
	mount /dev/mm..p2 /media/rootfs

# mover arq. p/ SD Card
# ---------------------
boot:
	tar -C /media/jonas/boot -zxf rootfs.tar.gz
rootfs:
	tar -C /media/jonas/root -zxf rootfs.tar.gz

# dhcpcd
# ---------------------
nano /etc/dhcpcd.conf

# dnsmasq
# ---------------------
nano /etc/dnsmasq.conf

# hostapd
# ---------------------
nano /etc/hostapd.conf
	interface=wlan0
	driver=nl80211
	hw_mode=g
	channel=10
	ieee80211d=1
	ieee80211h=1
	ieee80211n=1	
	wpa=2
	wpa_key_mgmt=WPA-PSK
	wpa_pairwise=TKIP
	rsn_pairwise=CCMP
	ssid=rpi_gateway
	wpa_passphrase=123123123	
	ignore_broadcast_ssid=0
	macaddr_acl=0
	auth_algs=1

# config. interfaces
nano /etc/network/interfaces 
	auto lo
		iface lo inet loopback
	auto eth0
		iface lo inet dhcp

	auto wlan0
		iface wlan0 inet static
		network
		address
		broadcast 
		gateway 

# controle de servico
/etc/init.d/S40network	# ja vem feito
/etc/init.d/S41dhcpd	# ja vem feito
/etc/init.d/S50dropbear	# ja vem feito
/etc/init.d/S50mosquito	# ja vem feito
/etc/init.d/S80dnsmasq	# ja vem feito

/etc/init.d/S42hostapd 	# criqar
/etc/init.d/S99iptable	# criqar

# controle do hostapd
nano /etc/init.d/S42hostapd
	#!/bin/sh

	start() {
	        printf "Starting hostapd: "
	        sleep 2s
	        hostapd -B /etc/hostapd.conf
	        [ $? = 0 ] && echo "OK" || echo "FAIL"
	}
	stop() {
	        printf "Stopping hostapd: "
	}
	restart() {
	        stop
	        start
	}

	case "$1" in
	  start)
	        start
	        ;;
	  stop)
	        stop
	        ;;
	  restart|reload)
	        restart
	        ;;
	  *)
	        echo "Usage: $0 {start|stop|restart}"
	        exit 1
	esac

	exit $?
chmod +x /etc/init.d/S42hostapd # tornar executavel
	# ...

# controle das rotas
nano /etc/init.d/S99iptable
	# ...

chmod +x /etc/init.d/S99iptable # tornar executavel

# reiniciar
reboot

# deligar
poweroff
