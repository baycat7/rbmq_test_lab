Role Name
=========
test install lab

Requirements
------------

For Debian 12 only

Dependencies
------------

Editional neded pkg. ufw, python3-pika

For run script need change  /rabbitmq_setup/tasks/main.yml parameter to configure_priv: '.*' 

Example Playbook
----------------

ansible-playbook rabbit.yml -e @/etc/ansible/roles/rabbitmq_setup/vars/sec.yml --ask-vault-pass

rabbit.yml content
----------------
```
---
- name: rabbit setup
  hosts: your_target_host_ip_or_fqdn
  become: true

  roles:
    - name: rbmq_test_lab 

```
License
-------

BSD
