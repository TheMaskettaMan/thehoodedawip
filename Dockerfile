# Use an official Python runtime as a parent image
FROM centos:7
# Determine parent-image

VOLUME ["/dev_masketta_clan/"]
#VOLUME ["/prod_masketta_clan"]

VOLUME ["/dev_masketta_clan_static"]
#VOLUME ["/prod_masketta_clan_static"]



ENV masketta_env dev
#ENV masketta_env prod

WORKDIR /dev_masketta_clan

#run necessary adds for RUN commands

# Personal instructions for dev env
#todo add separate requirements txt
#for apt-get requires

RUN yum install -y git
RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install -y nodejs
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u
RUN yum install -y python36u-pip

# TODO  add these to a requirementstxt
RUN pip3.6 install flask
RUN pip3.6 install redis

# Install any needed packages specified in requirements.txt
#RUN pip3.6 install --trusted-host pypi.python.org -r requirements.txt

COPY ./dev_bash_config/* /root/
COPY ./requirements.txt .
COPY ./initial_readme.txt .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Dev_Masketta_Clan

RUN cat ./initial_readme.txt

CMD ["bash"]


