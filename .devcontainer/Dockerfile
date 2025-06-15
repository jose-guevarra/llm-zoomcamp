FROM public.ecr.aws/amazonlinux/amazonlinux:latest


# Set PYVER as the default Python interpreter
# Define the version of Python to install
# For example "3.11" will get the latest version of 3.11 (ex 3.11.4, 3.11.5, etc)
ARG PYVER="3.11"
RUN dnf update && dnf install -y python3-pip python$PYVER python$PYVER-pip && dnf clean all

RUN pip$PYVER install pipenv
RUN update-alternatives --install /usr/bin/python3 python /usr/bin/python$PYVER 1
RUN update-alternatives --set python /usr/bin/python$PYVER
RUN update-alternatives --set python /usr/bin/python$PYVER

# Add path to pipenv
ENV PIPENV_VENV_IN_PROJECT=1
ENV PIPENV_VERBOSITY=-1

# These settings prevent a timezone prompt when Python installs
# Use this article to find your time zone (TZ):
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
ENV TZ=America/Los_Angeles \
    DEBIAN_FRONTEND=noninteractive


RUN dnf update -y && dnf install -y sudo vim git unzip make wget \
    glibc-langpack-en


# User setup
ARG REMOTE_USER=dockeruser

RUN /usr/sbin/groupadd -r sudo \
    && /usr/sbin/useradd -rm -d /workspaces -s /bin/bash -g sudo -u 1001 $REMOTE_USER \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER $REMOTE_USER