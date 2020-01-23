# wizworm-cogs
A future home for custom Red cogs.

Various cogs can be created to manage different aspects of noobshack in a chatops style.
- create/manage/view dedicated gameserver infrastructure
- administration of those servers
- trigger builds/deployments of applications
- autoscale kubernetes infrastructure
- redeploy itself with minimal downtime.

## Third-party plugins
[Jumper-plugins - casino](https://github.com/Redjumpman/Jumper-Plugins)

### Installation
```
!load downloader
!repo add jumper-cogs https://github.com/Redjumpman/Jumper-Cogs
I agree
!cog install jumper-cogs casino
!cog install jumper-cogs russianroulette
!load casino
!load russianroulette
!cog update
```

### Configuration
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

### Useful commands
* `!info`
* `!cog list jumper-cogs` for information on available cogs.
