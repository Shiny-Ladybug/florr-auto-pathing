import cv2
import os

map_name = "desert"
assert map_name in [path.removesuffix(".png") for path in os.listdir("./maps")]
map_image = cv2.imread(f"./maps/{map_name}.png")

map_image_copy = map_image.copy()


def on_mouse_click(event, x, y, flags, param):
    global map_image
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Map position: ({x}, {y})")
        map_image = map_image_copy.copy()
        cv2.circle(map_image, (x, y), radius=2,
                   color=(0, 0, 255), thickness=-1)
        cv2.putText(map_image, f"({x}, {y})", (x + 5, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (4, 250, 4), 1)
        cv2.imshow("Map", map_image)


cv2.imshow("Map", map_image)
cv2.setMouseCallback("Map", on_mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()
