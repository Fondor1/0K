# Âbsolute ZERO (0K)
This repository is intended to be a sandbox for the Guild Wars 2 guild Âbsolute ZERO.

# Project ideas
Various guild members have proposed ideas for projects and apps that tie the Guild Wars 2 trading post and other API functions to various external devices.

### Crafting Profit Calculator
Collects information on all materials available in bank and inventory and decides if it is more profitable to sell the raw materials or to produce an item.

##### Benefits/Features
* Dynamically optimizes profit with minimal time expenditure
* Player can unselect materials that are earmarked for other purposes 
* Player can save and restore which recipes or materials are hidden

##### Challenges
* Cannot programmatically determine which recipes a player has unlocked (As a workaround, each recipe can be un-selectable to eliminate recipes that the player does not have)

### Trading Post Push Notifications for Buy/Sell Order Completion
Allows players to set a threshold on price for buy and sell orders. Software can send notifications or a daily digest summary of items.

##### Benefits/Features
* Allows monitoring of pricing, essentially allowing players to set a [stop or limit order](http://www.investopedia.com/ask/answers/04/022704.asp).

##### Challenges
* The API can only notify of specific conditions but cannot purchase or sell items on behalf of the player
