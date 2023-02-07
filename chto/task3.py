# Преобразуйте позицию DD (десятичные градусы) в DMS (градусы, минуты, секунды).
# Inputs:
# dd_lat и dd_lon 2 значения с плавающей точкой, представляющие широту и долготу в градусах - т.е.
# 2 значения с плавающей точкой, включенные в [-90, 90] и [-180, 180].
# Обратите внимание, что широта 0 - северная, долгота 0 - восточная.
# Outputs:
# Набор широт DMS, сформированный следующим образом: DDD*mm'sss.sss"C
# Значения:
# DDD: градусы
# мм: минуты
# ss.sss: секунды, округленные до 3 знаков после запятой
# C: первая буква в верхнем регистре кардинального
# направления
# источники о WGS 84 в Википедии (https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84)

# Task3 test example
# test.describe("Basic conversions")
# test.it("should return the right DMS")
# test.assert_equals(convert_to_dms(35.03299485527936, 33.233755230903625),
#                                  ('035*01\'58.781"N', '033*14\'01.519"E'))
# test.assert_equals(convert_to_dms(-37.111415669561595, -12.284317023586482),
#                                  ('037*06\'41.096"S', '012*17\'03.541"W'))
# test.assert_equals(convert_to_dms(19.61499312350978, -155.48217818140984),
#                                  ('019*36\'53.975"N', '155*28\'55.841"W'))

#Satan start resolving! Good luck!
#def convert_to_dms(dd_lat, dd_lon):
# gl hf !
# return dms_lat, dms_lon