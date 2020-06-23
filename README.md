
# NSLS2 Intallation Instructions

Notes:
* Need to periodically run ssh-add
* May need to update sudoers file to set requiretty to false
* May need to use zookeeper-server-stop/start to start zookeepers in the correct order
* May need to update the ansible version to fix errors.
* May need to run playbook multiple times.
* I had to run `sudo apt-get update --fix-missing` on one of the machines.
* I had to update the java version

Procedure:
* `git clone https://github.com/NSLS-II/cp-ansible`
* Checkout the desired branch
* Make sure that you can connect to all nodes: `ansible -i hosts.yml all -m ping -k -K`
* Open the required ports on each of the Kafka nodes: 2181, 2888, 3888, 9092, 9091 are needed for the broker_zookeeper playbook
* Install Kafka brokers, and zookeeper: `ansible-playbook -i hosts.yml broker_zookeeper.yml -k -K -vvv`

Test the installation:
* `git clone https://github.com/bluesky/bluesky-kafka`
* `cd bluesky-kafka/bluesky_kafka/tests`
* 'pytest --kafka-bootstrap-servers "cmb01:9092, cmb02:9092, cmb03:9092"`

Create the default topics:
* `python cp-ansible/create_bluesky_topics.py`


# CP-Ansible

## Introduction

Ansible provides a simple way to deploy, manage, and configure the Confluent Platform services. This repository provides playbooks and templates to easily spin up a Confluent Platform installation. Specifically this repository:

* Installs Confluent Platform packages.
* Starts services using systemd scripts.
* Provides configuration options for plaintext, SSL, SASL_SSL, and Kerberos.

The services that can be installed from this repository are:

* ZooKeeper
* Kafka
* Schema Registry
* REST Proxy
* Confluent Control Center
* Kafka Connect (distributed mode)
* KSQL Server

## Documentation

You can find the documentation for running CP-Ansible at https://docs.confluent.io/current/tutorials/cp-ansible/docs/index.html.

## Contributing


If you would like to contribute to the CP-Ansible project, please refer to the [CONTRIBUTE.md](https://github.com/confluentinc/cp-ansible/blob/5.4.x/CONTRIBUTING.md)


## License

[Apache 2.0](https://github.com/confluentinc/cp-ansible/blob/5.4.x/LICENSE.md)
