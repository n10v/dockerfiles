#inherit from the base container, which have all the needed script to launch tasks
FROM  ingi/inginious-c-base
LABEL org.inginious.grading.name="lisp"

RUN set -x && \
      yum -y install sbcl && \
      yum clean all
