# Assuming you know which functions are disabled (i.e. via phpinfo) find out if any dangerous functions are still allowed
# Reads a file named "disabled.txt" with the functions separated by newlines

# Dangerous functions list from https://github.com/teambi0s/dfunc-bypasser/blob/master/dfunc-bypasser.py
dangerous_functions = ['pcntl_alarm','pcntl_fork','pcntl_waitpid','pcntl_wait','pcntl_wifexited','pcntl_wifstopped','pcntl_wifsignaled','pcntl_wifcontinued','pcntl_wexitstatus','pcntl_wtermsig','pcntl_wstopsig','pcntl_signal','pcntl_signal_get_handler','pcntl_signal_dispatch','pcntl_get_last_error','pcntl_strerror','pcntl_sigprocmask','pcntl_sigwaitinfo','pcntl_sigtimedwait','pcntl_exec','pcntl_getpriority','pcntl_setpriority','pcntl_async_signals','error_log','system','exec','shell_exec','popen','proc_open','passthru','link','symlink','syslog','ld','mail']
not_disabled = dangerous_functions

with open("disabled.txt", 'r') as file:
    for line in file:
        func = line.strip()
        if func in dangerous_functions:
            not_disabled.remove(func)
print(not_disabled)
