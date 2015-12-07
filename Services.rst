#format rst

Start, stop, and check the status of network services
=====================================================

.. contents:: :depth: 2

Start/Stop Networking
---------------------

* The traditional way way: /etc/init.d/networking {start|stop|restart}

* RHEL 6: service network {start|stop|restart}

* RHEL 7: systemctl {start|stop|restart} network.service

General Service Management
--------------------------

* Start service : systemctl start <service>

* Stop service : systemctl stop <service>

* Query if a service is running : systemctl is-active <service>

* Enable a service at boot: systemctl enable <service>

* Disable a service at boot: systemctl disable <service>

* Check if a service is enabled at boot: systemctl is-enabled <service>

* Check the status of a service: systemctl status <service>

* Permanently disable a service: systemctl mask <service>

List of Network Services
------------------------

* httpd

netstat
-------

* http://tldp.org/LDP/nag2/x-087-2-iface.netstat.html

