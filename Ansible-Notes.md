# Ansible Notes

Various thoughts/meditations on Ansible and Ansible playbooks.

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