# wizworm-cogs
Cogs which are designed to manage and query noobshack gameservers in a chatops style.

## Cog Overview
### gaze
A wrapper around the Gaze noobshack dedicated gameserver API. Queries gaze.reulan.com to get server statistics.

### points
not implemented.

### future
To be implemented:
- RCON access or gameserver admin functions
- trigger builds/deployments of applications
- autoscale gameserver infrastructure
- BattleMetrics information
- List points for all members

## Installation
### Wizworm Configuration
In order to configure a new instance of the Red-Bot and theme it for wizworm the following commands are issued:

#### Base
```
!load downloader
```

#### noobshack cogs
```
!repo add wizworm-cogs https://github.com/noobshack/wizworm-cogs
!cog install wizworm-cogs gaze
!load gaze
```

### Local Development
For Manjaro Linux the following setup process was done:
1. Install python + java [as mentioned on the Red docs](https://docs.discord.red/en/stable/install_linux_mac.html#arch-linux)
```
sudo pacman -Syu python python-pip git jre11-openjdk-headless base-devel
```

2. Setup then enter virtual environment
```
python -m venv ~/kit/redenv
source ~/kit/redenv/bin/activate
```

3. Install Red Discord Bot to `redenv`
```
python -m pip install -U pip setuptools wheel Red-DiscordBot
```

4. Install packages needed for cogs:
```
python -m pip install -U requests
```

### Kubernetes
#### Persistant Storage
If a Kubernetes volume mount is in use, it can be mounted to the volume in a path different than `/cogs` or `/core`.

Wizworm has it's "custom content" set to `/home/wizworm/wizzy` which I use as my base install path since in my case the data would carry over across container reboots or
and allow me to keep it through k8s cluster migrations.

To use the volume mount path, you can issue a single command to the Discord bot:
```
[p]installpath /home/wizworm/wizzy
```

This will retain the previous settings and versions of the installed cogs, if needed the PVC can be backed up and then cogs can be updated with
```
[p]cog update
```

## other cogs I enjoy
### casino cog
[Jumper-plugins - casino](https://github.com/Redjumpman/Jumper-Plugins)
```
!load downloader
!repo add jumper-cogs https://github.com/Redjumpman/Jumper-Cogs
I agree
!cog install jumper-cogs casino
!load casino
```

Additional configuration
[Casino Owner/Admin/User commands](https://github.com/Redjumpman/Jumper-Plugins/wiki/Casino-RedV3#owner-level)

```
!casinoset name noobshack
!casinoset cooldown blackjack 1	
!casinoset min blackjack 1
!casinoset max blackjack 9999
!casinoset multiplier blackjack 2
```

### League cog
[Malarne - League](https://github.com/Malarne/discord_cogs)
```
!repo add MalarneCogs https://github.com/Malarne/discord_cogs
!cog install MalarneCogs League
!load casino
```
