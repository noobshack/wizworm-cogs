# wizworm discord bot manual configuration

## Installation
### Base
```
!load downloader
```

### noobshack cogs
```
!repo add wizworm-cogs https://github.com/noobshack/wizworm-cogs
!cog install wizworm-cogs gaze
!load gaze
```

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

???
!casinoset access <game> <access>
!casinoset multiplier ?
!casinoset payoutlimit <limit>
!casinoset payouttoggle
```

### League cog
[Malarne - League](https://github.com/Malarne/discord_cogs)
```
!repo add MalarneCogs https://github.com/Malarne/discord_cogs
!cog install MalarneCogs League
!load casino
```
