# Tank
a DIY tank project of mine... in works since October '18!

joyReadoutOnly.py:    Spews data dump for analog joystick movement on Pro Controller

                      Nintendo Switch Pro Controller data dump:
                        Left Joystick:
                          - Axis 0 = (left) -.845 to +.770 (right)
                          - Axis 1 = (up) -.859 to +.826 (down)
                        Right Joystick:
                          - Axis 2 = (left) -.829 to +.765 (right)
                          - Axis 3 = (up) -.829 to +.811 (down)

servo.py:             Controlling the servos with code only

joyVert.py:           Controlling the pitch servo with Pro Controller, right joystick, up-down movements

joyHoriz.py:          Controlling the yaw servo with Pro Controller, right joystick, left-right movements

joyFinal.py:          includes snippets to get data from Switch Pro controller, outputs right analog
                      stick data to pitch servo (Parallax Standard Servo) and yaw servo (Parallax 
                      Continuous Rotation Servo). Body of turret has yet to be designed and 3D
                      printed. 
                      Pitch Servo pin#18
                      Yaw Servo pin#26
