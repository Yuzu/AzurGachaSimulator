# Azur Lane Gacha Simulator
This is pretty much exactly what it sounds like. The rate are the exact same as in the game. 

# Dependencies

* BS4

# Misc.
Most of the ship information is pulled from the [Azur Lane Wiki](https://azurlane.koumakan.jp/Azur_Lane_Wiki). Depending on how they decide to organize their information, it may break the program. 

As for now, the program utilizes a "pointer" to check for new ships after a certain point so that the update time does not take an eternity.

If you must reconstruct the entirety of **shipList.json**, then enter **info.json** and change the value of *"pointer"* to **1**, **NOT 0.**