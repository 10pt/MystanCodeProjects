"""
Title: Tribute to 2025 world expo

Thought drawing this logo would be fun, and it didn't fail me.
The eyeball part cost me half of the total worktime!
"""

from campy.graphics.gobjects import GOval, GRect,GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window = GWindow(width=800, height=1000)
    circle1 = GOval(150,150, x=450, y = 50)
    circle1.color ='red'
    circle1.filled = True
    circle1.fill_color ='red'
    window.add(circle1)
    circle1_1= GOval(70,70,x=520,y=75)

    window.add(circle1_1)
    circle1_1.color = 'white'
    circle1_1.filled = True
    circle1_1.fill_color = 'white'
    circle1_2 = GOval(30, 30, x=550, y=80)
    window.add(circle1_2)
    circle1_2.color = 'deepskyblue'
    circle1_2.filled = True
    circle1_2.fill_color = 'deepskyblue'
    circle2 = GOval(180, 80, x=480, y=180)
    window.add(circle2)
    circle2.color = 'red'
    circle2.filled = True
    circle2.fill_color = 'red'
    circle3 = GOval(105, 130, x=520, y=240)
    window.add(circle3)
    circle3.color = 'red'
    circle3.filled = True
    circle3.fill_color = 'red'
    circle4 = GOval(165, 140, x=470, y=350)
    window.add(circle4)
    circle4.color = 'red'
    circle4.filled = True
    circle4.fill_color = 'red'
    circle4_1 = GOval(80, 70, x=540, y=400)
    window.add(circle4_1)
    circle4_1.color = 'white'
    circle4_1.filled = True
    circle4_1.fill_color = 'white'
    circle4_2 = GOval(35, 35, x=580, y=410)
    window.add(circle4_2)
    circle4_2.color = 'deepskyblue'
    circle4_2.filled = True
    circle4_2.fill_color = 'deepskyblue'
    circle5 = GOval(140, 140, x=370, y=420)
    window.add(circle5)
    circle5.color = 'red'
    circle5.filled = True
    circle5.fill_color = 'red'
    circle5_1 = GOval(50, 50, x=410, y=490)
    window.add(circle5_1)
    circle5_1.color = 'white'
    circle5_1.filled = True
    circle5_1.fill_color = 'white'
    circle5_2 = GOval(20,20, x=425, y = 520)
    window.add(circle5_2)
    circle5_2.color = 'deepskyblue'
    circle5_2.filled = True
    circle5_2.fill_color = 'deepskyblue'
    circle6 = GOval(100, 100, x=290, y=420)
    window.add(circle6)
    circle6.color = 'red'
    circle6.filled = True
    circle6.fill_color = 'red'
    circle7 = GOval(75, 115, x=260, y=335)
    window.add(circle7)
    circle7.color = 'red'
    circle7.filled = True
    circle7.fill_color = 'red'
    circle8 = GOval(125, 125, x=190, y=255)
    window.add(circle8)
    circle8.color = 'red'
    circle8.filled = True
    circle8.fill_color = 'red'
    circle8_1 = GOval(60, 60, x=240, y=300)
    window.add(circle8_1)
    circle8_1.color = 'white'
    circle8_1.filled = True
    circle8_1.fill_color = 'white'
    circle8_2 = GOval(30, 30, x=250, y=302)
    window.add(circle8_2)
    circle8_2.color = 'deepskyblue'
    circle8_2.filled = True
    circle8_2.fill_color = 'deepskyblue'
    circle9 = GOval(100, 100, x=255, y=180)
    window.add(circle9)
    circle9.color = 'red'
    circle9.filled = True
    circle9.fill_color = 'red'
    circle10 = GOval(105, 105, x=180, y=165)
    window.add(circle10)
    circle10.color = 'red'
    circle10.filled = True
    circle10.fill_color = 'red'
    circle10_1 = GOval(60, 60, x=200, y=190)
    window.add(circle10_1)
    circle10_1.color = 'white'
    circle10_1.filled = True
    circle10_1.fill_color = 'white'
    circle10_2 = GOval(30, 30, x=205, y=195)
    window.add(circle10_2)
    circle10_2.color = 'deepskyblue'
    circle10_2.filled = True
    circle10_2.fill_color = 'deepskyblue'
    circle11 = GOval(100, 105, x=265, y=115)
    window.add(circle11)
    circle11.color = 'red'
    circle11.filled = True
    circle11.fill_color = 'red'
    circle12 = GOval(120, 120, x=335, y=45)
    window.add(circle12)
    circle12.color = 'red'
    circle12.filled = True
    circle12.fill_color = 'red'

    Text1 = GLabel('DA\'AN, TAIPEI, TAIWAN', x=240, y=615 )
    Text1.font ='-35'
    window.add(Text1)
    Text2 = GLabel('S  T  C  O', x=240, y=735)
    Text2.font = '-100'
    Text2.color = 'red'
    Text2.filled =True
    Text2.fill_color = 'red'
    window.add(Text2)

    Text3 = GLabel('2  0  2  2', x=240, y=850)
    Text3.font = '-100'
    Text3.color = 'deepskyblue'
    Text3.filled = True
    Text3.fill_color = 'deepskyblue'
    window.add(Text3)


if __name__ == '__main__':
    main()
