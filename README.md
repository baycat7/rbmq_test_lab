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

_____rabbit.yml_____

- name: rubbit setup
  hosts: your_host
  become: true

  roles:
    - name: rabbitmq_setup

License
-------

BSD
