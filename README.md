# deploy-webhook

A simple webhook server for docker-compose services.
When a webhook is triggered for a project the following commands will be run in its directory:

```sh
git pull
docker-compose pull
docker-compose build
docker-compose up --detach
```
