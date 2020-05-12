from math import ceil
from templates.frame import header, footer


def audio_line(audios, titles):
    """
    Two line tr, one for title and another for audio
    """
    title_line = ["<tr>", "</tr>"]
    for title in titles:
        if title is not None:
            title_line.insert(-1, f"<td><strong>{title}</strong></td>")
        else:
            title_line.insert(-1, "<td></td>")
    audio_line = ["<tr>", "</tr>"]
    for audio in audios:
        if audio is not None:
            audio_line.insert(-1, f"""<td><audio controls=""><source src="{audio}"></audio></td>""")
        else:
            audio_line.insert(-1, "<td></td>")
    return "".join(title_line) + "".join(audio_line)


def audio_lines(audios, titles, width=2):
    """
    Many lines of width ended with empty line.
    """
    l = []
    for i in range(0, ceil(len(audios) / width)):
        audio_buf = []
        title_buf = []
        begin = i * width
        end = begin + width
        while begin < end:
            if begin < len(audios):
                audio_buf.append(audios[begin])
                title_buf.append(titles[begin])
            else:
                audio_buf.append(None)
                title_buf.append(None)
            begin += 1
        l.append(audio_line(audio_buf, title_buf))
    return "".join(l) + "<tr>" + "<td></td>" * width + "</tr>"


def table_of_list(text, paths, titles, width=2):
    return f"""
    <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th colspan={width} style="text-align: left;">{text}</th>
                </tr>
            </thead>
            <tbody>
            {audio_lines(paths, titles, width)}
            </tbody>
        </table>
    </div>
    """


def table_with_texts(texts, pathss, titless, width=2):
    m = [
        table_of_list(text, paths, titles, width) for text, paths, titles in zip(texts, pathss, titless)
    ]
    return "".join(m)

