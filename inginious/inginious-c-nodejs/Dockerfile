#inherit from the base container, which have all the needed script to launch tasks
FROM  ingi/inginious-c-base
LABEL org.inginious.grading.name="nodejs"

RUN set -x && \
      curl --silent --location https://rpm.nodesource.com/setup_7.x | bash - && \
      yum -y install nodejs && \
      yum clean all
