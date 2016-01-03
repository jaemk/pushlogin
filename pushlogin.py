from pushbullet import Pushbullet
import os

import settings

# Context manager to suppress stdout and stderr.
class suppress_stdout_stderr(object):
    ''' Class to suppress pushbullet output '''
    def __init__(self):
        # Open a pair of null files
        self.null_fds =  [os.open(os.devnull,os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0],1)
        os.dup2(self.null_fds[1],2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0],1)
        os.dup2(self.save_fds[1],2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])


def _read_key():
    key = settings.key
    if not key:
         print("No key found in 'settings.py'\n",
               "Formatting:\n",
               "      key = 'enterkeytexthere'\n")
    return key


def main():
    key = _read_key()
    with suppress_stdout_stderr():
        pb = Pushbullet(key)
        push = pb.push_note("SSH Login!", "Notification of successful ssh login.")


if __name__ == '__main__':
    main()

