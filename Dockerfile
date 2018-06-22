# Use an official Python runtime as a parent image
FROM centos
# Determine parent-image

VOLUME ["/dev_masketta_clan/"]

WORKDIR /dev_masketta_clan

#run necessary adds for RUN commands
ADD ./dev_bash_config/* /root/
ADD ./requirements.txt .

# Personal instructions for dev env
#todo add separate requirements txt
#for apt-get requires

RUN yum install -y git
RUN curl --silent --location https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install -y nodejs
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum install -y python36u
RUN yum install -y python-pip

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Masketta_Clan_Dev

RUN cat ./initial_readme.txt

CMD ["bash"]


