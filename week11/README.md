### Docker Image Command


```shell
docker image ls # Alias docker image list, docker images

# Options:
# -a, --all		Show all images (default hides intermediate images)
# -q, --quiet		Only show image IDs
```

```shell
docker image pull # Alias docker pull

# Usage	docker image pull [OPTIONS] NAME[:TAG|@DIGEST]
# Options:
# -a, --all-tags		Download all tagged images in the repository
# -q, --quiet		    Suppress verbose output

# By default docker pull pulls images from Docker Hub

# The following command pulls the testing/test-image image 
# from a local registry listening on port 5000 (myregistry.local:5000):
# docker image pull myregistry.local:5000/testing/test-image
```

```shell
docker image push  # Alias docker push

# Usage	docker image pull [OPTIONS] NAME[:TAG|@DIGEST]
# Options:
# -a, --all-tags		Push all tags of an image to the repository
# -q, --quiet		    Suppress verbose output

# By default docker pushes  images to Docker Hub

# The following command push the myadmin/rhel-httpd:latest image 
# to registry of registry-host listening on port 5000
# docker image push registry-host:5000/myadmin/rhel-httpd:latest
```


```shell
docker image tag  # docker tag

# Description
# A full image name has the following format and components:
#
# [HOST[:PORT_NUMBER]/]PATH
#
# HOST: The optional registry hostname specifies where the image is located. 
#       The command uses Docker's public registry at registry-1.docker.io by default.
#       
# PORT_NUMBER: If a hostname is present, it may optionally be followed 
#              by a registry port number in the format :8080.
# 
# PATH: The path consists of slash-separated components. 
# 
# [NAMESPACE/]REPOSITORY:  When the namespace is not present, Docker uses library as the default namespace.
# After the image name, the optional TAG is a custom, human-readable manifest identifier that's typically 
# a specific version or variant of an image. 
#
#

# To tag a local image httpd as fedora/httpd with the tag version1.0:
docker tag httpd fedora/httpd:version1.0

# To push an image to a private registry and not the public 
# Docker registry you must include the registry hostname and port (if needed).
docker tag 0e5574283393 myregistryhost:5000/fedora/httpd:version1.0
```



### Docker Container Command


```shell
docker container ls 
# Alias docker container list, docker container ps, docker ps

# Options:
# -a, --all		Show all containers (default shows just running)
# -q, --quiet	Only display container IDs
```
