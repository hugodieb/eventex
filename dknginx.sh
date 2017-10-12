docker stop nginx
docker rm nginx
docker run -d --restart=unless-stopped \
	   --name=nginx -p 80:80 \
	   -v /home/hugo/wttd/dkdata/nginx/conf.d:/etc/nginx/conf.d \
	   -v /home/hugo/wttd/dkdata/eventex/uwsgi:/uwsgi_eventex \
	   nginx
