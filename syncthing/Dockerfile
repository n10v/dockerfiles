FROM ubuntu:latest

RUN useradd syncthing

ENV SYNCTHING_VERSION 0.14.21

RUN set -x && \
	apt-get update && apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/* && \
	tarball="syncthing-linux-amd64-v${SYNCTHING_VERSION}.tar.gz" && \
	curl -fSL "https://github.com/syncthing/syncthing/releases/download/v${SYNCTHING_VERSION}/$tarball" -O && \
	apt-get purge -y --auto-remove curl && \
	tar -xvf "$tarball" --strip-components=1 "$(basename "$tarball" .tar.gz)"/syncthing && \
	mv syncthing /usr/local/bin/syncthing && \
	rm "$tarball" && \
	apt-get clear && \

VOLUME /config

EXPOSE 8384 22000 21025/udp

USER syncthing

CMD ["syncthing", "-no-browser", "-no-restart", "-gui-address=0.0.0.0:8384", "-home=/config"]
