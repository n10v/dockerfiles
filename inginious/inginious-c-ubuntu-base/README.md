INGInious
=========

This container is a base container for INGInious built on ubuntu.

Containers based on standard inginious-c-base are not compatible with this base container.

Base container (bogem/inginious-c-ubuntu-base)
--------------------------------------

The base container image.

Contains basic INGInious commands, that are needed in order to grade tasks in INGInious.

All container images written for INGInious should inherit from this container image.

This container is not able to grade anything, as it lacks a name label.
