<details> <summary>Задание:</summary>

```Параллельный запуск процессов

1. Реализовать класс ProcessController, который организует очередь заданий и параллельное выполнение заданий из очереди.
 Данный класс должен содержать следующие методы:
-	set_max_proc — аргумент: n. Метод устанавливает ограничение: максимальное число одновременно выполняемых заданий не
должно превышать n.
-	start — аргументы: tasks, max_exec_time:
2. tasks — список заданий. Задание представляет кортеж вида: (функция, кортеж входных аргументов для функции).
Пример: tasks = [(function0, (f0_arg0, f0_arg1)), (function1, (f1_arg0, f1_arg1, f1_arg2)), (function2, (f2_arg0, ))]
4. max_exec_time — максимальное время (в секундах) работы каждого задания из списка tasks

Данный метод помещает в очередь все задания из tasks. В случае, если не достигнуто ограничение на максимальное число 
одновременно работающих заданий, метод запускает выполнение заданий из очереди до тех пор, пока не будет достигнуто это 
ограничение. Запуск задания представляет порождение нового процесса, который выполняет соответствующую функция с её 
аргументами. При этом каждый запущенный процесс для задания из tasks не должен работать дольше max_exec_time.
-	wait — (без аргументов) ждать пока не завершат своё выполнение все задания из очереди.
-	wait_count — (без аргументов) возвращает число заданий, которые осталось запустить.
-	alive_count — (без аргументов) возвращает число выполняемых в данный момент заданий.
2. Придумать пример, который продемонстрирует корректность реализации класса ProcessController.
3. Написанный код на языке python должен соответствовать соглашению PEP8.
```
</details>


В файле [process_controller.py](process_controller.py) представлен класс `ProcessController` организующий порядок выполнения параллельных процессов.

Он включает аттрибуты:
- `max_proc` - [int] максимальное число одновременно выполняемых заданий (по умолчанию = 1)
- `threads` - [threading.Thread] список потоков <br>

Методы:
- `set_max_proc(n)` - устанавливает максимальное значение `max_proc`
- `wait()` - ожидает завершения выполнения заданий
- `wait_count()` - возвращает число заданий, которые осталось запустить
- `alive_count()` - количество заданий выполняемых в данный момент

В файле [task.py](task.py) представлена функция-пример `example_task(message, sleep_time)` выполняющая список заданий `tasks` из кортежей. Эта функция принимает в аргументах сообщение для трансляции и время задержки для дальнейшего отслеживания параллельных процессов.

В файле [main.py](main.py) в функции `main()` представлена реализация проверки класса `ProcessController` на примере заданий `tasks`

<details> <summary>Разбор примера:</summary>

Функция `main()`

```
    # создаем экземпляр класса
    pc = ProcessController()
    
    # задаем лимит одновременно выполняяемых заданий
    pc.set_max_proc(2)
    
    # передаем в аргументах список заданий и лимит времени на выполнение задания
    pc.start(tasks1, 3)
    
    # отслеживаем временные показатели
    logging.debug(f" - Currently {pc.alive_count()} processes are alive")
    logging.debug(" - Adding external tasks...")
    logging.debug(f" - Currently {pc.wait_count()} tasks left")
    
    # добавляем новые задания
    pc.start(tasks2, 3)
    
    # отслеживаем временные показатели
    logging.debug(f" - Currently {pc.alive_count()} processes are alive")
    logging.debug(f" - Currently {pc.wait_count()} tasks left")
    
    # ожидаем завершения
    pc.wait()
    logging.debug(" - All tasks completed.")

```

Вывод в логах:
```
    DEBUG:root: > Task 2 started
    DEBUG:root: > Task 1 started
    DEBUG:root: < Task 2 finished
    DEBUG:root: < Task 1 terminated
    DEBUG:root: - Currently 2 processes are alive
    DEBUG:root: - Adding external tasks...
    DEBUG:root: - Currently 2 tasks left
    DEBUG:root: > Task 4 started
    DEBUG:root: > Task 3 started
    DEBUG:root: < Task 3 finished
    DEBUG:root: > Task 5 started
    DEBUG:root: < Task 4 terminated
    DEBUG:root: > Task 6 started
    DEBUG:root: < Task 5 terminated
    DEBUG:root: > Task 7 started
    DEBUG:root: < Task 6 finished
    DEBUG:root: - Currently 2 processes are alive
    DEBUG:root: - Currently 1 tasks left
    DEBUG:root: > Task 8 started
    DEBUG:root: < Task 7 finished
    DEBUG:root: < Task 8 terminated
    DEBUG:root: - All tasks completed.
    
    Process finished with exit code 0
```
</details>
