def labeler(tags_qs, html=True):
    """ tags_qs: queryset of labels;
        label objects need a 'name' and 'color' attribute
        html: True if you want a <span> style output
              False if you want just a dictionary
    """

    if html:
        ret = ''
    else:
        ret = []
    for tag in tags_qs:
        source_color = tag.color if tag.color else "#ffffff"
        col = source_color.replace('#', '')
        R = int('0x%s' % col[0:2], 16)
        G = int('0x%s' % col[2:4], 16)
        B = int('0x%s' % col[4:], 16)
        lum = 1 - (0.299 * R + 0.587 * G + 0.114 * B) / 255
        if lum < 0.5:
            colore_font = 'black'  # bright colors - black font
        else:
            colore_font = 'white'  # dark colors - white font
        if html:
            ret += (
                "<span style='display: inline-block; padding:5px; margin: "
                "0 3px; background-color:#{}; color:{}; font-weight: bold'>"
                "{}</span>"
            ).format(col, colore_font, tag.name)
        else:
            ret.append(
                {'bg_color': col, 'font_color': colore_font, 'label': tag.name}
            )
    return ret
    
