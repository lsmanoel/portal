# menuconfig
# ---------------------
	git clone --recurse-submodules https://github.com/profmarcondes/emb22109_20191.git
	emb22109_20191/projects/ ./create.sh gateway raspberrypi3
	emb22109_20191/projects/gateway/  make menuconfig

		Build options/Enable complier cache [*]
		Toolchain/Toolchain type (External toolchain)
		System configuration/ Root password (gateway)
		System configuration/ System hostname (rpi_gateway)
		System configuration/after  $(BR2_EXTERNAL_EMB22109_PATH)/board/scripts/tar-boot.sh
		Target package/Network applications (dropbear)
		Target package/Network applications (mosquitto)
		Target package/Network applications (hostapd)
		Target package/Network applications (wpa_suppliant)
		Target package/Library/Graphics (opencv3)
		Target package/System tools (htop)
		Target package/Text editor (nano)
		Target interpreter language/python3
		Target real time/xenomai
		Host utilities cmake
		Host utilities opkg-utils
		Host utilities python-cython
		Filesystem images/ tar the root filesystem: Compression method (gzip)
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

# ajuste da ethernet no boot
# ---------------------	
	nano /etc/init.d/S41_aux
		#!/bin/sh

		start() {
		        printf "Starting Xunxo: "
		        sleep 2s
		        /etc/init.d/S40network restart
		        [ $? = 0 ] && echo "OK" || echo "FAIL"
		}
		stop() {
		        printf "Stopping Xunxo: OK"
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
	chmod +x /etc/init.d/S41_aux
