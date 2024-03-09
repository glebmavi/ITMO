def get_tag_text(text):
    for i in range(len(text)):
        if text[i] == "<":
            start = i + 1
            end = text.find(">", start, )
            ret = text[i + 1:end]
            return ret
    return None


def get_between_tags(text):
    end = text.find("<", )
    ret = text[:end]
    return ret


x = """<tr><th class="day">
												<script>$("#2day_btn").show();</script>
												<span>Вт</span></th>                <td class="time">
                    <span>10:00-11:30</span>
                                            <div>3, 7, 9, 11, 13, 15, 17</div>
                                        <dd class="rasp_aud_mobile"></dd>
                    <dt class="rasp_corp_mobile"><i class="fa fa-map-marker"></i><span>ул.Ломоносова, д.9, лит. М</span></dt>
                </td>
                <td class="room">
                    <dl>
                        <dd></dd>
                        <dt><i class="fa fa-map-marker"></i><span>ул.Ломоносова, д.9, лит. М</span></dt>
                    </dl>
                </td>
                <td class="lesson">
                    <dl>
                        <dd>Основы профессиональной деятельности(Лек): актовый зал</dd><dt><b>
                                                                    Клименков Сергей Викторович                                                                </b></dt>
                    </dl>
                </td><td class="lesson-format">Очно - дистанционный </td>

                </tr>
                <tr><th class="day"></th>                <td class="time">
                    <span>10:00-11:30</span>
                                            <div>5</div>
                                        <dd class="rasp_aud_mobile"></dd>
                    <dt class="rasp_corp_mobile"><i class="fa fa-map-marker"></i><span></span></dt>
                </td>
                <td class="room">
                    <dl>
                        <dd></dd>
                        <dt><i class="fa fa-map-marker"></i><span></span></dt>
                    </dl>
                </td>
                <td class="lesson">
                    <dl>
                        <dd>Основы профессиональной деятельности(Лек): ZOOM</dd><dt><b>
                                                                    Клименков Сергей Викторович                                                                </b></dt>
                    </dl>
                </td><td class="lesson-format">Дистанционный </td>

                </tr>
                <tr><th class="day"></th>                <td class="time">
                    <span>10:00-11:30</span>
                                            <div>2, 4, 6, 8, 10, 12, 14, 16</div>
                                        <dd class="rasp_aud_mobile">1124 ауд.</dd>
                    <dt class="rasp_corp_mobile"><i class="fa fa-map-marker"></i><span>ул.Ломоносова, д.9, лит. М</span></dt>
                </td>
                <td class="room">
                    <dl>
                        <dd>1124 ауд.</dd>
                        <dt><i class="fa fa-map-marker"></i><span>ул.Ломоносова, д.9, лит. М</span></dt>
                    </dl>
                </td>
                <td class="lesson">
                    <dl>
                        <dd>Программирование(Лек)</dd>четная неделя<dt><b>
                                                                    Письмак Алексей Евгеньевич                                                                </b></dt>
                    </dl>
                </td><td class="lesson-format">Очно - дистанционный </td>

                </tr>"""


def main(text):
    tags = ''
    data = ''
    temp = text
    while temp is not None:
        tagText = get_tag_text(temp)
        if tagText is None:
            ret = tags + '\n' + data
            return ret
        elif '/' in tagText:
            dataText = get_between_tags(temp)
            if dataText is not None or dataText != '':
                data += '"' + get_between_tags(temp) + '"' + ';'
        else:
            tags += tagText + ';'
        to_remove = "<" + tagText + ">"
        end = temp.find(to_remove) + len(to_remove)
        to_remove = temp[0:end]
        temp = temp.removeprefix(to_remove)

    ret = tags + '\n' + data
    return ret


outputFile = open("4.csv", "w")
outputFile.write(main(x))
