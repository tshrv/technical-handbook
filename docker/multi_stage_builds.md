# Multi Stage Builds

With multi-stage builds, you use multiple `FROM` statements in your `Dockerfile`. Each `FROM` instruction can use a different base, and each of them begins a new stage of the build. You can **selectively copy artifacts** from one stage to another, leaving behind everything you don’t want in the final image. To show how this works, let’s adapt the `Dockerfile` from the previous section to use multi-stage builds.

```dockerfile
# syntax=docker/dockerfile:1

FROM golang:1.16
WORKDIR /go/src/github.com/alexellis/href-counter/
RUN go get -d -v golang.org/x/net/html  
COPY app.go ./
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o app .

FROM alpine:latest  
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=0 /go/src/github.com/alexellis/href-counter/app ./
CMD ["./app"]
```

You only need the single `Dockerfile`. You don’t need a separate build script, either. Just run `docker build`.
```
 docker build -t alexellis2/href-counter:latest .
```

The end result is the same tiny production image as before, with a significant reduction in complexity. You don’t need to create any intermediate images, and you don’t need to extract any artifacts to your local system at all.

How does it work? The second `FROM` instruction starts a new build stage with the `alpine:latest` image as its base. The `COPY --from=0` line copies just the built artifact from the previous stage into this new stage. The Go SDK and any intermediate artifacts are left behind, and not saved in the final image.