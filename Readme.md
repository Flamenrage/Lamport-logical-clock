### Автор: Flamenrage

## Реализовация алгоритма логических часов Лэмпорта

<p align="center"> 
<img  width="650" align="center" src="processes.png"/> <br> 
Схема взаимодействия процессов
</p>


<p align="center"> 
Вывод в консоль <br>
<img  width="800" align="center" src="вывод.png"/> <br> 
</p>
Часы Лэмпорта — простой алгоритм определения порядка событий в распределённой системе. В связи с отсутствием возможности полностью синхронизировать все узлы - вводится отношение частичного порядка с минимальными затратами, метод является прообразом метода векторных часов.

Лесли Лэмпорт разработал механизм, при использовании которого отношение порядка задаётся одним числом. Часы Лэмпорта монотонно увеличивают счётчик каждого процесса согласно определенным правилам.

Программа состоит из трех файлов:
main.py, processes.py и service.py


