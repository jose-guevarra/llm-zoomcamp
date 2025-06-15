FROM public.ecr.aws/amazonlinux/amazonlinux:latest

# Define the version of Python to install
# For example "3.11" will get the latest version of 3.11 (ex 3.11.4, 3.11.5, etc)
ARG PYVER="3.11"

# Add path to pipenv
ENV PIPENV_VENV_IN_PROJECT=1
ENV PIPENV_VERBOSITY=-1

# These settings prevent a timezone prompt when Python installs
# Use this article to find your time zone (TZ):
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
ENV TZ=America/Los_Angeles \
DEBIAN_FRONTEND=noninteractive


RUN dnf update -y && yum install -y sudo vim git unzip make wget procps \
    python3-pip python3.11 python3.11-pip glibc-langpack-en


RUN pip3.11 install pipenv

RUN dnf update && dnf install -y sudo vim git unzip make wget python3-pip python$PYVER python$PYVER-pip && dnf clean all

# Set PYVER as the default Python interpreter
RUN pip$PYVER install pipenv
RUN update-alternatives --install /usr/bin/python3 python /usr/bin/python$PYVER 1
RUN update-alternatives --set python /usr/bin/python$PYVER
RUN update-alternatives --set python /usr/bin/python$PYVER


# User setup
ARG REMOTE_USER=dockeruser

RUN /usr/sbin/groupadd -r sudo \
&& /usr/sbin/useradd -rm -d /workspaces -s /bin/bash -g sudo -u 1001 $REMOTE_USER \
&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
