FROM public.ecr.aws/amazonlinux/amazonlinux:latest


# Python Install
# Define the version of Python to install
# For example "3.11" will get the latest version of 3.11 (ex 3.11.4, 3.11.5, etc)
ARG PYVER="3.11"

RUN dnf install -y python3-pip python$PYVER python$PYVER-pip glibc-langpack-en && dnf clean all

# Set PYVER as the default Python interpreter
RUN pip$PYVER install pipenv
RUN update-alternatives --install /usr/bin/python3 python /usr/bin/python$PYVER 1
RUN update-alternatives --set python /usr/bin/python$PYVER
RUN update-alternatives --set python /usr/bin/python$PYVER

# Use venv dir local to Pipfile
ENV PIPENV_VENV_IN_PROJECT=1
ENV PIPENV_VERBOSITY=-1


# Install devel packages
RUN dnf update -y && yum install -y sudo vim git unzip make wget


# User setup
ARG REMOTE_USER=dockeruser

RUN /usr/sbin/groupadd -r sudo \
    && /usr/sbin/useradd -rm -d /workspaces -s /bin/bash -g sudo -u 1001 $REMOTE_USER \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER $REMOTE_USER
