FROM alpine:3
RUN apk add --no-cache git git-lfs

VOLUME [ "/data" ]
ENTRYPOINT [ "/examples_script.sh" ]

COPY examples_script.sh /
