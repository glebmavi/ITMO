import time
from oblig import *
from first import *
from second import *


x = """<table id="2day" class="rasp_tabl" cellspacing="0" cellpadding="0" border="0">
  											<tbody><tr><th class="day">
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

                  </tr>
                  <tr>"""

start_time = time.time()
for i in range(1000):
    oblig(x)
    i += 1
print("Oblig: --- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
for i in range(1000):
    first(x)
    i += 1
print("First: --- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
for i in range(1000):
    second(x)
    i += 1
print("Second: --- %s seconds ---" % (time.time() - start_time))
