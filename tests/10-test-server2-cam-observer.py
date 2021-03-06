import time
import matplotlib

matplotlib.use('TkAgg')  # needed for tkinter GUI
import matplotlib.pyplot as plt
from duckietown_slimremote.helpers import random_id, timer
from duckietown_slimremote.networking import get_ip, construct_action, make_push_socket
from duckietown_slimremote.pc.camera import SubCameraMaster, cam_window_init, cam_window_update, \
    cam_windows_init_opencv, cam_windows_update_opencv

host = "quacksparrow.local"

robot_sock = make_push_socket(host)
cam = SubCameraMaster(host)

own_id = random_id()
own_ip = get_ip()
msg = construct_action(own_id, own_ip)

print("sending init", msg)
robot_sock.send_string(msg)

cam_windows_init_opencv()

while True:
    img = cam.get_img_blocking()
    cam_windows_update_opencv(img)
