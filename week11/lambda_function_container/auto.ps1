<#
.SYNOPSIS
Builds a Docker image for the specified platform.

.DESCRIPTION
This script builds a Docker image for the specified platform using the specified tag.

.NOTES
File Name      : build-docker-image.ps1
Author         : Your Name
Prerequisite   : Docker must be installed on the system.

#>

# Build the Docker image for the specified platform
docker build -t docker-image:test .
