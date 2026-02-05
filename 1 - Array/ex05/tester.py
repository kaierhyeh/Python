#!/usr/bin/env python3

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)

# #!/usr/bin/env python3\r Error:
# /r Error:
# Windows 喜歡用兩個隱形字元來換行：\r\n (CRLF)。
# Linux/Mac 喜歡用一個隱形字元來換行：\n (LF)。
