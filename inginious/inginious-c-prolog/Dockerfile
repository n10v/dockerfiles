FROM  ingi/inginious-c-base
LABEL org.inginious.grading.name="prolog"

RUN set -x && \
      yum install -y \
        autoconf \
        chrpath \
        libunwind \
        freetype-devel \
        gmp-devel \
        java-1.8.0-openjdk-devel \
        jpackage-utils \
        libICE-devel \
        libjpeg-turbo-devel \
        libSM-devel \
        libX11-devel \
        libXaw-devel \
        libXext-devel \
        libXft-devel \
        libXinerama-devel \
        libXmu-devel \
        libXpm-devel \
        libXrender-devel \
        libXt-devel \
        ncurses-devel \
        openssl-devel \
        pkgconfig \
        readline-devel \
        unixODBC-devel \
        zlib-devel \
        uuid-devel \
        libarchive-devel && \
      yum groupinstall -y "Development Tools" && \
      yum install -y rpmdevtools && \
      rpm -ihv --nomd5 https://kojipkgs.fedoraproject.org//packages/pl/7.2.3/3.fc25/src/pl-7.2.3-3.fc25.src.rpm && \
      cd ~/rpmbuild && \
      yum install -y java-1.6.0-openjdk-devel && \
      yum install -y `grep ^BuildRequires SPECS/pl.spec | awk 'NF==2 {print $2}'` && \
      rpmbuild -ba SPECS/pl.spec && \
      yum install -y RPMS/x86_64/pl-*.rpm && \
      yum clean all
