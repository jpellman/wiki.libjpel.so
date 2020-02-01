#format rst

Web Browsers Must Die
=====================

I'm getting sick of the fact that web browsers seem to be usurping the functionality of a proper operating system, and that every Web 2.0 website seems to be some `unholy bloated piece of shit`_.  I grew up on Web 1.0 in the 90s- I thrived in that environment.  There was no clutter, no bullshit, no embedded bitcoin miners or ransomware payloads hidden in embedded ads.  Just raw information, following `Grice's maxims`_ like a champ.

Furthermore, call me old school (and I'm generally speaking a young-ish dude), but I'm annoyed by the tendency to shoehorn everything onto HTTP.  Wasn't the point of having application layer protocols exist in the first place to tailor calls over the internet to specific application domains?  This gripe isn't really based in anything technical (HTTP is actually probably better than most application-layer protocols that could be devised independently for many applications), but my gut instinct is that in many cases, HTTP is an unnecessary middle man when an API is built on top of it (disclaimer: I might be wrong here).  Dammit get off my lawn!

I want to go back to simpler days, and so I'm trying to figure out what tools and utilities I can use to get me back to the olden times.  I got in to this mode of thinking once a long time ago (circa 2013) but I sem to have circled back again.  Here are some ideas:

* `Wiki CLI`_ because I want to feel like WAIS_ is a thing outside of LibraryComputing_.

* RTV_ because I want to feel like the USENET still exists.

* Newsboat_ because when I want to read news, I want to read *text* and not see some shitty auto-play video that tanks all of my cell phone data (fuck you NY Times).

* cmdg_ for Gmail (since I think that Gmail labels have value over vanilla, standard e-mail).  Maybe aerc_ would work too.

  * mutt apparently has some support for Gmail labels: here_ and `here <https://developers.google.com/gmail/imap/imap-extensions#access_to_gmail_labels_x-gm-labels>`__

  * Other concerns about mutt w/ gmail: `here <https://spin.atomicobject.com/2014/02/11/connect-mutt-gmail/>`__ 

* `MPS Youtube`_ to replace YouTube_.  I'm sick of being distracted by recommended videos trying to convince me of some nonsense or that contain some BuzzFeed_-style listicle in video form.

* Finch_ for online chat.

* screen to give me the experience of cycling through a bunch of different tabs.

* For everything else, `brow.sh`_ or Lynx.

* An Ansible playbook to set all this up.

* A lightweight VM I can run on Bruno_ with all of this installed.  OS X will need to stay because I like video games.

.. ############################################################################

.. _unholy bloated piece of shit: https://www.webbloatscore.com/

.. _Grice's maxims: https://www.sas.upenn.edu/~haroldfs/dravling/grice.html

.. _Wiki CLI: https://github.com/walle/wiki

.. _WAIS: https://en.wikipedia.org/wiki/Wide_area_information_server

.. _LibraryComputing: ../LibraryComputing

.. _RTV: https://github.com/michael-lazar/rtv

.. _Newsboat: https://github.com/newsboat/newsboat

.. _cmdg: https://github.com/ThomasHabets/cmdg

.. _aerc: https://aerc-mail.org/

.. _here: https://stackoverflow.com/questions/23721726/how-to-display-gmail-labels-in-mutt

.. _MPS Youtube: https://github.com/mps-youtube/mps-youtube

.. _YouTube: ../YouTube

.. _BuzzFeed: ../BuzzFeed

.. _Finch: https://developer.pidgin.im/wiki/Using%20Finch

.. _brow.sh: https://www.brow.sh/

.. _Bruno: ../Bruno

