"""
File: my_drawing
Name: Joanne Chen
----------------------
TODO: Draw a piglet from Winnie the Pooh.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: It's a drawing of Piglet from Winnie the Pooh! And I just like those cute characters.
    The reason I chose it instead of Pooh is that Piglet no need to wear clothes:)
    """
    window = GWindow()
    back = GRect(500, 500)
    back.filled = True
    back.fill_color = 'thistle'
    window.add(back)
    # hands
    hand_l = GOval(30, 30, x=135, y=290)
    hand_l.filled = True
    hand_l.fill_color = 'lavenderblush'
    hand_l.color = 'lavenderblush'
    window.add(hand_l)
    hand_l1 = GRect(30, 12, x=155, y=300)
    hand_l1.filled = True
    hand_l1.fill_color = 'lavenderblush'
    hand_l1.color = 'lavenderblush'
    window.add(hand_l1)
    hand_r = GOval(30, 30, x=325, y=290)
    hand_r.filled = True
    hand_r.fill_color = 'lavenderblush'
    hand_r.color = 'lavenderblush'
    window.add(hand_r)
    hand_r1 = GRect(30, 12, x=305, y=300)
    hand_r1.filled = True
    hand_r1.fill_color = 'lavenderblush'
    hand_r1.color = 'lavenderblush'
    window.add(hand_r1)
    # feet
    feet_l = GOval(40, 30, x=191, y=440)
    feet_l.filled = True
    feet_l.fill_color = 'lavenderblush'
    feet_l.color = 'lavenderblush'
    window.add(feet_l)
    feet_l1 = GRect(20, 50, x=210, y=400)
    feet_l1.filled = True
    feet_l1.fill_color = 'lavenderblush'
    feet_l1.color = 'lavenderblush'
    window.add(feet_l1)
    feet_r = GOval(40, 30, x=259, y=440)
    feet_r.filled = True
    feet_r.fill_color = 'lavenderblush'
    feet_r.color = 'lavenderblush'
    window.add(feet_r)
    feet_r1 = GRect(20, 50, x=260, y=400)
    feet_r1.filled = True
    feet_r1.fill_color = 'lavenderblush'
    feet_r1.color = 'lavenderblush'
    window.add(feet_r1)
    # body
    body = GOval(140, 170, x=175, y=250)
    body.filled = True
    body.fill_color = 'lightcoral'
    body.color = 'lightcoral'
    window.add(body)
    body1 = GOval(120, 6, x=185, y=290)
    body1.filled = True
    window.add(body1)
    body11 = GOval(117, 6, x=187, y=287)
    body11.filled = True
    body11.fill_color = 'lightcoral'
    body11.color = 'lightcoral'
    window.add(body11)
    body2 = GOval(137, 6, x=176, y=320)
    body2.filled = True
    window.add(body2)
    body22 = GOval(135, 6, x=178, y=317)
    body22.filled = True
    body22.fill_color = 'lightcoral'
    body22.color = 'lightcoral'
    window.add(body22)
    body3 = GOval(136, 6, x=177, y=350)
    body3.filled = True
    window.add(body3)
    body33 = GOval(138, 6, x=176, y=347)
    body33.filled = True
    body33.fill_color = 'lightcoral'
    body33.color = 'lightcoral'
    window.add(body33)
    body4 = GOval(116, 6, x=187, y=380)
    body4.filled = True
    window.add(body4)
    body44 = GOval(117, 6, x=186, y=377)
    body44.filled = True
    body44.fill_color = 'lightcoral'
    body44.color = 'lightcoral'
    window.add(body44)
    # face
    face1 = GOval(140, 175, x=175, y=100)
    face1.filled = True
    face1.fill_color = 'lavenderblush'
    face1.color = 'lavenderblush'
    window.add(face1)
    face2 = GOval(180, 100, x=155, y=175)
    face2.filled = True
    face2.fill_color = 'lavenderblush'
    face2.color = 'lavenderblush'
    window.add(face2)
    # eyes
    eye_l = GOval(8, 12, x=220, y=180)
    eye_l.filled = True
    window.add(eye_l)
    eye_r = GOval(8, 12, x=262, y=180)
    eye_r.filled = True
    window.add(eye_r)
    # mouth
    mouth1 = GOval(30, 20, x=230, y=210)
    mouth1.filled = True
    window.add(mouth1)
    mouth2 = GOval(30, 20, x=230, y=206)
    mouth2.filled = True
    mouth2.fill_color = 'lavenderblush'
    mouth2.color = 'lavenderblush'
    window.add(mouth2)
    # nose
    nose = GOval(20, 10, x=235, y=200)
    nose.filled = True
    nose.fill_color = 'lightcoral'
    nose.color = 'lightcoral'
    window.add(nose)
    # ears
    ear_l = GPolygon()
    ear_l.add_vertex((190, 130))
    ear_l.add_vertex((220, 105))
    ear_l.add_vertex((180, 50))
    ear_l.filled = True
    ear_l.fill_color = 'lightcoral'
    ear_l.color = 'lightcoral'
    window.add(ear_l)
    ear_l1 = GOval(10, 90, x=175, y=51)
    ear_l1.filled = True
    ear_l1.fill_color = 'lightcoral'
    ear_l1.color = 'lightcoral'
    window.add(ear_l1)
    ear_l2 = GPolygon()
    ear_l2.add_vertex((180, 142))
    ear_l2.add_vertex((220, 105))
    ear_l2.add_vertex((175, 90))
    ear_l2.filled = True
    ear_l2.fill_color = 'lightcoral'
    ear_l2.color = 'lightcoral'
    window.add(ear_l2)
    ear_r = GPolygon()
    ear_r.add_vertex((295, 128))
    ear_r.add_vertex((265, 103))
    ear_r.add_vertex((310, 50))
    ear_r.filled = True
    ear_r.fill_color = 'lightcoral'
    ear_r.color = 'lightcoral'
    window.add(ear_r)
    ear_r1 = GOval(8, 90, x=306, y=50)
    ear_r1.filled = True
    ear_r1.fill_color = 'lightcoral'
    ear_r1.color = 'lightcoral'
    window.add(ear_r1)
    ear_r2 = GPolygon()
    ear_r2.add_vertex((309, 141))
    ear_r2.add_vertex((265, 103))
    ear_r2.add_vertex((310, 65))
    ear_r2.filled = True
    ear_r2.fill_color = 'lightcoral'
    ear_r2.color = 'lightcoral'
    window.add(ear_r2)


if __name__ == '__main__':
    main()
