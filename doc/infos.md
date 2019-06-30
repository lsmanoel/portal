Target Architecture:
    ARM

 Build Options
     Compiler cache

Toolchain
    External

System configuration
-> network omterface DHCP
    eth0 ??? 
-> pass root:
       portal
-> System hostname:
      rpi_portal

filesystem images -> Compression method
    gzid

Target packages -> Libraries
-> Network applications:
       mosquitto (MQTT)
       openssh (SCP)
-> Graphics:
       vl4
       opencv3
-> Text editor
      nano

-------------------------------------------------------
COMPILADOR, EXT?
build options-> Commands -> scp
toolchain -> compilador
toolchain -> external
system configuration -> DHCP
builroot | rootfs_overlay ???
