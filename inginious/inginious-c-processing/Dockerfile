FROM  ingi/inginious-c-base
LABEL org.inginious.grading.name="processing"

ENV PROCESSING_VERSION 3.2.4

RUN set -x && \
      yum -y install xorg-x11-server-Xvfb libXrender.x86_64 java-1.7.0-openjdk.x86_64 && \
      tarball="processing-${PROCESSING_VERSION}-linux64.tgz" && \
      curl -fSL "http://download.processing.org/${tarball}" -O && \
      tar -xzf "$tarball" && \
      mv "processing-${PROCESSING_VERSION}" /opt/processing && \
      rm "$tarball" && \
      ln -s /opt/processing/processing /usr/bin/processing && \
      ln -s /opt/processing/processing-java /usr/bin/processing-java && \
      yum clean all

COPY create_display.bash /usr/sbin/
RUN  chmod +x /usr/sbin/create_display.bash
ENV  DISPLAY :1

ENTRYPOINT ["/usr/sbin/create_display.bash"]
