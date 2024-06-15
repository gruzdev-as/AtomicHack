# AtomicHack
![](https://github.com/gruzdev-as/AtomicHack/assets/95618433/7ee5bba3-ef52-4263-8b8a-84e337529ebe)

Team Members:
1) **Груздев Александр** - Captain + ML (a little bit)
2) **Литвинов Максим** - ML
3) **Рыжичкин Кирилл** - ML
4) **Аксеновский Максим** - ML
5) **Лозовенко Артем** - Backend + Frontend

## Кейс "Определение дефектов сварных швов с помощью нейросети (DS)"

Ссылка на презентацию: 
Ссылка на поднятое решение:

## Описание решения 

Мы предлагаем использовать для решения задачи детекции дефекта сварного шва две модели - YOLOv{VERSION}X а также модель Detection Transformer. 
Модели могут использоваться раздельно, а также их результаты могут ансамблироваться используя NMS (Non-Maximum Suppression) 
Серверная часть написана на ХХХ и ХХХ

Достигнутые результаты: 
- Метрика на публичном ЛБ ХХ
- Метрика на приватном ЛБ ХХ
- Время инференса на одно изображение ХХ сек

## Воспроизведение решения 

Для воспроизведения решения ...

## Потенциальные улучшения и перспективы развития 

Команда проекта уделила большое внимание проработке потенциальных путей встраивания решения в экосистему конечного заказчика. На этапе концепта предложены следующие идеи, подробнее о которых можно найти в презентации: 
1) Для процесса обучения - предоставление справочных материалов по каждому допущенному дефекту в режиме реального времени;
2) Для продакшна - создание "таблицы лидеров" производства для регуляции рабочего процесса, а также реализации механизма премирования сотрудников, которые допускают меньше брака, чем остальные;
