# Potions

This is a basic project to teach Flask. As routes are added, they will be added to the doc.


## Routes
- `/`: 
  - `GET`: Returns a welcome message.
- `/inventory`: 
  - `GET`: Returns entire inventory
- `/potions`
  - `POST`: Adds a potion to database the redirects to `/inventory`

## Models
- `Potion`
 - `id (int)`: generated automatically.
 - `name (string)`: the name of the potion. unique.
 - `quantity (int)`: the amount in stock.
 - `price (int)`: the amount in gold pieces.

## Files & Folders
- `app.py`: Contains the controller (aka the routes and logic)
- `deprecated`: Code files no longer used. Kept for demo purposes.
- `model.py`: Contains the model