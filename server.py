import time
import random
import sys
import os
from colorama import init, Fore, Back, Style

init()

def print_with_delay(text, delay=0.03, color=Fore.WHITE):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_command(command, color=Fore.GREEN):
    print(f"{Fore.CYAN}root@server:~# {color}{command}{Style.RESET_ALL}")
    time.sleep(0.5)

def print_error(text, delay=0.02):
    for char in text:
        print(f"{Fore.RED}{char}", end='', flush=True)
        time.sleep(delay)
    print(f"{Style.RESET_ALL}")

def print_warning(text, delay=0.02):
    for char in text:
        print(f"{Fore.YELLOW}{char}", end='', flush=True)
        time.sleep(delay)
    print(f"{Style.RESET_ALL}")

def simulate_system_check():
    print_command("top -bn1")
    print_with_delay("top - 14:30:15 up 45 days, 23:45,  2 users,  load average: 1.25, 1.18, 1.12", 0.02)
    print_with_delay("Tasks: 245 total,   1 running, 244 sleeping,   0 stopped,   0 zombie", 0.02)
    print_with_delay("%Cpu(s):  8.2 us,  2.1 sy,  0.0 ni, 89.1 id,  0.6 wa,  0.0 hi,  0.0 si,  0.0 st", 0.02)
    print_with_delay("MiB Mem :  16384.0 total,   2048.0 free,   8192.0 used,   6144.0 buff/cache", 0.02)
    print_with_delay("MiB Swap:   2048.0 total,   1024.0 free,   1024.0 used.  10240.0 avail Mem", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND", 0.02)
    print_with_delay(" 1234 www-data  20   0  1234567  123456  12345 S   5.2   0.8   1:23.45 nginx", 0.02)
    print_with_delay(" 1235 www-data  20   0  1234567  123456  12345 S   4.8   0.8   1:12.34 nginx", 0.02)
    print_with_delay(" 1236 mysql     20   0  2345678  234567  23456 S   3.2   1.4   2:34.56 mysqld", 0.02)
    print_with_delay(" 1237 redis     20   0   567890   56789   5678 S   2.1   0.3   0:45.67 redis-server", 0.02)
    time.sleep(2)

def simulate_disk_check():
    print_command("df -h")
    print_with_delay("Filesystem      Size  Used Avail Use% Mounted on", 0.02)
    print_with_delay("/dev/sda1        50G   35G   13G  73% /", 0.02)
    print_with_delay("tmpfs           8.0G     0  8.0G   0% /dev/shm", 0.02)
    print_with_delay("tmpfs           4.0G  4.0K  4.0G   1% /run", 0.02)
    print_with_delay("tmpfs           5.0M     0  5.0M   0% /run/lock", 0.02)
    print_with_delay("tmpfs           8.0G     0  8.0G   0% /sys/fs/cgroup", 0.02)
    print_warning("WARNING: Disk usage is high (73%)", 0.02)
    time.sleep(1)

def simulate_log_analysis():
    print_command("tail -f /var/log/nginx/error.log")
    print_with_delay("2024/01/15 14:30:12 [error] 1234#0: *5678 connect() failed (111: Connection refused) while connecting to upstream", 0.02)
    print_with_delay("2024/01/15 14:30:15 [error] 1234#0: *5679 upstream timed out (110: Connection timed out) while SSL handshaking", 0.02)
    print_with_delay("2024/01/15 14:30:18 [error] 1234#0: *5680 upstream sent invalid header while reading response header from upstream", 0.02)
    print_with_delay("2024/01/15 14:30:21 [error] 1234#0: *5681 upstream sent too big header while reading response header from upstream", 0.02)
    time.sleep(2)
    
    print_command("grep 'ERROR' /var/log/application.log | tail -10")
    print_with_delay("2024-01-15 14:30:12 ERROR [main] Database connection failed: timeout", 0.02)
    print_with_delay("2024-01-15 14:30:15 ERROR [main] Cache miss for key: user:12345", 0.02)
    print_with_delay("2024-01-15 14:30:18 ERROR [main] API rate limit exceeded", 0.02)
    print_with_delay("2024-01-15 14:30:21 ERROR [main] Memory allocation failed", 0.02)
    time.sleep(1)

def simulate_network_troubleshooting():
    print_command("netstat -tulpn | grep :80")
    print_with_delay("tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1234/nginx", 0.02)
    print_with_delay("tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      1234/nginx", 0.02)
    time.sleep(1)
    
    print_command("ping -c 3 google.com")
    print_with_delay("PING google.com (142.250.191.78) 56(84) bytes of data.", 0.02)
    print_with_delay("64 bytes from 142.250.191.78: icmp_seq=1 time=15.2 ms", 0.02)
    print_with_delay("64 bytes from 142.250.191.78: icmp_seq=2 time=14.8 ms", 0.02)
    print_with_delay("64 bytes from 142.250.191.78: icmp_seq=3 time=15.1 ms", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("--- google.com ping statistics ---", 0.02)
    print_with_delay("3 packets transmitted, 3 received, 0% packet loss, time 2002ms", 0.02)
    print_with_delay("rtt min/avg/max/mdev = 14.800/15.033/15.200/0.200 ms", 0.02)
    time.sleep(1)

def simulate_database_maintenance():
    print_command("mysql -u root -p -e 'SHOW PROCESSLIST;'")
    print_with_delay("Enter password: ", 0.02)
    time.sleep(0.5)
    print_with_delay("Id  User     Host            db   Command  Time  State             Info", 0.02)
    print_with_delay("1   root     localhost       NULL Query   0     starting          SHOW PROCESSLIST", 0.02)
    print_with_delay("2   app_user localhost       app  Sleep   45    NULL              NULL", 0.02)
    print_with_delay("3   app_user localhost       app  Query   120   Sending data      SELECT * FROM users WHERE...", 0.02)
    print_with_delay("4   app_user localhost       app  Sleep   30    NULL              NULL", 0.02)
    time.sleep(1)
    
    print_command("mysql -u root -p -e 'SHOW ENGINE INNODB STATUS\\G'")
    print_with_delay("Enter password: ", 0.02)
    time.sleep(0.5)
    print_with_delay("*************************** 1. row ***************************", 0.02)
    print_with_delay("  Type: InnoDB", 0.02)
    print_with_delay("  Name:", 0.02)
    print_with_delay("Status:", 0.02)
    print_with_delay("=====================================", 0.02)
    print_with_delay("2024-01-15 14:30:25 0x7f8b8c0b6700 INNODB MONITOR OUTPUT", 0.02)
    print_with_delay("=====================================", 0.02)
    print_with_delay("Per second averages calculated from the last 45 seconds", 0.02)
    print_with_delay("-----------------", 0.02)
    print_with_delay("BACKGROUND THREAD", 0.02)
    print_with_delay("-----------------", 0.02)
    print_with_delay("srv_master_thread loops: 1234 srv_active, 0 srv_shutdown, 0 srv_idle", 0.02)
    print_with_delay("srv_master_thread log flush and writes: 1234", 0.02)
    time.sleep(2)

def simulate_security_check():
    print_command("fail2ban-client status")
    print_with_delay("Status for the jail: sshd", 0.02)
    print_with_delay("|- Filter", 0.02)
    print_with_delay("|  |- Currently failed: 5", 0.02)
    print_with_delay("|  |- Total failed: 1234", 0.02)
    print_with_delay("|  `- File list: /var/log/auth.log", 0.02)
    print_with_delay("`- Actions", 0.02)
    print_with_delay("   |- Currently banned: 3", 0.02)
    print_with_delay("   |- Total banned: 567", 0.02)
    print_with_delay("   `- Banned IP list: 192.168.1.100 10.0.0.50 172.16.0.25", 0.02)
    time.sleep(1)
    
    print_command("ss -tulpn | grep LISTEN")
    print_with_delay("Netid  State   Recv-Q  Send-Q  Local Address:Port  Peer Address:Port  Process", 0.02)
    print_with_delay("tcp    LISTEN  0        128     0.0.0.0:22          0.0.0.0:*          users:(('sshd',pid=1234,fd=3))", 0.02)
    print_with_delay("tcp    LISTEN  0        128     0.0.0.0:80          0.0.0.0:*          users:(('nginx',pid=1235,fd=6))", 0.02)
    print_with_delay("tcp    LISTEN  0        128     0.0.0.0:443         0.0.0.0:*          users:(('nginx',pid=1235,fd=7))", 0.02)
    print_with_delay("tcp    LISTEN  0        128     127.0.0.1:3306      0.0.0.0:*          users:(('mysqld',pid=1236,fd=10))", 0.02)
    time.sleep(1)

def simulate_backup_process():
    print_command("rsync -avz --progress /var/www/ /backup/www/")
    print_with_delay("sending incremental file list", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("index.html", 0.02)
    print_with_delay("         1,234 bytes 100%    1.23MB/s    0:00:01", 0.02)
    print_with_delay("style.css", 0.02)
    print_with_delay("         5,678 bytes 100%    5.67MB/s    0:00:01", 0.02)
    print_with_delay("script.js", 0.02)
    print_with_delay("         9,012 bytes 100%    9.01MB/s    0:00:01", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("sent 15,924 bytes  received 1,234 bytes  34,316.00 bytes/sec", 0.02)
    print_with_delay("total size is 123,456,789  speedup is 7,654.32", 0.02)
    time.sleep(2)

def simulate_performance_optimization():
    print_command("free -h")
    print_with_delay("              total        used        free      shared  buff/cache   available", 0.02)
    print_with_delay("Mem:           16Gi       8.0Gi       2.0Gi       123Mi       6.0Gi       7.5Gi", 0.02)
    print_with_delay("Swap:          2.0Gi       1.0Gi       1.0Gi", 0.02)
    time.sleep(1)
    
    print_command("iostat -x 1 3")
    print_with_delay("Linux 5.4.0-74-generic (server)  01/15/2024  _x86_64_        (4 CPU)", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("avg-cpu:  %user   %nice %system %iowait  %steal   %idle", 0.02)
    print_with_delay("           8.25    0.00    2.15    1.20    0.00   88.40", 0.02)
    print_with_delay("", 0.01)
    print_with_delay("Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %util", 0.02)
    print_with_delay("sda              5.20    2.10    123.45     67.89     0.00     0.50   2.30", 0.02)
    time.sleep(2)

def main():
    print(f"{Fore.CYAN}=== 서버 관리 ==={Style.RESET_ALL}")
    print()
    
    simulate_system_check()
    print()
    
    simulate_disk_check()
    print()
    
    simulate_log_analysis()
    print()
    
    simulate_network_troubleshooting()
    print()
    
    simulate_database_maintenance()
    print()
    
    simulate_security_check()
    print()
    
    simulate_backup_process()
    print()
    
    simulate_performance_optimization()
    print()

if __name__ == "__main__":
    main() 