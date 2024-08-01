# Docker

- Docker: process level virtualization, VM: OS level virtualization
- Automates the deployment of applications inside software containers
- Does not have strict sharing of resources like VMs
- Environment synchronization becomes easier for dev teams
- Reduced setup/deployment time
- Docker containers allow you to commit changes to your Docker images and version control them. For example, if you perform a component upgrade that breaks your whole environment, it is very easy to rollback to a previous version of your Docker image.
- Docker ensures your applications and resources are isolated and segregated.

## Format of dockerfile

```docker
# Comment
INSTRUCTION arguments
```

## Commands

1. `FROM image_name:tag` - Defines the base image to be used
2. `WORKDIR path`
3. `ARG key` - Arguments provided and scoped only to the build process.
4. `COPY source destination` - Copy contents from source to destination
5. `RUN command` - The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile.
6. `ENTRYPOINT`
7. `CMD`

Environment variables are supported by the following list of instructions in the Dockerfile:

- ADD
- COPY
- ENV
- EXPOSE
- FROM
- LABEL
- STOPSIGNAL
- USER
- VOLUME
- WORKDIR
- ONBUILD (when combined with one of the supported instructions above)

.dockerfile - exclude files

### `ENTRYPOINT` and `CMD`

If `CMD` is used to provide **default arguments** for the `ENTRYPOINT` instruction, both the `CMD` and `ENTRYPOINT` instructions should be specified with the `JSON` array format.

```docker
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver]
```

### `ARG` and `ENV`

# More topics

- Swarm
- Compose
- Swarm vs Compose
- Persistent storage
- Networking
- Images
- Containers
- Secrets
- Multi stage builds
- Monitoring
- Healthchecks
- Plugins
- Build caching
- Docket Content Trust
- Container performance optimization
