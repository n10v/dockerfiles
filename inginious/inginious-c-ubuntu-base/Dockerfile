FROM	ubuntu:latest

# Install python, needed for scripts used in INGInious
RUN	set -x && \
		apt-get -y update && \
		apt-get -y install python python3-pip python3 zip unzip tar sed openssh-server openssl iproute file && \
		pip3 install --upgrade pip && \
		pip3 install msgpack-python pyzmq && \
		ln -s /usr/bin/python3 /bin/python3 && \
		apt-get clean

# Allow to run commands
ADD	. /INGInious
RUN	chmod -R 755 /INGInious/bin && \
		chmod 700 /INGInious/bin/INGInious && \
		mv /INGInious/bin/* /bin

# Install everything needed to allow INGInious' python libs to be loaded
RUN	chmod -R 644 /INGInious/inginious && \
		mkdir -p /usr/lib/python3.5/site-packages/inginious && \
		cp -R /INGInious/inginious/*.py  /usr/lib/python3.5/site-packages/inginious && \
		echo "inginious" > /usr/lib/python3.5/site-packages/inginious.pth

# Delete unneeded folders
RUN	rm -R /INGInious

# Create worker user
RUN	groupadd --gid 4242 worker && \
		useradd --uid 4242 --gid 4242 worker --home-dir /task

RUN	sed -i.bak '/^AcceptEnv/ d' /etc/ssh/sshd_config

CMD	["INGInious"]
