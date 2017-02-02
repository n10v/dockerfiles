FROM	bogem/inginious-c-ubuntu-base
LABEL	org.inginious.grading.name="processing"

ENV PROCESSING_VERSION 3.2.4

RUN set -x && \
		apt-get update && apt-get install -y curl --no-install-recommends && \
		apt-get install -y xvfb libxrender1 libxtst6 libxi6 default-jre && \
		tarball="processing-${PROCESSING_VERSION}-linux64.tgz" && \
		curl -fSL "http://download.processing.org/${tarball}" -O && \
		apt-get purge -y --auto-remove curl && \
		tar -xzf "$tarball" && \
		mv "processing-${PROCESSING_VERSION}" /opt/processing && \
		rm "$tarball" && \
		ln -s /opt/processing/processing /usr/bin/processing && \
		ln -s /opt/processing/processing-java /usr/bin/processing-java && \
		apt-get clean

COPY create_display.bash /usr/sbin/
RUN chmod +x /usr/sbin/create_display.bash
ENV DISPLAY :1

ENTRYPOINT ["/usr/sbin/create_display.bash"]
