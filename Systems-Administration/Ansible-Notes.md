# Ansible Notes

Various thoughts/meditations on Ansible and Ansible playbooks.

## Data Structure Fidelity

While configuration management tools are often compared to programming languages (e.g., "Infrastructure as Code"), I find that more often the syntax of such tools is more analogous to a database (e.g., similar to ITIL's "CMDB").  Phrased differently, while the distinction between data and program has been murky since the first stored program was introduced in the [Manchester Baby](https://en.wikipedia.org/wiki/Manchester_Baby), I think that Ansible veers more towards data than program (ditto for similar tools like Saltstack, Puppet, and Chef).  What little actual programming there is involved in config management is more geared towards control flow than actual computations.  Basically, in my view, Ansible is a [shim](https://en.wikipedia.org/wiki/Shim_(computing)) that wraps around interfaces used to interact with configuration data using standard CRUD operations.  Namely, Ansible roles contain data that needs to be written to:

 * The Yum, RPM or dpkg databases.
 * Data stored within flat files that live in /etc (such as fstab, passwd, sudoers, etc)
 * Firewall interfaces like firewall-cmd
 * Data/state maintained by systemd.

In general, unless there is a compelling reason to develop an alternative schema for representing data, I think that data in Ansible roles and playbooks should resemble the data structures already used.  This is because the act of re-mapping configuration data to a new schema from the one that the software developer has chosen ignores the developer's reasoning and implies that the information asymmetry between developer and end-user does not exist.  We should accept the existence of asymmetry, and defer to the developers judgement save for exceptional circumstances.

## Conditionals

Running the following repeatedly is the same as having a bunch of if/elif/else statements in a row (from [ansible-guacamole](https://github.com/mrlesmithjr/ansible-guacamole)):

```
- name: Setting a fact.
  set_fact:
    my_great_fact: foobar
when: >
    (ansible_distribution == "Debian") or
    (ansible_distribution == "Ubuntu")

- name: Setting a fact.
  set_fact:
    my_great_fact: fizzbuzz
when: >
    (ansible_distribution == "RedHat")
```

In contrast, this is the Ansible equivalent to a switch/case statement (from [ansible-anaconda](https://github.com/andrewrothstein/ansible-anaconda) by Andrew Rothstein):

```
- name: resolve platform specific vars
  include_vars: "{{ item }}"
  with_first_found:
    - files:
        - '{{ ansible_os_family }}.yml'
        - 'default.yml'
      paths:
        - '{{ role_path }}/vars'
```

Ansible switch/case statements are preferable because fewer conditionals need to be evaluated and case statements are more maintainable / grokkable.  In the case/statement, all that needs to happen is for _ansible_os_family_ to be expanded once, while in the other example _ansible_distribution_ is expanded three times and two _when_ statements need to be evaluated.