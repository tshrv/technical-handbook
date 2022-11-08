# Build docker image
1. Provide path to context, here `.`
2. Tag with a name and tag, here `test-app:0.1.0`
```
docker build -t test-app:0.1.0 .
```

# Push an image
1. Image created using the build command.
2. Tag the image with new repo and tagname.
3. Push the image
```
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname
```

# Pull
```
docker pull tshrv/dummy-app:0.1.0
```

# Run

```
docker run [repo/]image[:tag]

example -
docker run postgres
=> postgres:latest
=> will fetch from hub(indexed repositories) if not found locally
=> add ACR/Dockerhub/more as indexed repositories.

docker run tshrv/dummy-app:0.1.0
=> if image tshrv/dummy-app with tag 0.1.0 exists locally, runs
=> else tries to lookup and pull from repositories
```

Mount a local directory while running -
```
docker run -v $(pwd)/data:/data tshrv/dummy-app:0.1.0
```

Exposing ports -
```
docker run -v $(pwd)/data:/data -p 80:80 -p 200:200 tshrv/dummy-app:0.1.0
```