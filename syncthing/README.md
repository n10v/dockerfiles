Mix of tianon/syncthing and gbrks/syncthing

# Usage
	$ useradd syncthing
	$ chown -R syncthing /opt/appdata/syncthing
	$ chown -R syncthing <host sync folder>
	$ docker run -d --name=syncthing \
	--restart=on-failure:20 \
	-v /opt/appdata/syncthing:/config \
	-v /<host sync folder>:<sync folder> \
	-p 8384:8384/tcp \
	-p 22000:22000/tcp \
	-p 21025:21025/udp \
	bogem/syncthing
