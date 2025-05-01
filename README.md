# florr-auto-pathing

Time to upload some of my useful codes.

The whole codes stand on CLIENT-SIDE.

This project is **welcomed** to be used in any other florr.io projects.

## The Lazy Theta Star

After I used `a*` pathing for a few months, I found this method caused a lot of time wasting on collision with florr's walls, I quickly turned to use `lazyθ*`. And here's the differences (Green for lazy_theta_star and Red for a_star)

![](./compare.jpg)

## Maps

To decide on the positions and areas, I've already prepared `map_select.py` and `area_select.py` for you.

> \> python3 map_select.py # And you click anywhere you want on the map
>
> Map position: (53, 144)
> Map position: (55, 109)

> \> python3 area_select.py # And you first click on the left_top bound, next click on the right_bottom bound.
>
> Area added: [(6, 5), (40, 44)]
> Area added: [(1, 43), (27, 87)]
> Final areas: [[(6, 5), (40, 44)], [(1, 43), (27, 87)]]

## Implements

For this is CLIENT-SIDE, so I haven't do any resolution support.

You need to run this code in 1920x1080 with florr.io tab on the top and fullscreen.

Go run `main.py`

```python
if __name__ == "__main__":
    apply_map("<map>")
    location = <location> # the location decided in `map_select.py`
    dedicated_area = [(0, 0), (200, 200)]  
    # optional, if the player has moved into the area and got stuck, the code will end. Otherwise it will try to callibrate until reaching the final location
    while True:
        if lazy_theta_pathing(location, dedicated_area):
            break
    print("Pathing Done")
```

