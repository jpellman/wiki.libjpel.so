\#format rst

Notes on Backups of Maxwell's ZFS Pool to AWS
=============================================

An anacron script runs on [Maxwell](../Maxwell) once a month (i.e., it lives in */etc/cron.monthly*). It runs a series of commands based off the [StackOverflow](../StackOverflow) post [here](https://stackoverflow.com/questions/45786142/storing-locally-encrypted-incremental-zfs-snapshots-in-amazon-glacier) to generate encrypted, compressed snapshots that live in an AWS bucket in US-East 2 (Ohio). The script only does incremental backups, and keeps track off the last incremental snapshot that was made using a text file. It also generates a script that allows me to make a manual backup to an external hard disk within my apartment. This is in case I accidentally tank my ZFS pool and need to restore from scratch, but don't want to have to wait 3-5 hours for Glacier to retrieve files.

The commands used (taken from the [StackOverflow](../StackOverflow) post above) are as follows:

Sending a full backup:

    zfs send -R <pool name>@<snapshot name> | gzip | gpg --no-use-agent  --no-tty --passphrase-file ./passphrase -c - | aws s3 cp - s3://<bucketname>/<filename>.zfs.gz.gpg

Sending an incremental backup:

    zfs send -R -I <pool name>@<snapshot to do incremental backup from> <pool name>@<snapshot name> | gzip | gpg --no-use-agent  --no-tty --passphrase-file ./passphrase -c - | aws s3 cp - s3://<bucketname>/<filename>.zfs.gz.gpg

Restoring a backup:

    aws s3 cp s3://<bucketname>/<filename>.zfs.gz.gpg - | gpg --no-use-agent --passphrase-file ./passphrase -d - | gunzip | sudo zfs receive <new dataset name>

The initial encrypted, compressed snapshot (full backup) was created manually.

The aws cli copy command includes the following flag to account for very large snapshots:

    --expected-size (string) This argument specifies the expected size of a stream in terms of bytes. Note that this argument is needed only when a stream is being uploaded to s3 and the size is larger than 50GB. Failure to include this argument under these conditions may result in a failed upload due to too many parts in upload.

The string that's fed into this param is ESTIMATED\_UPLOAD from the following:

    LASTSNAP_SIZE=$(zfs list -t snapshot -o name,refer -Hp | grep ${POOL} | grep ${LASTSNAP} | awk '{print $2}' | paste -sd+ - | bc)
    CURSNAP_SIZE=$(zfs list -t snapshot -o name,refer -Hp | grep ${POOL} | grep ${CURSNAP} | awk '{print $2}' | paste -sd+ - | bc)
    ESTIMATED_UPLOAD=$(( ${CURSNAP_SIZE} - ${LASTSNAP_SIZE} ))

* * * * *

> [HomeLab](../HomeLab)
