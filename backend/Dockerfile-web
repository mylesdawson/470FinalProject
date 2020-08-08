FROM nginx:latest

COPY ./new.conf /etc/nginx/conf.d/default.conf

CMD nginx -g "daemon off; error_log /dev/stdout info;"
