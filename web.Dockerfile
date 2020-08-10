FROM nginx:latest

COPY ./backend/new.conf /etc/nginx/conf.d/default.conf

CMD nginx -g "daemon off; error_log /dev/stdout info;"
