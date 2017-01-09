#format rst

Locating and interpreting system log files and journals.
========================================================

.. contents:: :depth: 2

System Logs
-----------

* Are usually contained within /var/log.

* Are **definitely** contained within the directory specified in /etc/rsyslog.conf.

* SELinux logs in /var/log/audit/audit.log.

systemd
-------

* systemd-analyze : Returns the duration of the boot process.

* systemd-analyze blame : Returns the amount of time each process spent during the boot process.

Journals
~~~~~~~~

* journalctl : Returns the system event log.

* journalctl <path to daemon> : Returns all events related to daemon (example argument: *journalctl /sbin/crond*)

* journalctl -b : Returns all events since last boot.

* journalctl --since=today : Returns all events since today.

* journalctl -p err : Returns all events with syslog priority of 'error'.

* journalctl -f : Returns last 10 events; analogous to using tail with /var/log/messages in previous versions of RHEL.

-------------------------



SystemsAdministration_

.. ############################################################################

.. _SystemsAdministration: ../SystemsAdministration

