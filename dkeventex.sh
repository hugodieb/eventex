docker stop eventex
docker rm eventex
docker run -d --restart=unless-stopped \
	   --name=eventex \
	   -v /home/hugo/wttd/dkdata/eventex/uwsgi:/uwsgi \
	   eventex start.sh
