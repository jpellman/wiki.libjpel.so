Mistakes in IT
==============



Generating Unexpected Behavior When Invoking a Shell Command
------------------------------------------------------------

-   Typically a symptom of not reading the manual for a shell command first to totally grasp the flags and options.
-   A great many mistakes of this variety (and of other classes) are issues of communication. You cannot embrace knowledge/information if you do not first encode it. This occurs in other contexts as well (such as not reading e-mails carefully enough).
-   This can also be a symptom of inadequate testing.
    -   If possible, do a dry run of a command beforehand (i.e., rsync's '-n' flag) or use 'echo' before a script to make sure that the variable has the correct values.
    -   Also test results afterwards- make a checklist of what you expect an output to contain and what it should not contain.
-   General advice: Avoid using cd with relative paths in scripts (i.e., be wary of 'cd ..'). If a glitch occurs in anything before the 'cd' command, or a previous cd command before the relative path behaves peculiarly, you may end up in an unexpected directory.
-   Inadequate planning before putting together a script.
-   Inadequate logging for a script or command (e.g., should have a text file with status of various steps piped to it; send time for file sync).
-   Lack of consideration for how script may operate across environments (i.e., different versions of Linux, etc).
-   You cannot change ownership of a file or directory from a normal user to root easily (unless you are root). If you are changing ownership to root (or any other user) as a normal user, it [will not work](https://superuser.com/questions/697608/chown-operation-not-permitted).

Simple Pragmatics
-----------------

-   Don't do uploads over Wifi when Ethernet is possible. Don't use Ethernet when Infiniband makes sense.
-   Make sure that cords aren't plugged in in a way that is so mangled that unplugging one cord could accidentally power off another device.

User Communication
------------------

-   In some instances a user can be educated. Other times, it is better to apply a solution without educating the user, and then trying to educate the user later. Example: A user is agitated and under a lot of stress and needs the solution immediately.
-   Inadequate communication with users (getting user needs) before beginning a purchase process.
-   Performing a reboot without consulting users.

Documentation
-------------

-   Be mindful of the potential need to document changes in directory structure on a file system (redirecting the output of 'tree' or 'ls -R' to a text file might be a good idea here).

Migrations/Upgrades
-------------------

-   Inadequate documentation of licenses before a migration to new systems.
-   Inadequate planning before a migration. Not checking if and how licenses can be migrated between systems.
-   Upgrading a system without a checklist.
-   Upgrading a system without a rollback plan. Not having a time scale for a rollback plan.

Data Transfer / Storage
-----------------------

-   When transferring via Sneakernet (still occurs in rare situations): Not creating a manifest of files to be transferred before transferring them to a physical medium. Without such a manifest, there's no way of keeping track of whether or not all the files that were intended to be transferred actually were.
-   Don't assume that because a bay can be taken out of a server, it is plug'n'play. You **will** be burned on this if you do not bear this in mind. Server hard drives are not to be treated like USB hard drives you may use with a desktop.
-   *dd if=[block level device or image] bs=[block size A] | pv | dd of=[block level device or image] bs=[block size B] conv=sync* is a great way to corrupt an image. It's always a good idea to a) make sure you understand what a flag is doing (*conv=sync*) rather than trusting the documentation it came from blindly and b) make sure that the block size is the same on either side of a pipe using multiple dds.

