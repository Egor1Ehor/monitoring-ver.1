import os
import psutil

def get_name():
    return{
        "Имя системы": os.name,
        "Имя пользователя": os.getlogin()

    }
def get_cpu():
    return{
        "Количество ядер":psutil.cpu_count(logical=True),
        "Частота CPU":psutil.cpu_freq(percpu=False),
        "Использование CPU пользователями":psutil.cpu_times_percent(interval=None, percpu=False),
        "Загрузка ядер":dict(enumerate((psutil.cpu_percent(percpu=True, interval=1)),1)),
    }
def get_mem():
    return{
        "Использованная память":psutil.virtual_memory()
    }
def get_batery():
    return{
        "Заряд батареи":psutil.sensors_battery()
    }
def show(name,cpu,mem,batery):
    print(name,cpu,mem,batery)

def main():
    n=get_name()
    c=get_cpu()
    m=get_mem()
    b=get_batery()
    print(n)
    print(c)
    print(m)
    print(b)
if __name__ == '__main__':
    main()
    