Notes on Backups of Maxwell's ZFS Pool to AWS (DEPRECATED)
===========================================================

*NOTE: I no longer run ZFS at home except for ad-hoc experiments.  This is because I found ZFS to consistently be overkill for my personal needs.  In general, I've been re-assessing how I go about home-labbing so that long-running infrastructure / devices are much less complex.  I realized that the overhead / complexity of running ZFS didn't fit any of the use cases I have for storage in my personal life and actually was problematic (in the sense that if my loved ones needed to access my data in an emergency, no one would know what to do with a multi-disk ZFS dataset).  Furthermore, I found the egress charges from AWS S3 to be not worth it ( ~ $100 worth of egress charges vs a comparable amount to just buy an external hard disk and leave it at my mom's house upstate).  I'm leaving this page up for now just to document that I had this set up at one point, but it no longer reflects my contemporary configuration.*

An anacron script runs on [Maxwell](Maxwell) once a month (i.e., it lives in */etc/cron.monthly*). It runs a series of commands based off the [StackOverflow](StackOverflow) post [here](https://stackoverflow.com/questions/45786142/storing-locally-encrypted-incremental-zfs-snapshots-in-amazon-glacier) to generate encrypted, compressed snapshots that live in an AWS bucket in US-East 2 (Ohio). The script only does incremental backups, and keeps track off the last incremental snapshot that was made using a text file. It also generates a script that allows me to make a manual backup to an external hard disk within my apartment. This is in case I accidentally tank my ZFS pool and need to restore from scratch, but don't want to have to wait 3-5 hours for Glacier to retrieve files.

The commands used (taken from the [StackOverflow](StackOverflow) post above) are as follows:

Sending a full backup:

    zfs send -R <pool name>@<snapshot name> | gzip | gpg --no-use-agent  --no-tty --passphrase-file ./passphrase -c - | aws s3 cp - s3://<bucketname>/<filename>.zfs.gz.gpg

Sending an incremental backup:

    zfs send -R -I <pool name>@<snapshot to do incremental backup from> <pool name>@<snapshot name> | gzip | gpg --no-use-agent  --no-tty --passphrase-file ./passphrase -c - | aws s3 cp - s3://<bucketname>/<filename>.zfs.gz.gpg

Restoring a backup:

    aws s3 cp s3://<bucketname>/<filename>.zfs.gz.gpg - | gpg --no-use-agent --passphrase-file ./passphrase -d - | gunzip | sudo zfs receive <new dataset name>

The specific variant of the restore command that I use looks something like this:

    aws s3 cp s3://jpellman-maxwell-backup-us-east-2/full-test.gz.gpg - | gpg --passphrase-file /root/.backup_pass --no-tty --batch -d - | gunzip | zfs receive pool0/test2

The initial encrypted, compressed snapshot (full backup) was created manually.

The aws cli copy command includes the following flag to account for very large snapshots:

    --expected-size (string) This argument specifies the expected size of a stream in terms of bytes. Note that this argument is needed only when a stream is being uploaded to s3 and the size is larger than 50GB. Failure to include this argument under these conditions may result in a failed upload due to too many parts in upload.

The string that's fed into this param is ESTIMATED\_UPLOAD from the following:

    LASTSNAP_SIZE=$(zfs list -t snapshot -o name,refer -Hp | grep ${POOL} | grep ${LASTSNAP} | awk '{print $2}' | paste -sd+ - | bc)
    CURSNAP_SIZE=$(zfs list -t snapshot -o name,refer -Hp | grep ${POOL} | grep ${CURSNAP} | awk '{print $2}' | paste -sd+ - | bc)
    ESTIMATED_UPLOAD=$(( ${CURSNAP_SIZE} - ${LASTSNAP_SIZE} ))

