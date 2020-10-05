from PIL import Image, ImageDraw, ImageFont
import SchedParse


def genScheduleImg(id, host, bgColor, txtColor, lnColor, imgName, week, year, uGuid):
    startX = 70
    incX = 239
    sched = SchedParse.getSched(id, host, week, year, uGuid)

    fnt = ImageFont.truetype("arial.ttf", 15)
    img = Image.new('RGB', (1340, 550), color=bgColor)
    pic = ImageDraw.Draw(img)

    for item in sched:
        pic.text((item["x"] * 1.1, item["y"] ), item["text"], fill=txtColor, font=fnt, stroke_width=0)

    pic.line([(0, 16), (img.size[0], 16)], fill=lnColor)

    for i in range(6):
        pic.line([((startX + incX * i + 1), 0), ((startX + incX * i + 1), img.size[1])], fill=lnColor)

    img.save(imgName)

