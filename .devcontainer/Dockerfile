FROM public.ecr.aws/amazonlinux/amazonlinux:latest

# Add path to pipenv
ENV PIPENV_VENV_IN_PROJECT=1
ENV PIPENV_VERBOSITY=-1

RUN dnf update -y \
    && dnf install -y sudo vim unzip tar git make wget glibc-langpack-en procps

RUN dnf install -y python3-pip git python3.11 python3.11-pip

RUN pip3.11 install pipenv


# create remote user to wheel group, then allow passwordless sudo for wheel group
ENV REMOTE_USER="apprunner"
RUN /usr/sbin/adduser -rm -d /workspaces -s /bin/bash -g wheel -u 1001 $REMOTE_USER \
    && echo '%wheel ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER $REMOTE_USER
