# minecraft-setup
Have fun with your friends, every once in a while!

## setup

Setup credentials in `.env`, you need the usual AWS:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`

```bash

#############################
# Put a password in config
# for example, generate one with:
docker-compose run --rm backups ash
pass=$(strings /dev/urandom | grep -o '[[:alnum:]]' | head -n 30 | tr -d '\n')
echo "RCON_PASSWORD=$pass" >> .env

#############################
# Run
docker-compose up -d

#############################
# Restore backup, if it exists
docker-compose run --rm backups boot restore
```
