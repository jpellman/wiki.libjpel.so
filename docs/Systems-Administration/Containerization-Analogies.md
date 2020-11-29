

A collection of analogies for how Docker / containerization fits into the broader tech stack. Part of understanding these analogies is knowing that an operating system, at the end of the day, is really a program itself (albeit one that mediates access to the underlying hardware for other programs).

Docker/Kata/CRI-O Container : Python Virtual Environment, where a container is an environment for operating system libraries and other components written in C. Essentially, a container is a virtual environment for C code / lower-level code.

A Docker Image / Golden image : Application binary

Dockerfile / Ansible / Config management : Application source code

Packer / Buildah / [Image Builder](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/composing_a_customized_rhel_system_image/composer-description_composing-a-customized-rhel-system-image): Make

Dockerhub / container image registry : Yum repository

