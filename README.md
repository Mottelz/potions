# Potions

This is a basic project to teach Flask. As routes are added, they will be added to the doc.


## Routes
- `/`: 
  - `GET`: Returns a welcome message.
- `/inventory`: 
  - `GET`: Returns entire inventory.
- `/inventory/<category>/<id>`: 
  - `GET`: Returns the selected item. Use `/inventory` for complete list.

## Files
- `app.py`: Contains the controller (aka the routes and logic)
- `deprecated.py`: Code snippets for teaching purposes
- `staticModel.py`: Code to get hardcoded data.