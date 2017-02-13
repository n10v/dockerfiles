FROM  ingi/inginious-c-base
LABEL org.inginious.grading.name="clojure"

RUN set -x && \
      yum -y install java-1.7.0-openjdk && \
      zipfile="clojure-1.8.0.zip" && \
      curl -fSLO "https://repo1.maven.org/maven2/org/clojure/clojure/1.8.0/${zipfile}" && \
      unzip -q $zipfile && \
      rm $zipfile && \
      mv clojure-1.8.0/clojure-1.8.0.jar /opt/clojure.jar && \
      chmod 644 /opt/clojure.jar && \
      rm -rf clojure-1.8.0/

ADD clojure /bin/clojure
RUN chmod +x /bin/clojure
