# AtomicHack
![](https://github.com/gruzdev-as/AtomicHack/assets/95618433/7ee5bba3-ef52-4263-8b8a-84e337529ebe)

## Team Members:

1) [**Груздев Александр**](https://github.com/gruzdev-as) - Captain + ML (a little bit)
2) [**Литвинов Максим**](https://github.com/maksimlitvinov39kg) - ML
3) [**Рыжичкин Кирилл**](https://github.com/l1ghtsource) - ML
4) **Аксеновский Максим** - ML
5) [**Лозовенко Артем**](https://github.com/7aaassss) - Backend + Frontend

## Кейс "Определение дефектов сварных швов с помощью нейросети (DS)"

Ссылка на презентацию: [Тык](https://www.figma.com/design/jDp04wQ6hO3JvYr6Le8CqO/MISIS-%2B-SBER-AI-%2B-GPB-TEAM?node-id=10401-1109&t=Kh5W5AN8Ng87az8Q-1) 

Ссылка на поднятое решение:

## Описание решения 

Мы предлагаем использовать для решения задачи детекции дефекта сварного шва две модели - YOLOv{VERSION}X а также модель Detection Transformer. 
Модели могут использоваться раздельно, а также их результаты могут ансамблироваться используя NMS (Non-Maximum Suppression) 
Серверная часть написана на Streamlit и Flask

Достигнутые результаты: 
- Метрика на публичном ЛБ 0,93 map50
- Метрика на приватном ЛБ ХХ
- Время инференса на одно изображение: 0.6 сек

## Воспроизведение решения 

Для воспроизведения решения воспользуйтесь ноутбуками из папки notebooks. 

Для сборки и демо решения локально нужно : 
1) ```git clone https://github.com/gruzdev-as/AtomicHack.git```

2) ```docker-compose up -d --build```

3) ```перейти на localhost:8051```

## Потенциальные улучшения и перспективы развития 

Команда проекта уделила большое внимание проработке потенциальных путей встраивания решения в экосистему конечного заказчика. На этапе концепта предложены следующие идеи, подробнее о которых можно найти в презентации: 
1) Для процесса обучения - предоставление справочных материалов по каждому допущенному дефекту в режиме реального времени;
2) Для продакшна - создание "таблицы лидеров" производства для регуляции рабочего процесса, а также реализации механизма премирования сотрудников, которые допускают меньше брака, чем остальные;
