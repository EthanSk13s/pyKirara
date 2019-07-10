# Version 1.2.0 [2019/7/10]
## Additions
- Added get_cards and get_idols function which takes a list of ids and makes them to a list of card objects
- Added chara attr to card object which is an Idol object
## Changes
- Card attrs such as skill, and lead_skill are now objects instead of dicts
    - Some documentation are missing since I have no idea what some of them do

# Version 1.1.1 [2019/6/22]
## Hotfix
- Fixed card translations using the same string

# Version 1.1.0 [2019/6/21]
## Additions
- Added translate function to translate some japanese strings to english such as:
    - Card titles
    - Skill names (Including Lead skills)
    - Event names
    - Gacha names
- Added translate parameters to get_card, and get_now
## Changes
- Changed how name is matched in get_id from `x in y` to regex matching
    - This prevents appending cards from both Rin and Rina since both names have 'Rin' in them, or any other similar names
## Fixes
- Fixed duplicate ID appending in get_id when rarity param is passed
- Fixed mismatched category in get_now func

# Version 1.0.0 [2019/6/11]
## NOW ON PyPI!!!!
- To install:
    ```
     pip install pyKirara
    ```
## FULL REWRITE OF DUMB CODE!!!!
- All classes inheriting from Kirara are now dataclasses
    - I made the dumb mistake of spawning new clients everytime 
    any class is initialized. Everything should've been in one session
    in the first place
    - usage should still be mostly the same: initialize client get data use data

## General Changes & Additions
- get_id now has the ability to get one specific card
    - added ability to pass only the idol's first name
        - a bit buggy since substrings are weird
    - additional params added, rarity, position
        - rarity can be from n to ssr, or n+ to ssr+
            - check enums for dict mapping
        - position is the order when the card was released
            - EX: uzuki ssr 4, would get uzuki's 4th ssr
- Error catching is added to functions

## Card Class Changes & Additions
- changed card class members
    - skill_id is now just skill which is a dict of the skill's info
    - added lead_skill, which is also a dict of the skill's info
    - attribute is no longer a dict mapping, it now returns a string
    
# Version 0.5.0 [2019/5/27]
## Additions
- added has_spread and icon members to card objects
    - icon member is a link to the card's icon
    - has_spread is a bool value whether the card has a 
    spread image or not
    - icon is now a category for the save_image function
- also added icon member to idol object
## Changes
- event_list function to happening_list functions
    - happening_list can also now list Gacha objects
        - An additonal parameter called category can be used
        to define which object type to use
- get_id function now returns a list of card objects matching the name given
## Minor Changes
- Card.save_image() now gets the image via a stream now

# Version 0.4.1 [2019/5/18]
## Additions
- Added basic errors
- Documentations on Event objects
## Changes
- Changed how image category is handled from elif statements to a dictionary

## Bug Fixes
- Fixed transparent image links giving 404s (typo in link)
- Fixed typos in docstrings

# Version 0.4.0 [2019/5/13]
## Images and event stuff added
- Added [save_image()](https://github.com/EthanSk13s/pyKirara/blob/master/pyKirara/card.py#L174) to card object


    - This is a way to save images as a file-like object to save locally do something else, or just get the raw links

- Added [Event object](https://github.com/EthanSk13s/pyKirara/blob/master/pyKirara/client.py#L188) and [event_list()](https://github.com/EthanSk13s/pyKirara/blob/master/pyKirara/client.py#L256) function

    - The Event object is made due to a way to recall past events
    - event_list is to get a list of event objects happening currently

# Version 0.3.0 [2019/4/28]
## The "I'm not dead update"
- Added get_id finally, also with documents wow!
- Next update soon, I guess

# Version 0.2.0 [2019/3/3]
## Card object is now fully done!
- Fully documented
- Added functions to calculate stat value in a specific value, and to automatically find skill description
- Fixed album_id usin enum function when it's not suppose to
- enum function is now for the type attribute!

# Version 0.2.dev1 [2019/2/28]
- Basic Card object added (No Documentations)
- Attribute enum added
- Default request timeout for client is now 5 seconds

# Version 0.1.2 [2019/2/25]
- Moved Idol class separate from client
- Added more docstrings
- Updated docs

# Version 0.1.1 [2019/2/24]
- Finished all but one of the value for home_towns in enum (Too lazy to find)
- Finished Idol data load

# Version 0.1.0 [2019/2/23]
- Initial release
