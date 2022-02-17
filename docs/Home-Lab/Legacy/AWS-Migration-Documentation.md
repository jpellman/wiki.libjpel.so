# Documentation Concerning Migration from Linode to AWS

## General Notes
 * I killed the Wordpress service because I never used it and MoinMoin was serving me well for what I wanted (a place to throw my ideas) anyways.

## AMI Used and Dependencies I needed to install
I used a fresh CentOS 7 AMI: ami-2051294a.  wget was not installed, nor was vim (_yum install wget vim_).  Wanted to install htop too, but EPEL repos not available.  Followed instructions to get EPEL from [here](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-enable-epel/).  Step 3 is incorrect- _rpm –ivh epel-release-7-5.noarch.rpm_ should be _rpm epel-release-7-5.noarch.rpm -ivh_ for some befuddling reason lost to the depths of time.  The former command will print a help screen; the latter does what it's supposed to do.

## Apache Migration Notes
Ran _yum install httpd_.  Removed default default /etc/httpd.  rsync'd /etc/httpd from old VPS.  Had to remove PHP config files left from Wordpress (_rm /etc/httpd/conf.modules.d/10-php.conf_ ; _rm /etc/httpd/conf.d/php.conf_).  Cloned main branch of this repo into /var/www/html.

## MoinMoin Migration Notes
I re-installed MoinMoin 1.9.8 on the AMI (also wsgi; _yum install wsgi_).  Removed default /usr/local/share/moin and rsync'd /usr/local/share/moin from old VPS.  The AWS AMI has SELinux enabled by default.  This caused some issues with MoinMoin being able to open up the data directory.  See [here](https://moinmo.in/MoinMoinQuestions#MoinMoinQuestions.2FInstalling.MoinMoin_with_WSGI_can.27t_find_datadir) for resolution.  Started Apache (_service start httpd_).

## Primitive Backup
Migrated primitive backup scripts and last 10 backups to /usr/local/bin/backup.  Created a dedicated user with passwordless ssh for so that I can rsync tar'd backups directly to my home computer nightly using a cronjob.  Added the following line to root's crontab:

_35 20 * * 0,4 /usr/local/bin/backup/bin/fullBackup.sh_

This backup system is very rudimentary and exists as it does primarily because I don't want to spend more money on this than it is worth.  It's mostly so that the Wiki doesn't get totally zapped if something happens to the Amazon instance.  I can always start using snapshots if this gets more serious (and/or if I have more disposable income).

## Misc
 * Updated DNS entry to point to new IP address.
 * Archived home directories to home laptop (these looked like trash, but I decided to keep them at least for a bit as a precaution).
