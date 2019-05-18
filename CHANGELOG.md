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
