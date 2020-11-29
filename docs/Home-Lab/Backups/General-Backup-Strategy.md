This is a brief summary for how I envision backups will work with my home infrastructure.  My primary goal with my backup strategy is to minimize the fallout from a natural disaster or burglary, and ensure that I won't be totally screwed if my house burns down or I'm mugged.  While neither of these scenarios are super common, living in a large city with a large population of people makes the improbable inevitable...

My backup strategy consists of the following for my computer:

 * Generating one encrypted, compressed full ZFS snapshot and sending it to AWS once a year and tiering it to Deep Glacier after 2 days ([AWS-Backup](Home-Lab/Backups/AWS-Backup).
 * Sending encrypted, compressed incremental ZFS snapshots to AWS once every month ([AWS-Backup](Home-Lab/Backups/AWS-Backup).
 * Retaining 2 years worth of encrypted, compressed snapshots in AWS ([AWS-Backup](Home-Lab/Backups/AWS-Backup).
 * Making full backups of my disk to blu ray once every 2-4 years and storing these backups offsite ([Blu-Ray-Backup](Home-Lab/Backups/Blu-Ray-Backup). 
 * Scanning paper documents using my document scanner and saving them to _/datastore/documents_ on [Maxwell](Home-Lab/Hosts/Maxwell) (which also holds regular Excel/Word/CSV documents).
 * Syncing _/datastore/documents_ (essential documents from the apartment / my life in general) up to Google Drive (it was necessary to purchase 100GB on Google One for this, although the documents themselves are quite small).

For my smartphone:

 * Syncing all photos to Google Drive, where they are then copied down to [Maxwell](Home-Lab/Hosts/Maxwell) using [rclone](https://rclone.org/) or similar at some regular interval.  I may delete these manually sporadically, just to ensure that they're on hand (basically just treating Drive how I treat my current phone's storage)
 * Syncing all my audio diaries to Google Drive, where they are similarly sync'd down to Maxwell, but then deleted afterwards from Drive (no reason for them to linger there).
 * Syncing all my texts to GMail using IMAP with [SMS Backup+](https://github.com/jberkel/sms-backup-plus) (IMAP is necessary because Google broke its API)

For my online data:

 * Syncing all my tweets to [Maxwell](Home-Lab/Hosts/Maxwell) using [t](https://github.com/sferik/t) and some scripts.
 * Syncing my email to [Maxwell](Home-Lab/Hosts/Maxwell) using [gmvault](http://gmvault.org/) (with a workaround because, again, Google broke their own functionality)
